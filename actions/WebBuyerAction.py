# encoding: utf-8

"""
__author__ = "Zhang Pengfei"
__date__ = 2018/10/23
"""
from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json


class WebBuyerAction(object):

    def __init__(self, buyer):
        """
        初始化方法的一个常用数据
        :param buyer: 传的是一个用户对象
        """
        self.log = Log('buyer')
        self.buyer = buyer
        self.data_sso = Config('sso').data
        self.data_trade = Config('trade').data
        self.data_sms = Config('sms').data
        self.request = Request()
        self.tool = Tool()
        self.ps = 10

    def web_buyer_update_user(self, real_name, sex, company_name, company_post, head_img=None):
        """
        修改个人信息
        :param real_name: 名字
        :param sex:性别, 男或女
        :param company_name: 公司名称
        :param company_post: 公司职位
        :param head_img: 头像
        :return:
        """
        gender = {'男': 1, '女': 2}
        update_data = self.data_trade['http://dev.trade.worldfarm.com']['/web/buyer/user/update']
        update_data["head_img"] = head_img
        update_data["realName"] = real_name
        update_data["sex"] = gender[sex]
        update_data["companyName"] = company_name
        update_data["companyPosition"] = company_post
        update_data["_tk_"] = self.buyer.token
        update_data["_deviceId_"] = self.buyer.device_id
        self.request.post(url="http://dev.trade.worldfarm.com/web/buyer/user/update",
                          data=update_data)
        user_info = self.tool.query_user_info_by_mobile(self.buyer.mobile)[0]
        assert user_info["real_name"] == real_name
        assert user_info["sex"] == gender[sex]
        assert user_info["company_name"] == company_name
        assert user_info["company_position"] == company_post
        assert user_info["head_img"] == head_img
        self.log.logger.debug("姓名 更新为 %s" % real_name)
        self.log.logger.debug("性别 更新为 %s" % sex)
        self.log.logger.debug("公司 更新为 %s" % company_name)
        self.log.logger.debug("职位 更新为 %s" % company_post)
        self.log.logger.debug("头像 更新为 %s" % head_img)

    def web_change_password(self, newpwd):
        """
        修改密码
        :param newpwd: 新密码,6-15位数字和字母的组合
        :return:
        """
        data = self.data_sso.get('http://dev.sso.worldfarm.com').get('/web/sso/update-pwd')
        data['mobile'] = self.buyer.mobile
        data['password'] = self.buyer.password
        data['newPassword'] = newpwd
        data['token'] = self.buyer.token
        data["_deviceId_"] = self.buyer.device_id
        r = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/update-pwd', data=data).decode('utf-8')
        print(r)
        self.log.logger.debug("修改密码为: %s" % newpwd)

    def web_get_farm_list(self, city_id=None, farm_type=None, min_price=None, max_price=None,
                          min_area=None, max_area=None, sort_code=2):
        """
        获取农场列表
        :return:
        """
        data = self.data_trade['http://dev.trade.worldfarm.com']['/web/buyer/farm/list']
        data['ps'] = self.ps
        data['provinceId'] = city_id
        data['farmTypeList'] = farm_type
        data['minPrice'] = min_price
        data['maxPrice'] = max_price
        data['minArea'] = min_area
        data['maxArea'] = max_area
        data['sortCode'] = sort_code
        data['_language_'] = self.buyer.language
        farm_list = Request().post(url="http://dev.trade.worldfarm.com/web/buyer/farm/list", data=data)
        farm_list_json = json.loads(farm_list).get('content').get('datas')
        query_farm_list = self.tool.query_farm_list()
        for i in range(len(farm_list_json)):
            assert farm_list_json[i].get('id') == query_farm_list[i].get('farm_id')
            assert farm_list_json[i].get('type') == query_farm_list[i].get('type')
            assert farm_list_json[i].get('lng') == query_farm_list[i].get('lng')
            assert farm_list_json[i].get('lat') == query_farm_list[i].get('lat')
            # assert farm_list_json[i].get('imgLisst') == "[" + query_farm_list[i].get('url') + "]"
        return farm_list_json

    def web_get_farm_detail(self, farm_id):
        """
        获取农场详情
        :param farm_id: 农场ID
        :return:
        """
        data = self.data_trade['http://dev.trade.worldfarm.com']['/web/buyer/farm/detail']
        data['farmId'] = farm_id
        data['_language_'] = self.buyer.language
        farm_detail = Request().post(url="http://dev.trade.worldfarm.com/web/buyer/farm/detail", data=data)
        farm_detail_json = json.loads(farm_detail)
        query_farm_detail = self.tool.query_farm_detail_by_farm_id(farm_id)
        assert farm_detail_json.get('content').get('id') == query_farm_detail[0].get('id')
        return farm_detail

    def web_get_farm_list_first_id(self):
        """
        获取农场的ID
        :return:
        """
        farm_detail = self.web_get_farm_detail(self.web_get_farm_list()[0]['id'])
        farm_id = json.loads(farm_detail)['content']['id']
        return farm_id

    def web_get_customer_id_by_farm(self, farm_id):
        """
        获取农场对应的客服ID
        :param farm_id: 农场ID
        :return:
        """
        farm_detail = self.web_get_farm_detail(farm_id)
        farm_detail_json = json.loads(farm_detail)
        customer_service_id = farm_detail_json['content']['customerServiceId']
        return customer_service_id

    def web_get_order_no(self, farm_id):
        """
        生成订单,并返回订单号
        :param farm_id: 农场ID
        :return: 订单No
        """
        data = self.data_trade['http://dev.trade.worldfarm.com']['/web/order/submit-order']
        data['farmId'] = farm_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        order_no = Request().post(url="http://dev.trade.worldfarm.com/web/order/submit-order", data=data)
        order_no_json = json.loads(order_no)
        return order_no_json['content']['orderNo']

    def web_get_customer_account(self, farm_id):
        """
        获取客服IM返回客服的登录账户
        :param farm_id: 农场ID
        :return:
        """
        data = self.data_sms['http://dev.sms.worldfarm.com']['/web/im-auth/buyer/get/service-accid']
        data['userId'] = self.web_get_customer_id_by_farm(farm_id)
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        service_id = Request().post(url="http://dev.sms.worldfarm.com"
                                        "/web/im-auth/buyer/get/service-accid", data=data)
        service_id = str(json.loads(service_id)['content']).split('@')[0]
        account = self.tool.query_employee_user_no_by_user_id(service_id)
        return account

    def web_buyer_sale_bind(self, sale_id):
        """
        绑定销售ID
        :param sale_id: 销售ID
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/sale-bind')
        data['saleId'] = sale_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        re = Request().post(url="http://dev.trade.worldfarm.com/web/buyer/user/sale-bind", data=data)
        query_sale_id = self.tool.query_sale_id_by_user_id(self.buyer.user_id)[0].get('salesman_id')
        assert sale_id == query_sale_id
        return re

    def web_buyer_query_sale(self, sale_id):
        """
        查询销售
        :param sale_id: 销售ID
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/query-sale')
        data['saleId'] = sale_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        re = Request().post(url="http://dev.trade.worldfarm.com/web/buyer/user/query-sale", data=data)
        query_sale_id = self.tool.query_sale_id_by_user_id(self.buyer.user_id)[0].get('salesman_id')
        assert sale_id == query_sale_id
        return re

    def web_buyer_sale_bind_update(self, sale_id):
        """
        更新销售ID
        :param sale_id: 销售ID
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/sale-bind-update')
        data['saleId'] = sale_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        re = Request().post(url="http://dev.trade.worldfarm.com/web/buyer/user/sale-bind-update", data=data)
        query_sale_id = self.tool.query_sale_id_by_user_id(self.buyer.user_id)[0].get('salesman_id')
        assert sale_id == query_sale_id
        return re

    def web_buyer_user_detail(self):
        """
        查询用户的detail
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/detail')
        if data is None:
            data = {}
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        user_detail = Request().post(url="http://dev.trade.worldfarm.com/web/buyer/user/detail", data=data)
        user_detail_content = eval(user_detail).get('content')
        query_user_detail = self.tool.query_user_detail_by_user_id(self.buyer.user_id)[0]
        assert user_detail_content.get('realName') == query_user_detail.get('real_name')
        return user_detail

    def web_buyer_resource_add(self, farm_id, order_no):
        """
        上传购买资质
        :param farm_id: 农场ID
        :param order_no: 订单的NO
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/add')
        data['farmId'] = farm_id
        data['orderNo'] = order_no
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/web/buyer-resource/add", data=data)
        return r

    def web_buyer_resource_detail(self, order_no):
        """
        订单的购买资质详情
        :param order_no: 订单号
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/detail')
        data['orderNo'] = order_no
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/web/buyer-resource/detail", data=data)
        return r

    def web_buyer_resource_is_add(self, order_no):
        """
        判断订单是否可以上传购买资质
        :param order_no: 订单号
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/is-add')
        data['orderNo'] = order_no
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/web/buyer-resource/is-add", data=data)
        return r

    def web_buyer_resource_list(self, order_no, status, buyer_name):
        """
        购买资质列表
        :param order_no: 订单号
        :param status: 资质状态
        :param buyer_name: 买家姓名
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/resource-list')
        data['orderNo'] = order_no
        data['status'] = status
        data['buyerName'] = buyer_name
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/web/buyer-resource/resource-list", data=data)
        return r

    def web_buyer_farm_recommend_list(self, farm_id):
        """
        农场相关推荐
        :param farm_id: 农场ID
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/farm/recommend-list')
        data['farmId'] = farm_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/web/buyer/farm/recommend-list", data=data)
        return r

    def web_buyer_order_del(self, order_no_list=None):
        """
        买家删除订单
        :param order_no_list: 使用,分割,eg:1,2,3
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/order/del')
        data['orderNoList'] = order_no_list
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/web/order/del", data=data)
        return r

    def web_buyer_order_list(self, type_no=0):
        """
        感兴趣列表
        :param type_no: 0,1;默认填0,1表示查询的list是可以删除的order
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/web/order/list')
        data['type'] = type_no
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/web/order/list", data=data)
        return r