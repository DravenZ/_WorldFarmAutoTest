# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json


class AppBuyerAction(object):

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

    def app_buyer_interest_or_not(self, farm_id):
        """
        买家加星或者取消加星
        :param farm_id: 农场ID
        :return: 返回成功或者失败或者未返回则是抛异常
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/interest/interest-or-not')
        data['farmId'] = farm_id
        data["_tk_"] = self.buyer.token
        data["_deviceId_"] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        response = self.request.post(url="http://dev.trade.worldfarm.com/mobile/buyer/interest/interest-or-not",
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return True
        elif json_response["status"] == "ERROR":
            json_response["errorMsg"] = "加星失败!"
            return False
        else:
            raise Exception("status未返回OK或ERROR")

    def app_buyer_batch_cancel_interest(self, farm_id_list):
        """
        批量取消加星
        :param farm_id_list: 农场ID列表
        :return: 返回成功或者失败或者未返回则是抛异常
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/interest/batch-cancel-interest')
        data['farmIds'] = farm_id_list
        data["_tk_"] = self.buyer.token
        data["_deviceId_"] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        response = self.request.post(url="http://dev.trade.worldfarm.com/mobile/buyer/interest/batch-cancel-interest",
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return True
        elif json_response["status"] == "ERROR":
            json_response["errorMsg"] = "加星失败!"
            return False
        else:
            raise Exception("status未返回OK或ERROR")

    def app_buyer_interest_farm_list(self):
        """
        加星的列表,即感兴趣列表
        :return: 正确返回农场列表,失败返回False
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/interest/interest-farm-list')
        data['ps'] = self.ps
        data['pn'] = 1
        data["_tk_"] = self.buyer.token
        data["_deviceId_"] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        response = self.request.post(url="http://dev.trade.worldfarm.com/mobile/buyer/interest/interest-farm-list",
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            json_response["errorMsg"] = "加载失败!"
            return False
        else:
            raise Exception("status未返回OK或ERROR")

    def app_buyer_get_banner_by_type(self, banner_type):
        """
        根据类型获取banner
        :param banner_type: banner的类型
        :return: 返回banner
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/banner/get-by-type')
        data['type'] = banner_type
        data['ps'] = self.ps
        data['pn'] = 1
        data['_language_'] = self.buyer.language
        response = self.request.post(url="http://dev.trade.worldfarm.com/mobile/banner/get-by-type",
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            json_response["errorMsg"] = "加载失败!"
            return False
        else:
            raise Exception("status未返回OK或ERROR")

    def app_buyer_intent_livestock_order(self, name, mobile, contact_information):
        """
        创建畜牧的意向订单
        :param name: 姓名
        :param mobile: 手机号
        :param contact_information: 邮箱
        :return: 成功返回订单号
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/intent-order/add-livestock')
        data['name'] = name
        data['mobile'] = mobile
        data['contactInformation'] = contact_information
        data['_language_'] = self.buyer.language
        response = self.request.post(url="http://dev.trade.worldfarm.com/mobile/intent-order/add-livestock",
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            json_response["errorMsg"] = "创建畜牧服务的意向订单失败!"
            return False
        else:
            raise Exception("status未返回OK或ERROR")

    def app_buyer_intent_translation_order(self, farm_id):
        """
        创建翻译服务的意向订单
        :param farm_id: 农场的ID
        :return: 成功返回创建的订单编号
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/intent-order/add-translation')
        data['farmId'] = farm_id
        data['_language_'] = self.buyer.language
        response = self.request.post(url="http://dev.trade.worldfarm.com/mobile/intent-order/add-translation",
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            json_response["errorMsg"] = "创建翻译服务的意向订单失败!"
            return False
        else:
            raise Exception("status未返回OK或ERROR")

    def app_buyer_update_user(self, real_name, sex, company_name, company_post, head_img=None):
        """
        修改个人信息
        :param real_name: 姓名
        :param sex: 性别,男或女
        :param company_name: 公司名称
        :param company_post: 公司职位
        :param head_img: 头像url
        :return:
        """
        gender = {'男': 1, '女': 2}
        update_data = self.data_trade['http://dev.trade.worldfarm.com']['/mobile/buyer/user/update']
        update_data["head_img"] = head_img
        update_data["realName"] = real_name
        update_data["sex"] = gender[sex]
        update_data["companyName"] = company_name
        update_data["companyPosition"] = company_post
        update_data["_tk_"] = self.buyer.token
        update_data["_deviceId_"] = self.buyer.device_id
        update_data['_language_'] = self.buyer.language
        self.request.post(url="http://dev.trade.worldfarm.com/mobile/buyer/user/update",
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

    def app_change_password(self, newpwd):
        """
        修改密码
        :param newpwd: 新密码
        :return:
        """
        data = self.data_sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/update-pwd')
        data['mobile'] = self.buyer.mobile
        data['password'] = self.buyer.password
        data['newPassword'] = newpwd
        data['token'] = self.buyer.token
        data["_deviceId_"] = self.buyer.device_id
        r = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/update-pwd', data=data).decode('utf-8')
        print(r)
        self.log.logger.debug("修改密码为: %s" % newpwd)

    def app_get_farm_list(self, city_id=None, farm_type=None, min_price=None, max_price=None,
                          min_area=None, max_area=None, sort_code=2):
        """
        获取农场列表
        :return:
        """
        data = self.data_trade['http://dev.trade.worldfarm.com']['/mobile/buyer/farm/list']
        data['ps'] = self.ps
        data['provinceId'] = city_id
        data['farmTypeList'] = farm_type
        data['minPrice'] = min_price
        data['maxPrice'] = max_price
        data['minArea'] = min_area
        data['maxArea'] = max_area
        data['sortCode'] = sort_code
        data['_language_'] = self.buyer.language
        farm_list = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/farm/list", data=data)
        farm_list_json = json.loads(farm_list).get('content').get('datas')
        # query_farm_list = self.tool.query_farm_list()
        # for i in range(len(farm_list_json)):
        #     assert farm_list_json[i].get('id') == query_farm_list[i].get('farm_id')
        #     assert farm_list_json[i].get('type') == query_farm_list[i].get('type')
        #     assert farm_list_json[i].get('lng') == query_farm_list[i].get('lng')
        #     assert farm_list_json[i].get('lat') == query_farm_list[i].get('lat')
        #     assert farm_list_json[i].get('imgLisst') == "[" + query_farm_list[i].get('url') + "]"
        return farm_list_json

    def app_buyer_get_map_list(self, left_top_lng, left_top_lat, right_bottom_lng, right_bottom_lat, zoom_level,
                               province_id, sort_code=1, nation_id=25, trigger=None, farm_type_list=None,
                               min_price=None, max_price=None, min_area=None, max_area=None):
        """
        地图农场列表
        :param left_top_lng: 左上角的经度
        :param left_top_lat: 左上角的未读
        :param right_bottom_lng: 右下角的经度
        :param right_bottom_lat: 右下角的未读
        :param zoom_level: 聚合等级
        :param province_id: 城市ID
        :param sort_code: 排序的code
        :param nation_id: 国家的ID
        :param trigger:
        :param farm_type_list: 农场类型集合
        :param min_price: 最小的价格
        :param max_price: 最大的价格
        :param min_area: 最小的面积
        :param max_area: 最大的面积
        :return:
        """
        data = self.data_trade['http://dev.trade.worldfarm.com']['/mobile/buyer/farm/map-list']
        data['leftTopLng'] = left_top_lng
        data['leftTopLat'] = left_top_lat
        data['rightBottomLng'] = right_bottom_lng
        data['rightBottomLat'] = right_bottom_lat
        data['zoomLevel'] = zoom_level
        data['nationId'] = nation_id
        data['provinceId'] = province_id
        data['trigger'] = trigger
        data['farmTypeList'] = farm_type_list
        data['trigger'] = trigger
        data['minPrice'] = min_price
        data['maxPrice'] = max_price
        data['minArea'] = min_area
        data['maxArea'] = max_area
        data['sortCode'] = sort_code
        data['ps'] = self.ps
        data['_language_'] = self.buyer.language
        farm_list = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/farm/map-list", data=data)
        farm_list_json = json.loads(farm_list)
        return farm_list_json.get('content').get('datas')

    def app_get_farm_detail(self, farm_id):
        """
        获取农场详情
        :return:
        """
        data = self.data_trade['http://dev.trade.worldfarm.com']['/mobile/buyer/farm/detail']
        data['farmId'] = farm_id
        data['_language_'] = self.buyer.language
        farm_detail = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/farm/detail", data=data)
        json_response = json.loads(farm_detail)
        if json_response["status"] == "OK":
            farm_json = json_response["content"]
            farm_data_base = self.tool.query_farm_detail_by_farm_id(farm_id)[0]
            assert farm_json["address"] == farm_data_base["address"]
            assert farm_json["addressEn"] == farm_data_base["address_en"]
            assert farm_json["area"] == farm_data_base["area"]
            assert farm_json["areaCode"] == farm_data_base["area_code"]
            assert farm_json["farmName"] == farm_data_base["farm_name"]
            assert farm_json["farmNameEn"] == farm_data_base["farm_name_en"]
            assert farm_json["id"] == farm_data_base["id"]
            assert farm_json["languageType"] == farm_data_base["language_type"]
            assert farm_json["lat"] == farm_data_base["lat"]
            assert farm_json["lng"] == farm_data_base["lng"]
            assert farm_json["totalPrice"] == farm_data_base["total_price"]
            assert farm_json["type"] == farm_data_base["type"]
            assert farm_json["unitCode"] == farm_data_base["unit_code"]
            return farm_json
        else:
            raise Exception("Error: %s" % json_response["errorMsg"])

    def app_get_farm_list_first_id(self):
        """
        获取列表第一个农场的ID
        :return:
        """
        farm_detail = self.app_get_farm_detail(self.app_get_farm_list()[0]['id'])
        farm_id = json.loads(farm_detail)['content']['id']
        return farm_id

    def app_get_customer_id_by_farm(self, farm_id):
        """
        获取农场对应的客服ID
        :return:
        """
        farm_detail = self.app_get_farm_detail(farm_id)
        farm_detail_json = json.loads(farm_detail)
        customer_service_id = farm_detail_json['content']['customerServiceId']
        return customer_service_id

    def app_get_order_no(self, farm_id):
        """
        生成订单,并返回订单号
        :param farm_id: 农场ID
        :return: 订单No
        """
        data = self.data_trade['http://dev.trade.worldfarm.com']['/mobile/order/submit-order']
        data['farmId'] = farm_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        order_no = Request().post(url="http://dev.trade.worldfarm.com/mobile/order/submit-order", data=data)
        order_no_json = json.loads(order_no)
        return order_no_json['content']['orderNo']

    def app_get_customer_account(self, farm_id):
        """
        获取客服IM返回客服的登录账户
        :return:
        """
        data = self.data_sms['http://dev.sms.worldfarm.com']['/mobile/im-auth/buyer/get/service-accid']
        data['userId'] = self.app_get_customer_id_by_farm(farm_id)
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        service_id = Request().post(url="http://dev.sms.worldfarm.com"
                                        "/mobile/im-auth/buyer/get/service-accid", data=data)
        service_id = str(json.loads(service_id)['content']).split('@')[0]
        account = self.tool.query_employee_user_no_by_user_id(service_id)
        return account

    def app_buyer_sale_bind(self, sale_id):
        """
        绑定销售ID
        :param sale_id:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/sale-bind')
        data['saleId'] = sale_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        re = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/user/sale-bind", data=data)
        query_sale_id = self.tool.query_sale_id_by_user_id(self.buyer.user_id)[0].get('salesman_id')
        assert sale_id == query_sale_id
        return re

    def app_buyer_query_sale(self, sale_id):
        """
        查询销售
        :param sale_id:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/query-sale')
        data['saleId'] = sale_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        re = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/user/query-sale", data=data)
        query_sale_id = self.tool.query_sale_id_by_user_id(self.buyer.user_id)[0].get('salesman_id')
        assert sale_id == query_sale_id
        return re

    def app_buyer_sale_bind_update(self, sale_id):
        """
        更新销售ID
        :param sale_id:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/sale-bind-update')
        data['saleId'] = sale_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        re = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/user/sale-bind-update", data=data)
        query_sale_id = self.tool.query_sale_id_by_user_id(self.buyer.user_id)[0].get('salesman_id')
        assert sale_id == query_sale_id
        return re

    def app_buyer_user_detail(self):
        """
        查询用户的detail
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/detail')
        if data is None:
            data = {}
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        user_detail = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/user/detail", data=data)
        user_detail_content = eval(user_detail).get('content')
        query_user_detail = self.tool.query_user_detail_by_user_id(self.buyer.user_id)[0]
        assert user_detail_content.get('realName') == query_user_detail.get('real_name')
        return user_detail

    def app_buyer_resource_add(self, farm_id, order_no):
        """
        上传购买资质
        :param farm_id:
        :param order_no:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer-resource/add')
        data['farmId'] = farm_id
        data['orderNo'] = order_no
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer-resource/add", data=data)
        return r

    def app_buyer_resource_detail(self, order_no):
        """
        订单的购买资质详情
        :param order_no:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer-resource/detail')
        data['orderNo'] = order_no
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer-resource/detail", data=data)
        return r

    def app_buyer_resource_is_add(self, order_no):
        """
        判断订单是否可以上传购买资质
        :param order_no:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer-resource/is-add')
        data['orderNo'] = order_no
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer-resource/is-add", data=data)
        return r

    def app_buyer_resource_list(self, order_no, status, buyer_name):
        """
        购买资质列表
        :param order_no:
        :param status:
        :param buyer_name:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer-resource/resource-list')
        data['orderNo'] = order_no
        data['status'] = status
        data['buyerName'] = buyer_name
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer-resource/resource-list", data=data)
        return r

    def app_buyer_farm_recommend_list(self, farm_id):
        """
        农场相关推荐
        :param farm_id:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/farm/recommend-list')
        data['farmId'] = farm_id
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/farm/recommend-list", data=data)
        return r

    def app_buyer_subscribe_add(self, city_ids=None, farm_type=None, min_price=None, max_price=None,
                                min_area=None, max_area=None):
        """
        添加订阅规则
        :param city_ids:
        :param farm_type:
        :param min_price:
        :param max_price:
        :param min_area:
        :param max_area:
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/subscribe/add')
        data['cityIds'] = city_ids
        data['farmType'] = farm_type
        data['minPrice'] = min_price
        data['maxPrice'] = max_price
        data['minArea'] = min_area
        data['maxArea'] = max_area
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        response = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/subscribe/add", data=data)
        response = json.loads(response)
        query_subscribe_role = self.tool.query_subscribe_role_by_user_id(self.buyer.user_id)
        if response.get('status') == 'OK':
            if query_subscribe_role == ():
                raise Exception("Error: 添加订阅规则失败")
            else:
                assert query_subscribe_role[0].get('city_ids') == city_ids
                assert query_subscribe_role[0].get('farm_type') == farm_type
                assert query_subscribe_role[0].get('min_price') == min_price
                assert query_subscribe_role[0].get('max_price') == max_price
                assert query_subscribe_role[0].get('min_area') == min_area
                assert query_subscribe_role[0].get('max_area') == max_area
                return response
        elif response.get('status') != 'ERROR':
            assert response.get('errorMsg') == "该用户已经添加过订阅规则"
        else:
            raise Exception("Error: %s" % response["errorMsg"])

    def app_buyer_subscribe_detail(self):
        """
        查看订阅规则
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/subscribe/detail')
        if data is None:
            data = {}
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        response = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/subscribe/detail", data=data)
        response_json = json.loads(response)
        if response_json.get('status') == 'OK':
            response_json_content = response_json.get('content')
            query_subscribe_role = self.tool.query_subscribe_role_by_user_id(self.buyer.user_id)
            assert query_subscribe_role[0].get('city_ids') == response_json_content.get('city_ids')
            assert query_subscribe_role[0].get('farm_type') == response_json_content.get('farm_type')
            assert query_subscribe_role[0].get('min_price') == response_json_content.get('min_price')
            assert query_subscribe_role[0].get('max_price') == response_json_content.get('max_price')
            assert query_subscribe_role[0].get('min_area') == response_json_content.get('min_area')
            assert query_subscribe_role[0].get('max_area') == response_json_content.get('max_area')
            return response_json_content
        else:
            raise Exception("Error: %s" % response_json.get("errorMsg"))

    def app_buyer_subscribe_update(self, city_ids=None, farm_type=None, min_price=None, max_price=None,
                                   min_area=None, max_area=None):
        """
        修改订阅规则
        :param city_ids: 城市的ID的集合,egg:1,2,3
        :param farm_type: 集合:1,2,3
        :param min_price: 最小的价格
        :param max_price: 最大的价格
        :param min_area: 最小的面积
        :param max_area: 最大的面积
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/subscribe/update')
        data['cityIds'] = city_ids
        data['farmType'] = farm_type
        data['minPrice'] = min_price
        data['maxPrice'] = max_price
        data['minArea'] = min_area
        data['maxArea'] = max_area
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        response = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/subscribe/update", data=data)
        response_json = json.loads(response)
        query_subscribe_role = self.tool.query_subscribe_role_by_user_id(self.buyer.user_id)
        if response_json.get('status') == 'OK':
            if query_subscribe_role == ():
                raise Exception("Error: 更新订阅规则失败")
            else:
                assert query_subscribe_role[0].get('city_ids') == city_ids
                assert query_subscribe_role[0].get('farm_type') == farm_type
                assert query_subscribe_role[0].get('min_price') == min_price
                assert query_subscribe_role[0].get('max_price') == max_price
                assert query_subscribe_role[0].get('min_area') == min_area
                assert query_subscribe_role[0].get('max_area') == max_area
                return response_json
        else:
            raise Exception("Error: %s" % response_json["errorMsg"])

    def app_buyer_subscribe_farm_list(self):
        """
        农场订阅列表
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/subscribe/farm-list')
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/subscribe/farm-list", data=data)
        return r

    def app_buyer_order_del(self, order_no_list=None):
        """
        买家删除订单
        :param order_no_list: 使用,分割,eg:1,2,3
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/del')
        data['orderNoList'] = order_no_list
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/order/del", data=data)
        return r

    def app_buyer_order_list(self, type_no=0):
        """
        感兴趣列表
        :param type_no: 0,1;默认填0,1表示查询的list是可以删除的order
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/list')
        data['type'] = type_no
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/order/list", data=data)
        return r

    def app_buyer_update_show_auth(self):
        """
        查询是否显示提示认证信息
        :return:
        """
        data = self.data_trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/update-show-auth')
        if data is None:
            data = {}
        data['_tk_'] = self.buyer.token
        data['_deviceId_'] = self.buyer.device_id
        data['_language_'] = self.buyer.language
        r = Request().post(url="http://dev.trade.worldfarm.com/mobile/buyer/user/update-show-auth", data=data)
        return r
