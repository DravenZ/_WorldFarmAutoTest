#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/20'
"""

from faker import Faker
from utils.Log import Log


class Farmer(object):
    L = Log("Farmer")
    fake = Faker()

    heads = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012058085.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012097899.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012131136.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012158702.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012174832.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012206259.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012246905.png"]
    gender = {1: "男", 2: "女"}

    def __init__(self):
        self.head_img = self.heads[self.fake.random_int(0, 6)]
        self.L.logger.debug(u"农场主头像 为 %s " % str(self.head_img))
        self.real_name = self.fake.name()
        self.L.logger.debug(u"农场主姓名 为 %s " % str(self.real_name))
        self.birthday = self.fake.date_of_birth()
        self.L.logger.debug(u"农场主生日 为 %s " % str(self.birthday))
        self.mobile = self.fake.random_int(610000000, 619999999)
        self.L.logger.debug(u"农场主手机 为 %s " % str(self.mobile))
        self.farmer_address = self.fake.address().replace('\n', ' ')
        self.L.logger.debug(u"农场主住址 为 %s " % str(self.farmer_address))
        self.sex = self.fake.random_int(1, 2)
        self.L.logger.debug("农场主性别 为 %s " % self.gender[self.sex])
        self.owned_farmer_num = self.fake.random_int(1, 9)
        self.L.logger.debug(u"农场主拥有农场数 为 %s " % str(self.owned_farmer_num))

#
# if __name__ == '__main__':
#     Farmer()
