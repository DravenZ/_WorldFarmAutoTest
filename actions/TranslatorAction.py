#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/9/14'
"""

from utils.Config import Config
from utils.Util import Request
from utils.Util import DataBaseOperate
from backend.Tool import Tool
from utils.Log import Log
import json
import time


class TranslatorAction(object):

    def __init__(self, translator):
        self.log = Log('TranslatorAction')
        self.translator = translator
        self.data_sso = Config('sso').data
        self.data_trade = Config('trade').data
        self.data_sms = Config('sms').data
        self.data_base = DataBaseOperate()
        self.request = Request()
        self.tool = Tool()

    def translator_query_translate_list(self, farm_type=None, key_word=None):
        """
        已发布农场-待翻译农场列表
        :param farm_type: 详见farm_types字典
        :param key_word: 农场名称或农场地址
        :return: 返回与关键字匹配的已发布待翻译农场里列表
        """
        farm_types = {'休闲': 1, '畜牧': 2, '养殖': 2, '酒庄': 3, '葡萄园': 3, '林木': 4, '狩猎': 4, '综合': 5, '种植': 6}
        search_data = {"search": key_word,
                       "_tk_": self.translator.token,
                       "_deviceId_": self.translator.device_id}
        if farm_type:
            search_data["type"] = farm_types[farm_type]
        else:
            search_data["type"] = ""
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/translate-list',
                                     data=search_data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            to_translate_list = json_response["content"]["datas"]
            farm_id_set = set([farm["id"] for farm in to_translate_list])
            translate_list_data = self.data_base.operate('39.104.28.40', 'farm-trade',
                                                         'SELECT id FROM t_farm WHERE language_type != 3')
            data_base_id = [farm["id"] for farm in translate_list_data]
            assert farm_id_set.issubset(data_base_id)
            return to_translate_list
        else:
            raise Exception("Error: %s" % json_response["errorMsg"])

    def translator_query_translate_farm_detail(self, farm_id):
        """
        已发布农场-待翻译农场详情
        :param farm_id: 已发布待翻译农场id
        :return: 返回对应id农场详情
        """
        response = self.request.get(url='http://dev.trade.worldfarm.com'
                                        '/admin/farm/translate-detail/%s?_tk_=%s&_deviceId_=%s'
                                        % (str(farm_id), self.translator.token, self.translator.device_id))
        json_response = json.loads(response)
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
            assert farm_json["content"].replace('\\', '') == farm_data_base["content"].replace('\\', '')
            return farm_json
        else:
            raise Exception("Error: %s" % json_response["errorMsg"])

    def translator_query_published_farm_detail(self):
        """

        :return:
        """
        data = {"_tk_": self.translator.token, "_deviceId_": self.translator.device_id}
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/published-detail',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        else:
            raise Exception("Error: %s" % json_response["errorMsg"])

    def translator_query_published_farm_list(self):
        """

        :return:
        """
        data = {"_tk_": self.translator.token, "_deviceId_": self.translator.device_id}
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/published-detail',
                                     data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        else:
            raise Exception("Error: %s" % json_response["errorMsg"])


if __name__ == '__main__':
    from backend.Employee import Employee
    translator = Employee(100025, 123456)
    ta = TranslatorAction(translator)
    # ta.translator_query_published_farm_detail()
    ta.translator_query_translate_list()
    # farm_id = ta.translator_query_translate_list()[0]["id"]
    # ta.translator_query_translate_farm_detail(farm_id)

