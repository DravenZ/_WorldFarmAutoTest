#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from utils.Config import Config
from utils.Util import Request
from utils.Log import Log
from utils.Util import DataBaseOperate
import json
class farmerAction(object):
    def __init__(self, worldFarm):
        self.log = Log('farmerLog')
        self.request = Request()
        self.data_base = DataBaseOperate()
        self.worldFarm = worldFarm

    # 农场主-编辑农场
    def _mobile_farm_owner_edit(self, farmId, farmName, area, type, totalPrice, purchaseTimeStr, language = "zh", assertFlag = 1):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/mobile/farm-owner/edit')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['_language_'] = language
        data['farmId'] = farmId
        data['farmName'] = farmName
        data['area'] = area
        data['type'] = type
        data['totalPrice'] = totalPrice
        data['purchaseTimeStr'] = purchaseTimeStr
        data['language'] = language
        response = self.request.post(url='http://39.104.28.40:9600/mobile/farm-owner/edit', data=data)
        json_response = json.loads(response)
        dataStore = self.DataBaseOperate().operate('39.104.28.40', 'farm-trade',
                                                   'select * from t_farm where farm_name = %s order by id desc limit 1;' % farmName)

        if 1 == assertFlag:
            #  修改成功断言
            assert json_response["status"] == "OK"
            assert json_response["content"] == "true" or "True"
            assert json_response["errorMsg"] is not None

            # 落地数据断言
            assert data["area"] == dataStore[0]["area"]
            assert data["farmName"] == dataStore[0]["farm_name"]
            assert data["type"] == dataStore[0]["type"]
            assert data["totalPrice"] == dataStore[0]["total_price"]
            assert data["purchaseTimeStr"] == dataStore[0]["purchase_time"]
            assert data["language"] == dataStore[0]["language_type"]
            return dataStore[0]["farm_no"]

        elif 2 == assertFlag:
            # 修改失败断言
            assert json_response["status"] == "ERROR"
            assert json_response["content"] == "false" or "False"
            assert json_response["errorMsg"] is not None
            assert len(dataStore) == 0

    # 农场主 - 农场列表
    def _mobile_farm_owner_list(self, pn, ps, assertFlag = 1, language = "zh"):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/mobile/farm-owner/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['_language_'] = language
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://39.104.28.40:9600/mobile/farm-owner/list', data=data)
        json_response = json.loads(response)
        dataStore = self.DataBaseOperate().operate('39.104.28.40', 'farm-trade',
                                                             'SELECT * FROM t_farm ORDER BY id DESC limit %d,%d;' % (pn, ps))
        if 1 == assertFlag:
        #  查询-成功断言
            assert json_response["status"] == "OK"
            assert json_response["errorMsg"] is not None
            assert len(dataStore) == len(json_response["content"]["datas"])
            for tmp in json_response["content"]["datas"]:
                tmpx = 0
                assert tmp["address"] == dataStore[tmpx]["address"]
                assert tmp["area"] == dataStore[tmpx]["area"]
                assert tmp["areaUnit"] == dataStore[tmpx]["area_code"]
                assert tmp["farmName"] == dataStore[tmpx]["farm_name"]
                assert tmp["type"] == dataStore[tmpx]["type"]
                assert tmp["purchaseTime"] == dataStore[tmpx]["purchase_time"]
                assert tmp["totalPrice"] == dataStore[tmpx]["total_price"]
                tmpx += 1

        elif 2 == assertFlag:
        # 查询失败断言
            assert json_response["status"] == "ERROR"
            # assert json_response["content"] == "false" or "False"
            assert json_response["errorMsg"] is not None
            assert len(dataStore) == 0


    # 农场主 - 农场详情
    def _mobile_farm_owner_detail(self, farmId, assertFlag = 1):
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/mobile/farm-owner/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://39.104.28.40:9600/mobile/farm-owner/detail', data=data)
        json_response = json.loads(response)
        dataStore = self.DataBaseOperate().operate('39.104.28.40', 'farm-trade',
                                                             'select * from t_farm where farm_no = %s order by id desc limit 1' % farmId)
        # dataStore = [farm["id"] for farm in translate_list_data]

        if 1 == assertFlag:
        #  查询成功断言
            assert json_response["status"] == "OK"
            assert json_response["errorMsg"] is not None
            assert len(dataStore) == 1
        #   出参数据断言
            assert json_response["content"]["address"] == dataStore[0]["address"]
            assert json_response["content"]["area"] == dataStore[0]["area"]
            assert json_response["content"]["areaUnit"] == dataStore[0]["area_code"]
            assert json_response["content"]["farmName"] == dataStore[0]["farm_name"]
            assert json_response["content"]["type"] == dataStore[0]["type"]
            assert json_response["content"]["purchaseTime"] == dataStore[0]["purchase_time"]
            assert json_response["content"]["totalPrice"] == dataStore[0]["total_price"]

        elif 2 == assertFlag:
        # 查询失败断言
            assert json_response["status"] == "ERROR"
            # assert json_response["content"] == "false" or "False"
            assert json_response["errorMsg"] is not None
            assert len(dataStore) == 0

    # 农场主 - 添加农场
    def _mobile_farm_owner_add_farm(self, nationId, provinceId, cityId, country, lng, lat, address, images, propertyRightBoundaryList, government, governmentManager, workers, farmName, area, type, totalPrice, purchaseTimeStr, assertFlag = 1, language = "zh"):
        '''
        :param nationId: 国家
        :param provinceId: 省
        :param cityId: 市
        :param country: 区县
        :param lng: 经度
        :param lat: 维度
        :param address: 详细地址
        :param images: 这期不做注意,农场图片Json字符串 eg:[{"type":"1","url":"wwww.3232.cm"},{"type":"2","url":"wwww.baiduewew.cm"}]
        :param propertyRightBoundaryList: 这期不做注意，产权边界（多个以,隔开 最多10个）
        :param government: 这期不做注意，市政府
        :param governmentManager: 这期不做注意，市政府管理员
        :param workers: 这期不做注意，常用工作人员Json 字符串
        :param farmName: 农场名称
        :param area: 面积
        :param type: 农场类型(1:休闲,2:畜牧/养殖,3:酒庄/葡萄园,4:林木/狩猎,5:综合,6:种植)
        :param totalPrice: 购买价
        :param purchaseTimeStr: 购买时间 yyyy-MM-dd
        :param language: 语言
        :param assertFlag: 断言结果1：成功逻辑，其他失败逻辑
        :return:
        '''
        data = self.worldFarm.get('http://39.104.28.40:9600').get('/mobile/farm-owner/add-farm')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['_language_'] = language
        data['nationId'] = nationId
        data['provinceId'] = provinceId
        data['cityId'] = cityId
        data['country'] = country
        data['lng'] = lng
        data['lat'] = lat
        data['address'] = address
        data['images'] = images
        data['propertyRightBoundaryList'] = propertyRightBoundaryList
        data['government'] = government
        data['governmentManager'] = governmentManager
        data['workers'] = workers
        data['farmName'] = farmName
        data['area'] = area
        data['type'] = type
        data['totalPrice'] = totalPrice
        data['purchaseTimeStr'] = purchaseTimeStr
        data['language'] = language
        response = self.request.post(url='http://39.104.28.40:9600/mobile/farm-owner/add-farm', data=data)
        json_response = json.loads(response)
        dataStore = self.DataBaseOperate().operate('39.104.28.40', 'farm-trade',
                                                             'select * from t_farm where farm_name = %s order by id desc limit 1;' % farmName)
        # dataStore = [farm["id"] for farm in translate_list_data]

        if 1 == assertFlag:
        #  添加成功断言
            assert json_response["status"] == "OK"
            assert json_response["content"] == "true" or "True"
            assert json_response["errorMsg"] is not None
            assert len(dataStore) == 1
        # 落地数据断言
            assert data["address"] == dataStore[0]["address"]
            assert data["area"] == dataStore[0]["area"]
            assert data["farmName"] == dataStore[0]["farm_name"]
            assert data["type"] == dataStore[0]["type"]
            assert data["totalPrice"] == dataStore[0]["total_price"]
            assert data["nationId"] == dataStore[0]["nation_id"]
            assert data["provinceId"] == dataStore[0]["province_id"]
            assert data["cityId"] == dataStore[0]["city_id"]
            assert data["country"] == dataStore[0]["country"]
            assert data["purchaseTimeStr"] == dataStore[0]["purchase_time"]
            assert data["language"] == dataStore[0]["language_type"]
            return dataStore[0]["farm_no"]

        elif 2 == assertFlag:
        # 添加失败断言
            assert json_response["status"] == "ERROR"
            assert json_response["content"] == "false" or "False"
            assert json_response["errorMsg"] is not None
            assert len(dataStore) == 0

