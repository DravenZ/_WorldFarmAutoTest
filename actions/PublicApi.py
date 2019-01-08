#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json

class worldFarmAction(object):
    def __init__(self, worldFarm):
        self.log = Log('worldFarm')
        self.request = Request()
        self.worldFarm = worldFarm

    # 公共接口-获取所有农场资质字典
    def _config_common_get_all_farm_dict(self):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-all-farm-dict')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://39.104.28.40:9600/config/common/get-all-farm-dict', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    # 公共接口-获取所有banner类型
    def _config_common_get_banner_type(self):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-banner-type')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://39.104.28.40:9600/config/common/get-banner-type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    # 公共接口-农场出售状态
    def _config_common_get_farm_sale_status(self):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-farm-sale-status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://39.104.28.40:9600/config/common/get-farm-sale-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    # 公共接口-农场翻译状态
    def _config_common_get_farm_translate_status(self):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-farm-translate-status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://39.104.28.40:9600/config/common/get-farm-translate-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    # 公共接口-农场审核状态
    def _config_common_get_farm_audit_status(self):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-farm-audit-status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://39.104.28.40:9600/config/common/get-farm-audit-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    # 公共接口-农场是否销售
    def _config_common_get_farm_is_sale(self):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-farm-is-sale')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://39.104.28.40:9600/config/common/get-farm-is-sale', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    # 公共接口-农场修改状态
    def _config_common_get_farm_update_status(self):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-farm-update-status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://39.104.28.40:9600/config/common/get-farm-update-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    # 公共接口-图片上传-图片上传（农场扩展图片如图文混排，返回宽高）
    def _common_farm_upload_ext(self, file):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/common/farm/upload-ext')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['file'] = file
        response = self.request.post(url='http://39.104.28.40:9600/common/farm/upload-ext', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    # 公共接口-图片上传-图片上传(农场主图上传)
    def _common_farm_upload_img(self, file):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/common/farm/upload-img')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['file'] = file
        response = self.request.post(url='http://39.104.28.40:9600/common/farm/upload-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

        # 公共接口-图片上传-图片上传(农场主图上传-网络图片)
        def _common_farm_upload_img_url(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/common/farm/upload-img-url')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/common/farm/upload-img-url', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")


        # 公共接口-图片上传-上传农场资质附件
        def _common_farm_upload_information(self, file):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/common/farm/upload-information')
            data['_tk_'] = None
            data['_deviceId_'] = None
            data['file'] = file
            response = self.request.post(url='http://39.104.28.40:9600/common/farm/upload-information', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-图片上传-图片上传（签证资料、认证、审核资料）
        def _common_user_upload_ext(self, file):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/common/user/upload-ext')
            data['_tk_'] = None
            data['_deviceId_'] = None
            data['file'] = file
            response = self.request.post(url='http://39.104.28.40:9600/common/user/upload-ext', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")


        # 公共接口-图片上传-图片上传（所有用户头像上传）
        def _common_user_upload_head_img(self, file):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/common/user/upload-head-img')
            data['_tk_'] = None
            data['_deviceId_'] = None
            data['file'] = file
            response = self.request.post(url='http://39.104.28.40:9600/common/user/upload-head-img', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-app农场全部字典汇总
        def _config_common_get_app_dict_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-app-dict-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-app-dict-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-面积范围
        def _config_common_get_area_range_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-area-range-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-area-range-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-城市列表(默认澳大利亚下的城市)
        def _config_common_get_city_list(self, pid):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-city-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            data['pid'] = pid
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-city-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-农场类别列表
        def _config_common_get_farm_type_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-farm-type-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-farm-type-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-土地性质列表
        def _config_common_get_land_rights_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-land-rights-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-land-rights-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-买家APP端-排序类型取值列表
        def _config_common_get_mobile_sort_type_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-mobile-sort-type-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-mobile-sort-type-list',
                                         data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-国家列表(暂时只有澳大利亚)
        def _config_common_get_nation_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-nation-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-nation-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-价格范围
        def _config_common_get_price_range_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-price-range-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-price-range-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-土壤ph值列表
        def _config_common_get_soil_ph_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-soil-ph-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-soil-ph-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-土壤类型列表
        def _config_common_get_soil_type_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-soil-type-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-soil-type-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")

        # 公共接口-公共接口-字典配置-排序列表列表
        def _config_common_get_sort_type_list(self):
            data = self.worldFarm.get('http://39.104.28.40:9600').get('/config/common/get-sort-type-list')
            data['_tk_'] = None
            data['_deviceId_'] = None
            response = self.request.post(url='http://39.104.28.40:9600/config/common/get-sort-type-list', data=data)
            json_response = json.loads(response)
            if json_response["status"] == "OK":
                pass
            elif json_response["status"] == "ERROR":
                pass
            else:
                raise Exception("status未返回OK或ERROR")