#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/9/11'
"""

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json
import time


class PromoterAction(object):

    def __init__(self, promoter):
        self.log = Log('PromoterAction')
        self.promoter = promoter
        self.data_sso = Config('sso').data
        self.data_trade = Config('trade').data
        self.data_sms = Config('sms').data
        self.request = Request()
        self.tool = Tool()
        self.ps = 10

    def promoter_bind_seller_agent(self, seller_agent_id):
        bind_data = {'sellerAgencyId': str(seller_agent_id),
                     "_tk_": self.promoter.token,
                     "_deviceId_": self.promoter.device_id}
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/intermediary/bind',
                                     data=bind_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            json_response["errorMsg"] == "卖家中介已被其他用户绑定"
        else:
            raise Exception("status未返回OK或ERROR")

    def promoter_get_agent_detail(self, seller_agent_id):
        agent_data = {'sellerAgencyId': str(seller_agent_id),
                      "_tk_": self.promoter.token,
                      "_deviceId_": self.promoter.device_id}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/intermediary/detail',
                          data=agent_data)

    def promoter_get_own_detail(self):
        agent_data = {"_tk_": self.promoter.token,
                      "_deviceId_": self.promoter.device_id}
        detail = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/detail',
                                   data=agent_data)
        json_detail = json.loads(detail)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        birthday = json_detail["content"]["birthday"]/1000
        birthday_string = time.strftime("%Y-%m-%d", time.localtime(birthday))
        assert employee_info["birthday"] == birthday_string
        assert employee_info["head_img"] == json_detail["content"]["headImg"]
        assert employee_info["mobile"] == json_detail["content"]["mobile"]
        assert employee_info["mobile_region"] == json_detail["content"]["mobileRegion"]
        assert employee_info["real_name"] == json_detail["content"]["realName"]

    def promoter_update_birthday(self, birthday):
        birthday_data = {"_tk_": self.promoter.token,
                         "_deviceId_": self.promoter.device_id,
                         "birthday": birthday}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-birthday',
                          data=birthday_data)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        assert employee_info['birthday'] == birthday

    def promoter_update_head_img(self,
                                 head_img='http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                          '/data/farm/head/1530012246905.png'):
        img_data = {"_tk_": self.promoter.token,
                    "_deviceId_": self.promoter.device_id,
                    "headImg": head_img}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-head-img',
                          data=img_data)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        assert employee_info['head_img'] == head_img

    def promoter_update_mobile(self, mobile, mobile_region=86):
        mobile_data = {"_tk_": self.promoter.token,
                       "_deviceId_": self.promoter.device_id,
                       "mobileRegion": str(mobile_region),
                       "mobile": str(mobile)}
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-mobile',
                                     data=mobile_data)
        json_response = json.loads(response)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        if json_response["status"] == "OK":
            assert employee_info['mobile_region'] == str(mobile_region)
            assert employee_info['mobile'] == str(mobile)
        elif json_response["status"] == "ERROR":
            assert json_response["errorMsg"] == "该手机号已存在"
        else:
            raise Exception("status未返回OK或ERROR")

    def promoter_update_real_name(self, real_name):
        real_name_data = {"_tk_": self.promoter.token,
                          "_deviceId_": self.promoter.device_id,
                          "realName": real_name}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-real-name',
                          data=real_name_data)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        assert employee_info['real_name'] == str(real_name)

    def promoter_update_sex(self, sex):
        gender = {"男": 1, "女": 2}
        real_name_data = {"_tk_": self.promoter.token,
                          "_deviceId_": self.promoter.device_id,
                          "sex": gender[sex]}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-sex',
                          data=real_name_data)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        assert employee_info['sex'] == gender[sex]

    def promoter_update_signature(self, signature='这家伙很懒什么都没留下'):
        signature_data = {"_tk_": self.promoter.token,
                          "_deviceId_": self.promoter.device_id,
                          "signature": signature}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-signature',
                          data=signature_data)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        assert employee_info['signature'] == signature

    def promoter_add_visa(self, visa_time, expiry_time, visa_img_url):
        visa_data = {"_tk_": self.promoter.token,
                     "_deviceId_": self.promoter.device_id,
                     "visaTime": visa_time,
                     "expiryTime": expiry_time,
                     "visaImgUrl": visa_img_url}
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/visa/add',
                                     data=visa_data)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            assert employee_info['visa_time'] == visa_time
            assert employee_info['expiry_time'] == expiry_time
            assert employee_info['url'] == visa_img_url
        elif json_response["status"] == "ERROR":
            assert json_response['errorMsg'] == "用户已添加签证信息，不能重复添加"
        else:
            raise Exception("status未返回OK或ERROR")

    def promoter_visa_detail(self):
        visa_data = {"_tk_": self.promoter.token,
                     "_deviceId_": self.promoter.device_id}
        visa_detail = self.request.post(url='http://dev.trade.worldfarm.com/mobile/visa/detail',
                                        data=visa_data)
        json_detail = json.loads(visa_detail)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        visa_time_unix = json_detail['content']['visaTime'] / 1000
        expiry_time_unix = json_detail['content']['expiryTime'] / 1000
        visa_time = time.strftime("%Y-%m-%d", time.localtime(visa_time_unix))
        expiry_time = time.strftime("%Y-%m-%d", time.localtime(expiry_time_unix))
        assert employee_info['visa_time'] == visa_time
        assert employee_info['expiry_time'] == expiry_time
        assert employee_info['url'] == json_detail['content']['visaImgUrl']

    def promoter_update_visa(self, visa_time, expiry_time, visa_img_url):
        visa_data = {"_tk_": self.promoter.token,
                     "_deviceId_": self.promoter.device_id,
                     "visaTime": visa_time,
                     "expiryTime": expiry_time,
                     "visaImgUrl": visa_img_url}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/visa/update',
                          data=visa_data)
        employee_info = self.tool.query_employee_info_by_account(self.promoter.account)[0]
        assert employee_info['visa_time'] == visa_time
        assert employee_info['expiry_time'] == expiry_time
        assert employee_info['url'] == visa_img_url

    def promoter_query_agent_farm(self, seller_agent_id, name_like=''):
        query_data = {"_tk_": self.promoter.token,
                      "_deviceId_": self.promoter.device_id,
                      "sellerAgencyId": str(seller_agent_id),
                      "nameLike": name_like}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/im/send-farm/list',
                          data=query_data)

    def promoter_add_potential_agent_remark(self, seller_agent_id, remark):
        remark_data = {"_tk_": self.promoter.token,
                       "_deviceId_": self.promoter.device_id,
                       "sellerId": str(seller_agent_id),
                       "remark": remark}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/potential-agency/add-remark',
                          data=remark_data)

    def promoter_bind_potential_agent(self, potential_agent_id):
        potential_agent_data = {"_tk_": self.promoter.token,
                                "_deviceId_": self.promoter.device_id,
                                "agencyId": str(potential_agent_id)}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/potential-agency/bind',
                          data=potential_agent_data)

    def promoter_query_potential_agent_detail(self, potential_agent_id):
        potential_agent_data = {"_tk_": self.promoter.token,
                                "_deviceId_": self.promoter.device_id,
                                "sellerId": str(potential_agent_id)}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/potential-agency/detail',
                          data=potential_agent_data)

    def promoter_query_potential_agent_list(self, sort_code=2, sort_type='desc', lng='', lat='', pn=1, ps=20):
        query_data = {"_tk_": self.promoter.token,
                      "_deviceId_": self.promoter.device_id,
                      "sortCode": sort_code,
                      "sortType": sort_type,
                      "lat": lat,
                      "lng": lng,
                      "pn": pn,
                      "ps": ps}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/potential-agency/list',
                          data=query_data)

    def promoter_query_farm_dynamic_list(self, lng=133.8713537, lat=-23.6993532, pn=1, ps=20):
        query_data = {"_tk_": self.promoter.token,
                      "_deviceId_": self.promoter.device_id,
                      "lat": lat,
                      "lng": lng,
                      "pn": pn,
                      "ps": ps}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/dynamic/list',
                          data=query_data)

    def promoter_bind_agent_list(self, sort_code=1):
        sort_data = {"_tk_": self.promoter.token,
                     "_deviceId_": self.promoter.device_id,
                     "sortCode": sort_code}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/bind/list',
                          data=sort_data)

    def promoter_bind_agent_detail(self, seller_agent_id, lng=133.8713537, lat=-23.6993532):
        query_data = {"_tk_": self.promoter.token,
                      "_deviceId_": self.promoter.device_id,
                      "lat": lat,
                      "lng": lng,
                      "sellerAgencyId": seller_agent_id}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/bind/detail',
                          data=query_data)

    def promoter_bind_agent_update_remark(self, seller_agent_id, remark):
        remark_data = {"_tk_": self.promoter.token,
                       "_deviceId_": self.promoter.device_id,
                       "remark": remark,
                       "sellAgencyId": seller_agent_id}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/bind/update-remark',
                          data=remark_data)

    def promoter_query_farm_detail(self, farm_id, pn=1, ps=20):
        farm_data = {"_tk_": self.promoter.token,
                     "_deviceId_": self.promoter.device_id,
                     "farmId": farm_id,
                     "pn": pn,
                     "ps": ps}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/detail',
                          data=farm_data)

    def promoter_query_buyer_list(self, farm_id, seller_agent_id, pn=1, ps=20):
        farm_data = {"_tk_": self.promoter.token,
                     "_deviceId_": self.promoter.device_id,
                     "farmId": farm_id,
                     "sellerAgencyId": seller_agent_id,
                     "pn": pn,
                     "ps": ps}
        self.request.post(url='http://dev.trade.worldfarm.com/mobile/order/promotion/buyer-list',
                          data=farm_data)


# if __name__ == '__main__':
#     from backend.Employee import Employee
#     employee = Employee('100028', '123456')
#     pa = PromoterAction(employee)
#     pa.promoter_query_buyer_list(532, 499)
#     pa.promoter_query_farm_detail(532)
#     pa.promoter_bind_agent_update_remark(499, '备注')
#     pa.promoter_bind_agent_list()
#     pa.promoter_bind_agent_detail('499')
#     pa.promoter_query_farm_dynamic_list()
#     pa.promoter_query_potential_agent_list()
#     pa.promoter_query_potential_agent_detail(12)
#     pa.promoter_add_potential_agent_remark(12, '同行备注')
#     pa.promoter_bind_potential_agent(13)
#     pa.promoter_query_agent_farm(499)
#     pa.promoter_visa_detail()
#     pa.promoter_bind_seller_agent(419)
#     pa.promoter_get_own_detail()
#     pa.promoter_get_agent_detail(499)
#     pa.promoter_update_birthday('1983-11-10')
#     pa.promoter_update_head_img()
#     pa.promoter_update_mobile(18628322912, 86)
#     pa.promoter_update_real_name("修改名字1")
#     pa.promoter_update_sex("男")
#     pa.promoter_update_signature()
#     pa.promoter_add_visa('2018-09-11', '2018-11-11',
#                          'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530013225249.jpg')
#     pa.promoter_update_visa('2018-10-11', '2018-11-11',
#                             'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530013225249.jpg')

