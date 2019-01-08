#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Bai Ying'
__date__ = '2018/9/11'
"""

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
from backend.User import User
from backend.Farm import Farm
from backend.Farmer import Farmer
import json


class SellerAgent(object):
    def __init__(self, seller_agent):
        self.log = Log('sellerAgent')
        self.sellerAgent = seller_agent
        self.data_sso = Config('sso').data
        self.data_trade = Config('trade').data
        self.data_sms = Config('sms').data
        self.request = Request()
        self.tool = Tool()
        self.ps = 10

    def mobile_approve_seller_agent(self, real_name, company_name):
        approve_info = self.tool.query_approve_status(self.sellerAgent.mobile)
        if approve_info:
            if approve_info[0]['status'] == 2:
                approve_data = self.data_trade['http://dev.trade.worldfarm.com']['/mobile/seller-agency/user/add']
                approve_data["realName"] = real_name
                approve_data["companyName"] = company_name
                # approve_data["resource"] = resource
                approve_data["_tk_"] = self.sellerAgent.token
                approve_data["_deviceId_"] = self.sellerAgent.device_id
                self.request.post(url="http://dev.trade.worldfarm.com/mobile/seller-agency/user/add",
                                  data=approve_data)
                self.log.logger.debug("中介姓名 更新为 %s" % real_name)
                self.log.logger.debug("中介公司 更新为 %s" % company_name)
                # self.log.logger.debug("中介资料 更新为 %s" % resource)
            else:
                raise Exception('手机号 %s 的用户, 认证状态为 %s, 1为待审核, 3为审核通过'
                                % (str(self.sellerAgent.mobile), str(approve_info[0]['status'])))
        else:
            approve_data = self.data_trade['http://dev.trade.worldfarm.com']['/mobile/seller-agency/user/add']
            approve_data["realName"] = real_name
            approve_data["companyName"] = company_name
            # approve_data["resource"] = resource
            approve_data["_tk_"] = self.sellerAgent.token
            approve_data["_deviceId_"] = self.sellerAgent.device_id
            self.request.post(url="http://dev.trade.worldfarm.com/mobile/seller-agency/user/add",
                              data=approve_data)
            self.log.logger.debug("中介姓名 更新为 %s" % real_name)
            self.log.logger.debug("中介公司 更新为 %s" % company_name)
            # self.log.logger.debug("中介资料 更新为 %s" % resource)

    def mobile_seller_agent_add_farm(self, farm_name, farm_type, farm_state, price_range, are_range, language):
        data = self.data_trade['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/add-farm']
        fm = Farm(farm_name=farm_name, farm_type=farm_type, state_name=farm_state,
                  price_range=price_range, area_range=are_range)
        fmr = Farmer()
        data['farmName'] = fm.farm_name
        data['provinceId'] = fm.province_id
        data['cityId'] = fm.city_id
        data['area'] = fm.area
        data['totalPrice'] = fm.total_price
        data['images'] = fm.images
        data['type'] = fm.farm_type
        data['address'] = fm.farm_address
        data['lat'] = fm.lat
        data['lng'] = fm.lng
        data['content'] = fm.content
        data['headImg'] = fmr.head_img
        data['realName'] = fmr.real_name
        data['birthday'] = fmr.birthday
        data['mobile'] = fmr.mobile
        data['farmerAddress'] = fmr.farmer_address
        data['sex'] = fmr.sex
        data['ownedFarmerNum'] = fmr.owned_farmer_num
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['_language_'] = language
        user_id = self.tool.query_user_id_by_mobile(self.sellerAgent.mobile)
        farmId = Request().post(url="http://dev.trade.worldfarm.com/mobile/seller-agency/farm/add-farm",
                       data=data)
        add_farm = json.loads(farmId)['content']
        farm_info = self.tool.query_latest_farm_info(user_id)
        # self.assertEqual(farm_info["address_en"], data['address'])
        # self.assertEqual(farm_info["area"], data['area'])
        # self.assertEqual(farm_info["farm_name_en"], data['farmName'])
        # self.assertEqual(farm_info["lat"], data['lat'])
        # self.assertEqual(farm_info["lng"], data['lng'])
        # self.assertEqual(farm_info["status"], 20)
        # self.assertEqual(farm_info["total_price"], data['totalPrice'])
        # self.assertEqual(farm_info["type"], data['type'])
        return add_farm


    def mobile_seller_agent_search_farm(self, keyWords, language):
        # 模糊搜索农场列表
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/farm/search']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['keyWords'] = keyWords
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/farm/search', data=data)
        r_content = json.loads(r)['content']
        query_search_farm_list = self.tool.query_farm_list_by_keywords(keyWords)[0]
        assert r_content[0] == query_search_farm_list

    def mobile_seller_agency_add_remark(self, farmId, remark, language):
        # 卖家中介新增备注
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/add-remark']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['farmId'] = farmId
        data['remark'] = remark
        add = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/add-remark', data=data)
        add_remark = json.loads(add)
        # query_add_remark = self.tool.query_remark_by_farm_id(farmId)
        assert add_remark['status'] == 'OK'

    def mobile_seller_agency_close_farm(self, farmId, type, language):
        # 卖家中介关闭农场
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/close']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['farmId'] = farmId
        data['type'] = type #30已售出50暂不销售
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/close', data=data)
        r_close = json.loads(r)
        query_close_farm = self.tool.query_close_farm_by_farm_id(self.sellerAgent.user_id)
        if r_close == {'errorCode': '00030003', 'errorMsg': '农场已售出或者已关闭', 'status': 'ERROR'}:
            assert r_close['errorMsg'] == str('农场已售出或者已关闭')
            assert r_close['status'] == 'ERROR'
        else:
            assert r_close.get['farm_id'] == query_close_farm['id']
            assert r_close['status'] == query_close_farm['status']

    def mobile_seller_agency_close_farm_list(self, pn, language):
        # 卖家中介关闭农场列表
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/closed-list']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['pn'] = pn
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/closed-list', data=data)
        r_close = json.loads(r).get('content').get('datas')
        query_close_list = self.tool.query_close_list_by_seller_agency_id(self.sellerAgent.user_id)
        for i in range(len(r_close)):
            assert r_close[i].get('id') == query_close_list[i].get('id')
            assert r_close[i].get('imgUrl') == query_close_list[i].get('img_url')
            assert r_close[i].get('askNum') == query_close_list[i].get('ask_num')

    def mobile_seller_agency_farm_detail(self, lng, lat, farmId, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/detail']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['lng'] = lng
        data['lat'] = lat
        data['farmId'] = farmId
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/detail', data=data)
        query_farm_detail = self.tool.query_farm_detail_by_farm_id(farmId)[0]
        json_detail = json.loads(r_detail)
        assert json_detail['content']['id'] == query_farm_detail['id']
        assert json_detail['content']['farmName'] == query_farm_detail['farm_name']
        assert json_detail['content']['address'] == query_farm_detail['address']
        assert json_detail['content']['nationId'] == query_farm_detail['nation_id']
        # assert json_detail['content']['passBuyerCount'] == query_farm_detail['']
        assert json_detail['content']['soilPh'] == query_farm_detail['soil_ph']

    def mobile_seller_agency_im_send_farm_list(self, nameLike, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/im/send-farm/list']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['nameLike'] = nameLike
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/im/send-farm/list', data=data)
        r_farm_list = json.loads(r).get('content').get('datas')
        query_farm_list = self.tool.query_farm_list_by_seller_agency_id_or_name(nameLike, self.sellerAgent.user_id)
        for i in range(len(r_farm_list)):
            assert r_farm_list[i].get('type') == query_farm_list[i].get('type')
            # assert r_farm_list[i].get('totalPrice') == query_farm_list[i].get('total_price')

    def mobile_seller_agency_farm_list(self, sortCode, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/list']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['sortCode'] = sortCode
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/list', data=data)
        r_farm_list = json.loads(r).get('content').get('datas')
        query_farm_list = self.tool.query_farm_list_by_seller_agency_id(self.sellerAgent.user_id)
        for i in range(len(r_farm_list)):
            assert r_farm_list[i].get('id') == query_farm_list[i].get('id')
            # assert r_farm_list[i].get('farmName') == query_farm_list[i].get('farm_name')
            assert r_farm_list[i].get('askNum') == query_farm_list[i].get('ask_num')

    def mobile_seller_agency_map_list(self, lng, lat, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/map-list']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['lng'] = lng
        data['lat'] = lat
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/map-list', data=data)
        r_farm_list = json.loads(r).get('content').get('datas')
        query_farm_list = self.tool.query_map_list_by_seller_agency_id(self.sellerAgent.user_id)
        for i in range(len(r_farm_list)):
            assert r_farm_list[i].get('id') == query_farm_list[i].get('id')
            # assert r_farm_list[i].get('farmName') == query_farm_list[i].get('farm_name')
            assert r_farm_list[i].get('askNum') == query_farm_list[i].get('ask_num')

    # def seller_agency_update_farm(self, nationId, provinceId, cityId, farmName, type, area, totalPrice,
    #                               lng, lat, address, images, content, farmId, language):
    #     data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farm/update-farm']
    #     data['language'] = language
    #     data['_tk_'] = self.sellerAgent.token
    #     data['_deviceId_'] = self.sellerAgent.device_id
    #     data['nationId'] = nationId
    #     data['provinceId'] = provinceId
    #     data['cityId'] = cityId
    #     data['farmName'] = farmName
    #     data['totalPrice'] = totalPrice
    #     data['address'] = address
    #     data['content'] = content
    #     data['area'] = area
    #     data['farmId'] = farmId
    #     data['type'] = type
    #     data['lng'] = lng
    #     data['lat'] = lat
    #     data['images'] = images
    #     r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/update-farm', data=data)
    #     r_update_farm = json.loads(r)
    #     assert r_update_farm['status'] == 'OK'

    def mobile_seller_agency_update_farm(self, farm_id, update_data, language):
        data = {
            "_tk_": self.sellerAgent.token,
            "_deviceId_": self.sellerAgent.device_id,
            "farmId": farm_id
        }
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/detail', data=data)
        r_farm_detail = json.loads(r).get('content')
        for k, v in update_data.items():
            r_farm_detail[k] = v
        r_farm_detail['_tk_'] = self.sellerAgent.token
        r_farm_detail['_deviceId_'] = self.sellerAgent.device_id
        r_farm_detail['language'] = language
        r_farm_detail['farmId'] = farm_id
        R = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/update-farm',
                           data=r_farm_detail)
        r_update_farm = json.loads(R)
        assert r_update_farm['status'] == 'OK'

    def mobile_seller_agency_farmer_detail(self, farmId, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farmer/detail']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['farmId'] = farmId
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farmer/detail', data=data)
        query_farm_detail = self.tool.query_farmer_detail_by_farm_id(farmId)[0]
        json_detail = json.loads(r_detail)
        assert json_detail['content']['realName'] == query_farm_detail['real_name']
        # assert json_detail['content']['farmId'] == query_farm_detail['farm_id']
        # assert json_detail['content']['address'] == query_farm_detail['address']
        # assert json_detail['content']['nationId'] == query_farm_detail['nation_id']
        # # assert json_detail['content']['passBuyerCount'] == query_farm_detail['']
        # assert json_detail['content']['soilPh'] == query_farm_detail['soil_ph']

    def mobile_seller_agency_farmer_update(self, farmId, realName, sex, birthday, mobile, headImg, farmerAddress,
                                    ownedFarmerNum, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/farmer/update']
        data['language'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['realName'] = realName
        data['sex'] = sex
        data['birthday'] = birthday
        data['mobile'] = mobile
        data['headImg'] = headImg
        data['farmerAddress'] = farmerAddress
        data['ownedFarmerNum'] = ownedFarmerNum
        data['farmId'] = farmId
        r = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farmer/update', data=data)
        r_update_farm = json.loads(r)
        assert r_update_farm['status'] == 'OK'

    def mobile_seller_agency_use_add(self, realName, companyName, resource, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/user/add']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['realName'] = realName
        data['companyName'] = companyName
        data['resource'] = resource
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/user/add', data=data)
        json_detail = json.loads(r_detail)
        assert json_detail['status'] == 'OK'
        print(r_detail)

    def mobile_seller_agency_use_status(self, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/seller-agency/user/status']
        if data is None:
            data = {}
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/user/status', data=data)
        query_seller_agent_detail = self.tool.query_user_status_by_seller_agency_id(self.sellerAgent.user_id)[0]
        json_detail = json.loads(r_detail)
        assert json_detail['status'] == 'OK'
        assert json_detail['content'] == query_seller_agent_detail['status']

    def mobile_seller_agency_farm_buyer_list(self, farmId, type, pn, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/order/seller-agency/farm/buyer-list']
        # if data is None:
        #     data = {}
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['farmId'] = farmId
        data['type'] = type
        data['pn'] = pn
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/mobile/order/seller-agency/farm/buyer-list',
                                  data=data)
        r_buyer_list = json.loads(r_detail).get('content').get('datas')
        query_user_list = self.tool.query_buyer_list_by_farm_id(farmId)
        for i in range(len(query_user_list)):
            assert r_buyer_list[i].get('buyerId') == query_user_list[i].get('buyer_id')

    def mobile_seller_agency_message_buyer_list(self, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/mobile/order/seller-agency/message/buyer-list']
        # if data is None:
        #     data = {}
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/mobile/order/seller-agency/message/buyer-list',
                                  data=data)
        r_message_buyer_list = json.loads(r_detail).get('content').get('datas')
        query_user_list = self.tool.query_message_buyer_list_by_farm_id(self.sellerAgent.user_id)
        for i in range(len(r_message_buyer_list)):
            assert r_message_buyer_list[i].get('farmId') == query_user_list[i].get('farm_id')

    def web_seller_agent_add_farm(self, farm_name, farm_type, farm_state, price_range, are_range, language):
        data = self.data_trade['http://dev.trade.worldfarm.com']['/web/seller-agency/farm/add-farm']
        fm = Farm(farm_name=farm_name, farm_type=farm_type, state_name=farm_state,
                  price_range=price_range, area_range=are_range)
        fmr = Farmer()
        data['farmName'] = fm.farm_name
        data['provinceId'] = fm.province_id
        data['cityId'] = fm.city_id
        data['area'] = fm.area
        data['totalPrice'] = fm.total_price
        data['images'] = fm.images
        data['type'] = fm.farm_type
        data['address'] = fm.farm_address
        data['lat'] = fm.lat
        data['lng'] = fm.lng
        data['content'] = fm.content
        data['headImg'] = fmr.head_img
        data['realName'] = fmr.real_name
        data['birthday'] = fmr.birthday
        data['mobile'] = fmr.mobile
        data['farmerAddress'] = fmr.farmer_address
        data['sex'] = fmr.sex
        data['ownedFarmerNum'] = fmr.owned_farmer_num
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['_language_'] = language
        user_id = self.tool.query_user_id_by_mobile(self.sellerAgent.mobile)
        farmId = Request().post(url="http://dev.trade.worldfarm.com/web/seller-agency/farm/add-farm",
                       data=data)
        add_farm = json.loads(farmId)['content']
        farm_info = self.tool.query_latest_farm_info(user_id)
        # self.assertEqual(farm_info["address_en"], data['address'])
        # self.assertEqual(farm_info["area"], data['area'])
        # self.assertEqual(farm_info["farm_name_en"], data['farmName'])
        # self.assertEqual(farm_info["lat"], data['lat'])
        # self.assertEqual(farm_info["lng"], data['lng'])
        # self.assertEqual(farm_info["status"], 20)
        # self.assertEqual(farm_info["total_price"], data['totalPrice'])
        # self.assertEqual(farm_info["type"], data['type'])
        return add_farm

    def web_seller_agency_add_remark(self, farmId, remark, language):
        # 卖家中介新增备注
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/farm/add-remark']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['farmId'] = farmId
        data['remark'] = remark
        add = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/add-remark', data=data)
        add_remark = json.loads(add)
        query_add_remark = self.tool.query_remark_by_farm_id(farmId)
        assert add_remark['status'] == 'OK'
        # assert add_remark['farm_id'] == query_add_remark['id']
        # assert add_remark['remark'] == query_add_remark['remark']

    def web_seller_agency_close_farm(self, farmId, type, language):
        # 卖家中介关闭农场
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/farm/close']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['farmId'] = farmId
        data['type'] = type # 30已售出50暂不销售
        r = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/close', data=data)
        r_close = json.loads(r)
        query_close_farm = self.tool.query_close_farm_by_farm_id(self.sellerAgent.user_id)
        if r_close == {'errorCode': '00030003', 'errorMsg': '农场已售出或者已关闭', 'status': 'ERROR'}:
            assert r_close['errorMsg'] == str('农场已售出或者已关闭')
            assert r_close['status'] == 'ERROR'
        else:
            assert r_close.get['farm_id'] == query_close_farm['id']
            assert r_close['status'] == query_close_farm['status']

    def web_seller_agency_close_farm_list(self, pn, language):
        # 卖家中介关闭农场列表
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/farm/closed-list']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['pn'] = pn
        r = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/closed-list', data=data)
        r_close = json.loads(r).get('content').get('datas')
        query_close_list = self.tool.query_close_list_by_seller_agency_id(self.sellerAgent.user_id)
        for i in range(len(r_close)):
            assert r_close[i].get('id') == query_close_list[i].get('id')
            assert r_close[i].get('imgUrl') == query_close_list[i].get('img_url')
            assert r_close[i].get('askNum') == query_close_list[i].get('ask_num')

    def web_seller_agency_farm_detail(self, lng, lat, farmId, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/farm/detail']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['lng'] = lng
        data['lat'] = lat
        data['farmId'] = farmId
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/detail', data=data)
        query_farm_detail = self.tool.query_farm_detail_by_farm_id(farmId)[0]
        json_detail = json.loads(r_detail)
        assert json_detail['content']['id'] == query_farm_detail['id']
        assert json_detail['content']['farmName'] == query_farm_detail['farm_name']
        assert json_detail['content']['address'] == query_farm_detail['address']
        assert json_detail['content']['nationId'] == query_farm_detail['nation_id']
        # assert json_detail['content']['passBuyerCount'] == query_farm_detail['']
        assert json_detail['content']['soilPh'] == query_farm_detail['soil_ph']

    def web_seller_agency_im_send_farm_list(self, nameLike, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/farm/im/send-farm/list']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['nameLike'] = nameLike
        r = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/im/send-farm/list', data=data)
        r_farm_list = json.loads(r).get('content').get('datas')
        query_farm_list = self.tool.query_farm_list_by_seller_agency_id_or_name(nameLike, self.sellerAgent.user_id)
        for i in range(len(r_farm_list)):
            assert r_farm_list[i].get('type') == query_farm_list[i].get('type')

    def web_seller_agency_farm_list(self, sortCode, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/farm/list']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['sortCode'] = sortCode
        r = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/list', data=data)
        r_farm_list = json.loads(r).get('content').get('datas')
        query_farm_list = self.tool.query_farm_list_by_seller_agency_id(self.sellerAgent.user_id)
        for i in range(len(r_farm_list)):
            assert r_farm_list[i].get('id') == query_farm_list[i].get('id')
            # assert r_farm_list[i].get('farmName') == query_farm_list[i].get('farm_name')
            assert r_farm_list[i].get('askNum') == query_farm_list[i].get('ask_num')

    def web_seller_agency_update_farm(self, farm_id, update_data, language):
        data = {
            "_tk_": self.sellerAgent.token,
            "_deviceId_": self.sellerAgent.device_id,
            "farmId": farm_id
        }
        r = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/detail', data=data)
        r_farm_detail = json.loads(r).get('content')
        for k, v in update_data.items():
            r_farm_detail[k] = v
        r_farm_detail['_tk_'] = self.sellerAgent.token
        r_farm_detail['_deviceId_'] = self.sellerAgent.device_id
        r_farm_detail['language'] = language
        R = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/update-farm',
                           data=r_farm_detail)
        r_update_farm = json.loads(R)
        assert r_update_farm['status'] == 'OK'

    def web_seller_agency_farmer_detail(self, farmId, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/farmer/detail']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['farmId'] = farmId
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farmer/detail', data=data)
        query_farm_detail = self.tool.query_farmer_detail_by_farm_id(farmId)[0]
        json_detail = json.loads(r_detail)
        assert json_detail['content']['realName'] == query_farm_detail['real_name']
        # assert json_detail['content']['farmId'] == query_farm_detail['farm_id']
        # assert json_detail['content']['address'] == query_farm_detail['address']
        # assert json_detail['content']['nationId'] == query_farm_detail['nation_id']
        # # assert json_detail['content']['passBuyerCount'] == query_farm_detail['']
        # assert json_detail['content']['soilPh'] == query_farm_detail['soil_ph']

    def web_seller_agency_farmer_update(self, farmId, update_data, language):
        data = {
            "_tk_": self.sellerAgent.token,
            "_deviceId_": self.sellerAgent.device_id,
            "farmId": farmId
        }
        r = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farmer/detail', data=data)
        r_farmer_detail = json.loads(r).get('content')
        for k, v in update_data.items():
            r_farmer_detail[k] = v
        r_farmer_detail['_tk_'] = self.sellerAgent.token
        r_farmer_detail['_deviceId_'] = self.sellerAgent.device_id
        r_farmer_detail['language'] = language
        R = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/farmer/update',
                           data=r_farmer_detail)
        r_update_farm = json.loads(R)
        assert r_update_farm['status'] == 'OK'

    def web_seller_agency_use_add(self, realName, companyName, resource, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/user/add']
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['realName'] = realName
        data['companyName'] = companyName
        data['resource'] = resource
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/user/add', data=data)
        json_detail = json.loads(r_detail)
        assert json_detail['status'] == 'OK'
        print(r_detail)

    def web_seller_agency_use_status(self, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/seller-agency/user/status']
        if data is None:
            data = {}
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/web/seller-agency/user/status', data=data)
        query_seller_agent_detail = self.tool.query_user_status_by_seller_agency_id(self.sellerAgent.user_id)[0]
        json_detail = json.loads(r_detail)
        assert json_detail['status'] == 'OK'
        assert json_detail['content'] == query_seller_agent_detail['status']

    def web_seller_agency_farm_buyer_list(self, farmId, type, pn, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/order/seller-agency/farm/buyer-list']
        # if data is None:
        #     data = {}
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        data['farmId'] = farmId
        data['type'] = type
        data['pn'] = pn
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/mobile/order/seller-agency/farm/buyer-list',
                                  data=data)
        r_buyer_list = json.loads(r_detail).get('content').get('datas')
        query_user_list = self.tool.query_buyer_list_by_farm_id(farmId)
        for i in range(len(query_user_list)):
            assert r_buyer_list[i].get('buyerId') == query_user_list[i].get('buyer_id')

    def web_seller_agency_message_buyer_list(self, language):
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/web/order/seller-agency/message/buyer-list']
        # if data is None:
        #     data = {}
        data['_language_'] = language
        data['_tk_'] = self.sellerAgent.token
        data['_deviceId_'] = self.sellerAgent.device_id
        r_detail = Request().post(url='http://dev.trade.worldfarm.com/web/order/seller-agency/message/buyer-list',
                                  data=data)
        r_message_buyer_list = json.loads(r_detail).get('content').get('datas')
        query_user_list = self.tool.query_message_buyer_list_by_farm_id(self.sellerAgent.user_id)
        for i in range(len(r_message_buyer_list)):
            assert r_message_buyer_list[i].get('farmId') == query_user_list[i].get('farm_id')






# if __name__ == '__main__':
#     user = User("18602832572", "123456a", register=False)
#     sellerAgent = SellerAgent(user)
    # sellerAgent.seller_agency_farm_list(2, language='zh')
    #
    # sellerAgent.seller_agent_search_farm('漫花', language='zh')
    # sellerAgent.seller_agency_close_farm_list(1, language='zh')
    # sellerAgent.seller_agency_add_remark(516, "lalal", language='zh')
    # sellerAgent.seller_agency_close_farm(521, 30, language='zh')
    # sellerAgent.seller_agency_farm_detail(140.7842627, 37.8301386, 523, language='zh')
    # sellerAgent.web_seller_agent_add_farm("web测试大娃二娃农场名", "种植", "南澳大利亚", "2000万-3500万", "5000亩-10000亩",
    #                                        language='zh')
    # sellerAgent.mobile_seller_agency_update_farm(523, {"area": 12},language='zh')
    # sellerAgent.web_seller_agency_add_remark(516, "web自动化测试lalal", language='zh')

