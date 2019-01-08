#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/3/28'
"""


import json
import random
from utils.Log import Log
from utils.Util import DataBaseOperate
from utils.Util import Request
from utils.Config import Config
from backend.Session import EmployeeSession
from backend.Session import UserSession
import os
from utils.Util import Redis
from bs4 import BeautifulSoup
import re
# from utils.Util import AndroidTool

data9602 = Config('9602').data
data9600 = Config('9600').data


class Tool(object):
    L = Log("Tool")

    def query_random_city(self, state_name):
        region_au = Config('RegionAU').data
        city_len = len(region_au[state_name]) - 1
        city = list(region_au[state_name][random.randint(0, city_len)].items())[0]
        city_name = city[0]
        city_dict = city[1]
        self.L.logger.debug("%s 的 随机城市 为 %s" % (state_name, city_name))
        self.L.logger.debug("%s 的 州id 为 %s" % (city_name, city_dict["state"]))
        self.L.logger.debug("%s 的 市id 为 %s" % (city_name, city_dict["city"]))
        self.L.logger.debug("%s 的 地址 为 %s" % (city_name, city_dict["address"]))
        self.L.logger.debug("%s 的 维度lat 为 %s" % (city_name, city_dict["lat"]))
        self.L.logger.debug("%s 的 维度lat 为 %s" % (city_name, city_dict["lng"]))
        return city_name, city_dict

    def get_role_code(self, *role):
        roles = {'地推': 10, '客服': 20, '运营': 30, '翻译': 40, '买家中介': 50, '销售人员': 60, '后台管理': 70}
        role_list = []
        for r in role:
            role_list.append(roles[r])
        self.L.logger.debug('%s 的role_list是 %s' % (json.dumps(role), json.dumps(role_list)))
        return json.dumps(role_list)[1:-1]

    def get_images(self, key='farm'):
        redis = Redis()
        # redis.set('get_index', 0)
        get_index = int(redis.get('get_index'))
        response = Request().get(
            'https://www.pexels.com/search/%s/?page=%s&format=html' % (key, str((get_index / 15) + 1)))
        soup = BeautifulSoup(response)
        images = soup.findAll('a', attrs={'href': re.compile("(^https.*)\?")})
        # list_start = get_index
        # list_end = list_start + 15
        i = 0
        for link in images:
            image_url = '%s&auto=compress\n' % link.get('href')
            self.L.logger.debug(image_url)
            image = Request().get(image_url)
            i += 1
            with open('./Images/banner%s.jpg' % str(i), 'wb') as picture:
                picture.write(image)
        # redis.set('get_index', str(list_end))

    def upload_image(self):
        redis = Redis()
        get_index = int(redis.get('get_index')) - 15
        for i in range(1, 16):
            if round((os.path.getsize("./Images/banner"+str(i)+".jpg"))/1000.0/1000.0, 1) < 5:
                Request().post_file(url="http://39.104.28.40:9600/common/farm/upload-img",
                                    file_path="./Images/banner%s.jpg" % str(i))
                # zyp_url = json.loads(response)["content"]
                # redis.set("image%s" % str(get_index + i), zyp_url)
                self.L.logger.debug("image%s uploaded !" % str(get_index + i))
            else:
                self.L.logger.debug("image%s exceed size !" % str(get_index + i))

    @staticmethod
    def query_user_info_by_mobile(mobile):
        sql = 'SELECT * FROM t_user WHERE mobile = %s AND is_delete = 0;' % str(mobile)
        user_info = DataBaseOperate().operate("39.104.28.40", "farm-uc", sql)
        return user_info

    @staticmethod
    def query_employee_info_by_account(account):
        sql = 'SELECT tu.*,tuv.expiry_time,tuv.visa_time,tur.url ' \
              'FROM `farm-uc`.t_employee te ' \
              'LEFT JOIN `farm-uc`.t_user tu ON te.user_id=tu.id ' \
              'LEFT JOIN `farm-trade`.t_user_visa tuv ON te.user_id=tuv.user_id ' \
              'LEFT JOIN `farm-trade`.t_user_resource tur ON te.user_id=tur.user_id ' \
              'WHERE te.user_no="%s";' % str(account)
        employee_info = DataBaseOperate().operate("39.104.28.40", "farm-uc", sql)
        return employee_info

    def delete_user_by_mobile(self, mobile):
        user_info = Tool.query_user_info_by_mobile(mobile)
        if user_info:
            redis = Redis()
            user_index = int(redis.get('user_index'))
            DataBaseOperate().operate("39.104.28.40", "farm-uc",
                                      'UPDATE t_user SET mobile = "%s" WHERE mobile = "%s";'
                                      % (str(user_index), str(mobile)))
            self.L.logger.debug('原手机号 %s 修改为 %s' % (str(mobile), str(user_index)))
            redis.set('user_index', user_index + 1)
        else:
            raise Exception('手机号输入错误: %s' % str(mobile))

    def query_approve_status(self, mobile):
        approve_status = {'0': '未知', '1': '待审核', '2': '审核未通过', '3': '审核通过'}
        approve_info = DataBaseOperate().operate("39.104.28.40", "farm-uc",
                                                 'SELECT tsa.* FROM	`farm-trade`.t_seller_agency tsa '
                                                 'LEFT JOIN `farm-uc`.t_user tu ON tu.id = tsa.user_id '
                                                 'WHERE tu.mobile = "%s";' % str(mobile))
        if approve_info:
            self.L.logger.debug('手机号 %s, 用户id %s, 审核状态 %s'
                                % (str(mobile), approve_info[0]['user_id'],
                                   approve_status[str(approve_info[0]['status'])]))
        else:
            self.L.logger.debug('手机号 %s 用户未上传中介认证资料')
        return approve_info

    def query_user_id_by_mobile(self, mobile):
        user_ids = DataBaseOperate().operate("39.104.28.40", "farm-uc",
                                             'SELECT id FROM `farm-uc`.t_user WHERE mobile = "%s";'
                                             % str(mobile))
        user_id = user_ids[0]["id"]
        self.L.logger.debug("手机号为 %s 的 中介uid 为 %s" % (str(mobile), str(user_id)))
        return user_id

    def query_latest_farm_info(self, user_id):
        farm_infos = DataBaseOperate().operate("39.104.28.40", "farm-trade",
                                               'SELECT * FROM `farm-trade`.t_farm WHERE seller_agency_id = %s'
                                               ' AND `status` = 20 ORDER BY id DESC LIMIT 1;'
                                               % str(user_id))
        self.L.logger.debug("uid 为 %s的中介 最新农场Id 为 %s" % (str(user_id), str(farm_infos[0]["id"])))
        return farm_infos[0]

    def query_employee_user_no_by_user_id(self, user_id):
        user_no = DataBaseOperate().operate("39.104.28.40", "farm-uc",
                                            'SELECT user_no FROM `farm-uc`.t_employee WHERE user_id = %s;'
                                            % str(user_id))
        self.L.logger.debug('用户id %s 的 工号为 %s' % (str(user_id), str(user_no[0]['user_no'])))
        return user_no[0]['user_no']

    def query_order_id_by_order_no(self, order_no):
        order_id = DataBaseOperate().operate("39.104.28.40", "farm-trade",
                                             'SELECT id FROM `farm-trade`.t_order WHERE order_no = %s;'
                                             % str(order_no))
        self.L.logger.debug('订单号 %s 的 订单id为 %s' % (str(order_no), str(order_id[0]['id'])))
        return order_id[0]['id']

    def query_sale_id_by_user_id(self, user_id):
        sql = "select salesman_id from t_buyer where t_buyer.buyer_id = %s AND is_delete =0;" % str(user_id)
        sale_id = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("查询出用户 %s 的sale_id 是 %s " % (str(user_id), str(sale_id)))
        return sale_id

    def query_farm_list(self):
        sql = "SELECT farm_id, area, area_code,unit_code, total_price, total_rmb,f.type,lng,lat," \
              "GROUP_CONCAT( '{\"type\":', fi.type, ', \"imgUrl\":\"', fi.img_url, '\"}' ) url FROM t_farm f " \
              "left JOIN t_farm_image fi ON fi.farm_id = f.id WHERE f.status = 20 GROUP BY farm_id " \
              "order by f.edit_time desc LIMIT 0,24;"
        farm_list = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("查询出农场列表 %s" % str(farm_list))
        return farm_list

    def query_user_detail_by_user_id(self, user_id):
        sql = "select * from t_user where id = %s AND is_delete =0;" % str(user_id)
        user_info = DataBaseOperate().operate("39.104.28.40", "farm-uc", sql)
        self.L.logger.debug("查询出用户 %s 的信息是 %s " % (str(user_id), str(user_info)))
        return user_info

    def query_order_by_user_id(self, ip, user_id):
        orders = DataBaseOperate().operate(ip, "hcb_tg",
                                           "SELECT order_no FROM hcb_tg.wish_order WHERE buyer_id = %s AND is_delete =0"
                                           % str(user_id))
        self.L.logger.debug("用户ID %s 服务器 %s 订单号 %s" % (str(user_id), str(ip), str(orders)))
        return orders

    def query_farm_list_by_keywords(self, keywords):
        farm_list = DataBaseOperate().operate("39.104.28.40", "farm-trade",
                                              "SELECT farm_name FROM `farm-trade`.t_farm "
                                              "WHERE farm_name like '%%%s%%' AND is_delete =0 "
                                              "order by create_time desc "
                                              % str(keywords))
        farm_name = [farm["farm_name"] for farm in farm_list]
        self.L.logger.debug("模糊查询包括 %s的农场列表为 %s" % (str(keywords), str(farm_list)))
        return farm_name

    def query_remark_by_farm_id(self, farm_id):
        remark = DataBaseOperate().operate("39.104.28.40", "farm-trade",
                                           "SELECT farm_id, remark FROM `farm-trade`.t_seller_agency_remark "
                                           "WHERE farm_id = %s AND is_delete =0"
                                           % str(farm_id))
        self.L.logger.debug("farmid 为 %s的农场 最新备注为 %s" % (str(farm_id), str(remark)))
        return remark

    def query_close_farm_by_farm_id(self, farm_id):
        status = DataBaseOperate().operate("39.104.28.40", "farm-trade",
                                           "SELECT id, status FROM `farm-trade`.t_farm WHERE id = %s AND is_delete =0"
                                           % str(id))
        self.L.logger.debug("farmid 为 %s的农场 下架原因为 %s" % (str(id), str(status)))
        return status

    def query_close_list_by_seller_agency_id(self, seller_agency_id):
        sql="SELECT * FROM `farm-trade`.t_farm tf LEFT JOIN `farm-trade`.t_farm_image `tfi` ON `tfi`.farm_id = tf.id " \
            "WHERE seller_agency_id = %s AND (status = 30 or status = 50) and is_delete =0 " \
            "GROUP BY tf.id  order by closed_time desc; " % str(seller_agency_id)
        close_farm_list = DataBaseOperate().operate("39.104.28.40", "farm-trade",sql)
        self.L.logger.debug("seller_agency_id 为 %s的卖家中介所有关闭农场为 %s" % (str(seller_agency_id), str(close_farm_list)))
        return close_farm_list

    def query_farm_detail_by_farm_id(self, farm_id):
        sql = "SELECT tf.*,tfr.content FROM `farm-trade`.t_farm tf " \
              "LEFT JOIN `farm-trade`.t_farm_remark tfr ON tfr.farm_id=tf.id " \
              "WHERE tf.id= %s AND tfr.is_delete=0" % str(farm_id)
        farm_detail = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("farm_id 为 %s的农场详情为 %s" % (str(farm_id), str(farm_detail)))
        return farm_detail

    def query_farm_list_by_seller_agency_id(self, seller_agency_id):
        sql = "SELECT * FROM `farm-trade`.t_farm farm  " \
              " WHERE seller_agency_id = %s AND is_delete =0 " \
              "AND farm.status IN (10, 20) ORDER BY farm.publish_time DESC LIMIT 20" % str(seller_agency_id)
        farm_list = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("seller_agency_id 为 %s的农场列表为 %s" % (str(seller_agency_id), str(farm_list)))
        return farm_list

    def query_map_list_by_seller_agency_id(self, seller_agency_id):
        sql = "SELECT * FROM `farm-trade`.t_farm farm  " \
              " WHERE seller_agency_id = %s AND is_delete =0 " \
              "AND farm.status IN (10, 20) ORDER BY farm.publish_time DESC LIMIT 20" % str(seller_agency_id)
        map_list = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("seller_agency_id 为 %s的地图农场列表为 %s" % (str(seller_agency_id), str(map_list)))
        return map_list

    def query_farmer_detail_by_farm_id(self, farm_id):
        sql = "SELECT * FROM `farm-trade`.t_farmer  " \
              " WHERE farm_id = %s AND is_delete =0 " % str(farm_id)
        famer_detail = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("farm_id 为 %s的农场主信息为 %s" % (str(farm_id), str(famer_detail)))
        return famer_detail

    def query_user_status_by_seller_agency_id(self, seller_agency_id):
        sql = "SELECT * FROM `farm-trade`.t_seller_agency  " \
              " WHERE user_id = %s AND is_delete =0 " % str(seller_agency_id)
        user_status = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("seller_agency_id 为 %s的认证经纪人信息为 %s" % (str(seller_agency_id), str(user_status)))
        return user_status

    def query_buyer_list_by_farm_id(self, farm_id):
        sql = "SELECT * FROM `farm-trade`.t_order ftto  " \
              "WHERE ftto.farm_id = %s AND ftto.order_status != 40 AND ftto.is_delete = 0 " \
              "ORDER BY ftto.order_status DESC, ftto.create_time DESC " % str(farm_id)
        user_list = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("farm_id 为 %s的意向买家列表为 %s" % (str(farm_id), str(user_list)))
        return user_list

    def query_message_buyer_list_by_farm_id(self, seller_agency__id):
        sql = "SELECT * FROM `farm-trade`.t_order ftto  LEFT JOIN `farm-uc`.t_user tu ON tu.id = ftto.buyer_id " \
              "LEFT JOIN `farm-trade`.t_farm tf ON tf.id = ftto.farm_id LEFT JOIN `farm-trade`.t_farm_image tfi " \
              "ON tfi.farm_id = tf.id WHERE ftto.seller_agency_id = %s AND ftto.order_status != 40 " \
              "AND tfi.is_delete = 0 AND tfi.type = 1 ORDER BY ftto.order_status DESC, " \
              "ftto.create_time DESC;" % str(seller_agency__id)
        user_list = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("seller_agency_id 为 %s的意向买家列表状态为 %s" % (str(seller_agency__id), str(user_list)))
        return user_list

    def query_farm_list_by_seller_agency_id(self, keywords,seller_agency_id):
        sql = "SELECT *  FROM `farm-trade`.t_farm WHERE farm_name like '%%%s%%'" \
              "and seller_agency_id = %s AND is_delete =0 " \
              "order by create_time desc " % (str(keywords), str(seller_agency_id))
        farm_list = DataBaseOperate().operate("39.104.28.40", "farm-trade", sql)
        self.L.logger.debug("seller_agency_id 为 %s的农场列表为 %s" % (str(seller_agency_id), str(farm_list)))
        return farm_list


    def delete_order_by_user_id(self, ip, admin_st, admin_sid, tg, user_id):
        orders = self.query_order_by_user_id(ip, user_id)
        if len(orders) > 0:
            for n in range(len(orders)):
                Request().post(
                    url=tg + "/web/admin/manager/delOrder",
                    data="st=%s&sid=%s&orderNo=%s" %
                         (admin_st, admin_sid, orders[n]["order_no"]))
                self.L.logger.debug("用户ID %s 订单 %s 删除成功" % (str(user_id), orders[n]["order_no"]))
        else:
            self.L.logger.debug("用户ID %s 无订单可删除" % str(user_id))

    def send_verify_code(self, host, mobile):
        url = host + "/web/sms/getVerifyCode"
        Request().post(url=url, data="mobile=%s" % str(mobile))
        self.L.logger.debug("手机号 %s 发送验证码成功" % str(mobile))

    @staticmethod
    def test():
        redis = Redis()
        for i in range(160):
            j = redis.get("image%s" % str(i))
            if j is None:
                print("image%s" % str(i))
            else:
                pass

    def operator_approve_seller_agent(self, mobile, status=False):
        operator = EmployeeSession('100031', '123456')
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/cs/seller-agency/list']
        data['status'] = 1
        data['_tk_'] = operator.token
        data['_deviceId_'] = operator.deviceId
        wait = Request().post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/list',
                              data=data)
        wait_list = json.loads(wait)['content']['datas']
        for i in wait_list:
            if i['mobile'] == mobile:
                Request().post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/detail-resource-list',
                               data={'_tk_': operator.token, '_deviceId_': operator.deviceId, 'id': i['id']})
                audit_data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/cs/seller-agency/audit']
                audit_data['_tk_'] = operator.token
                audit_data['_deviceId_'] = operator.deviceId
                audit_data['id'] = i['id']
                if status:
                    # type=1表示通过
                    audit_data['type'] = 1
                    Request().post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/audit',
                                   data=audit_data)
                    self.L.logger.debug('手机号 %s 的用户上传的中介资料审核通过' % str(mobile))
                else:
                    # type=2表示审核不通过
                    audit_data['type'] = 2
                    Request().post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/audit',
                                   data=audit_data)
                    self.L.logger.debug('手机号 %s 的用户上传的中介资料审核未通过' % str(mobile))
            else:
                pass

    def operator_account_seller_agent(self):
        operator = EmployeeSession('100031', '123456')
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/cs/seller-agency/pending-count']
        if data:
            pass
        else:
            data = {}
        data['status'] = 1
        data['_tk_'] = operator.token
        data['_deviceId_'] = operator.deviceId
        r = Request().post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/pending-count',
                           data=data)
        print(r)

    def seller_agent_search_farm(self, keyWords, language):
        seller = UserSession('18602832572', '123456a')
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/farm/search']
        data['_language_'] = language
        data['_tk_'] = seller.token
        data['_deviceId_'] = seller.deviceId
        data['keyWords'] = keyWords
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/farm/search', data=data)
        r_content = json.loads(r)
        print(r_content)
        return r_content

    def seller_agency_add_remark(self, farmId, remark, language):
        seller = UserSession('18602832572', '123456a')
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/add-remark']
        data['_language_'] = language
        data['_tk_'] = seller.token
        data['_deviceId_'] = seller.deviceId
        data['farmId'] = farmId
        data['remark'] = remark
        Add = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/add-remark', data=data)
        Add_remark = json.loads(Add)
        return Add_remark

    def seller_agency_close_farm(self, farmId, type, language):
        seller = UserSession('18602832572', '123456a')
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/close']
        data['_language_'] = language
        data['_tk_'] = seller.token
        data['_deviceId_'] = seller.deviceId
        data['farmId'] = farmId
        data['type'] = type #30已售出50暂不销售
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/close', data=data)
        r_close = json.loads(r)
        return r_close




# class AdminOperate(object):
#     L = Log("AdminOperate")
#     android_tool = AndroidTool()
#     buyer = TruckUser(data["Newtruck"]["Buyer"])
#     sale = TruckUser(30800, "employee")
#
#     def submit_order_by_sale(self, unit_mobile, verify_code):
#         self.android_tool.set_up_admin()
#         self.android_tool.enter_new_truck_page(unit_mobile, verify_code)
#         self.android_tool.d(text="订单采集").click()
#         self.android_tool.d(resourceId="com.wlqq.phantom.plugin.newcar:id/et_name").set_text(self.buyer.real_name())
#         self.android_tool.d(resourceId="com.wlqq.phantom.plugin.newcar:id/et_phone").set_text(self.buyer.mobile())
#         self.android_tool.d(text="点击获取").click()
#         sleep(3)
#         db_query = DataBaseOperate().operate("10.2.1.8", "logisticsqq",
#                                              "SELECT content FROM t_sms_record WHERE mobile = " +
#                                              "%s" % self.buyer.mobile() +
#                                              " AND DATE_FORMAT(send_time, '%Y-%m-%d') "
#                                              "= CURRENT_DATE() ORDER BY `id` DESC LIMIT 1;")
#         verify_code = db_query[0]["content"][:4]
#         sleep(3)
#         self.android_tool.d(resourceId="com.wlqq.phantom.plugin.newcar:id/et_varificationCode")\
#             .set_text(str(verify_code))
#         self.android_tool.d(resourceId="com.wlqq.phantom.plugin.newcar:id/rl_local_address").click()
#         self.android_tool.d(text="成都").click()
#         self.android_tool.d(text="提交").click()
#         sleep(3)
#         self.android_tool.tear_down_admin()


# if __name__ == '__main__':
#     # Tool().operator_approve_seller_agent('18602832572', status=True)
#     # Tool().get_role_code('地推', '客服', '运营')
#     # Tool().query_approve_status("18602832572")
#     # Tool().seller_agent_search_farm('漫花庄园', language='zh')
#     # Tool().seller_agency_add_remark(516, "lalal", language='zh')
#     Tool().seller_agency_close_farm(516, 30, language='zh')
# #     r = Redis()
#     for i in range(75, 76):
#         try:
#             v = r.get("image%s" % str(i))
#         except AttributeError:
#             print("image%s" % str(i))
    # t = Tool()
    # t.get_images()
    # user_id = t.query_employee_user_no_by_uesr_id(405)
    # print user_id
    # t.query_latest_farm_info(user_id)
    # t.test()
    # t.upload_image()
    # q = Query()
    # q.query_random_city("新南威尔士")
