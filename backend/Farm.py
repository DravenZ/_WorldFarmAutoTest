#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/15'
"""


from backend.Tool import Tool
from utils.Util import Redis
from utils.Log import Log
from faker import Faker


class Farm(object):
    L = Log('Farm')
    fake_en = Faker('en_AU')
    fake = Faker('zh_CN')

    def __init__(self, farm_name="自动化默认农场名", state_name="北部地区", farm_type="综合",
                 area_range="500亩以下", price_range="500万以下"):
        farm_type_dict = {"休闲": 1, "畜牧": 2, "养殖": 2, "种植": 6, "酒庄": 3, "葡萄园": 3,
                          "林木": 4, "狩猎": 4, "综合": 5}
        farm_area_dict = {"500亩以下": self.fake.random_int(1, 82),
                          "500亩-5000亩": self.fake.random_int(83, 823),
                          "5000亩-10000亩": self.fake.random_int(824, 1647),
                          "10000亩-50000亩": self.fake.random_int(1648, 8236),
                          "50000亩以上": self.fake.random_int(8237, 16473)}
        total_price_dict = {"500万以下": self.fake.random_int(1, 980392),
                            "500万-2000万": self.fake.random_int(1020408, 3921568),
                            "2000万-3500万": self.fake.random_int(4081632, 6862745),
                            "3500万-5000万": self.fake.random_int(7142857, 9803921),
                            "5000万以上": self.fake.random_int(10204081, 19607843)}
        city = Tool().query_random_city(state_name)
        self.farm_name = farm_name
        self.farm_name_en = self.fake_en.name() + " Farm"
        self.L.logger.debug("中文农场名 为 %s" % self.farm_name)
        self.L.logger.debug("英文农场名 为 %s" % self.farm_name_en)
        self.farm_type = farm_type_dict[farm_type]
        self.L.logger.debug("农场类型 为 %s %s" % (self.farm_type, farm_type))
        city_name = city[0]
        self.L.logger.debug("农场的州-市 为 %s %s" % (state_name, city_name))
        self.farm_address = city[1]["address"]
        self.L.logger.debug("中文农场地址 为 %s" % self.farm_address)
        self.farm_address_en = city[1]["address"]
        self.L.logger.debug("英文农场地址 为 %s" % self.farm_address_en)
        self.lat = city[1]["lat"]
        self.L.logger.debug("农场维度lat 为 %s" % self.lat)
        self.lng = city[1]["lng"]
        self.L.logger.debug("农场经度lng 为 %s" % self.lng)
        self.nation_id = 25
        self.L.logger.debug("农场的nationId 为 %d" % self.nation_id)
        self.province_id = city[1]["state"]
        self.L.logger.debug("农场的provinceId 为 %d" % self.province_id)
        self.city_id = city[1]["city"]
        self.L.logger.debug("农场的cityId 为 %d" % self.city_id)
        self.area = farm_area_dict[area_range]
        self.L.logger.debug("农场的面积 为 %s 英亩" % str(self.area))
        self.total_price = total_price_dict[price_range]
        self.L.logger.debug("农场的总价 为 %s 澳元" % str(self.total_price))
        self.unitCode = "AUD"
        self.L.logger.debug("农场的货币单位 为 %s" % self.unitCode)
        self.unit_price = self.total_price/self.area
        self.L.logger.debug("农场的单价 为 %s 澳元" % str(self.unit_price))
        self.water_rights = "中文水权描述:" + self.fake.text().replace('\n',' ')
        self.L.logger.debug(self.water_rights)
        self.water_rights_en = "英文水权描述:" + self.fake_en.text().replace('\n',' ')
        self.L.logger.debug(self.water_rights_en)
        self.regulations = "中文土地使用规定:" + self.fake.text().replace('\n',' ')
        self.L.logger.debug(self.regulations)
        self.regulations_en = "英文土地使用规定:" + self.fake_en.text().replace('\n',' ')
        self.L.logger.debug(self.regulations_en)
        self.rainfall = self.fake.random_int(20, 1000)
        self.L.logger.debug("降雨量 %s毫升/年" % self.rainfall)
        self.disadvantage = "中文杂草和虫害:" + self.fake.text().replace('\n',' ')
        self.L.logger.debug(self.disadvantage)
        self.disadvantage_en = "英文杂草和虫害:" + self.fake_en.text().replace('\n',' ')
        self.L.logger.debug(self.disadvantage_en)
        self.area_code = 'mu'
        self.L.logger.debug("中文面积单位: %s" % self.area_code)
        self.area_code_en = 'acre'
        self.L.logger.debug("英文面积单位: %s" % self.area_code_en)
        self.soil_ph = 3 #float(self.fake.random_int(-10, 150)/10)
        self.L.logger.debug("土壤PH值: %s" % self.soil_ph)
        self.soil_type = self.fake.random_int(1, 3)
        redis = Redis()
        self.images = '[{"type":"1", ' \
                      '"url":"' + redis.get("image%s" % str(self.fake.random_int(1, 75))) + '"},' \
                      '{"type":"2", ' \
                      '"url":"' + redis.get("image%s" % str(self.fake.random_int(1, 75))) + '"},' \
                      '{"type":"3", ' \
                      '"url":"' + redis.get("image%s" % str(self.fake.random_int(1, 75))) + '"},' \
                      '{"type":"4", ' \
                      '"url":"' + redis.get("image%s" % str(self.fake.random_int(1, 75))) + '"}]'
        self.L.logger.debug("农场Banner 为 %s " % str(self.images))
        self.content = '[{"type":"1", ' \
                       '"value":"' + redis.get("image%s" % str(self.fake.random_int(1, 75))) + '"},'\
                       '{"type":"2", ' \
                       '"value":"' + self.fake.text().replace("\n", " ") + '"},' \
                       '{"type":"1", ' \
                       '"value":"' + redis.get("image%s" % str(self.fake.random_int(1, 75))) + '"},' \
                       '{"type":"2", ' \
                       '"value":"' + self.fake.text().replace("\n", " ") + '"}]'
        self.L.logger.debug("中文农场介绍 为 %s " % str(self.content))
        self.content_en = '[{"type":"1", ' \
                          '"value":"' + redis.get("image%s" % str(self.fake.random_int(1, 75))) + '"},'\
                          '{"type":"2", ' \
                          '"value":"' + self.fake_en.text().replace("\n", " ") + '"},' \
                          '{"type":"1", ' \
                          '"value":"' + redis.get("image%s" % str(self.fake.random_int(1, 75))) + '"},' \
                          '{"type":"2", ' \
                          '"value":"' + self.fake_en.text().replace("\n", " ") + '"}]'
        self.L.logger.debug("英文农场介绍 为 %s " % str(self.content_en))


if __name__ == '__main__':
    Farm()
