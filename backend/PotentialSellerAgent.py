#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/9/12'
"""


from faker import Faker
from utils.Log import Log
from utils.Config import Config
from utils.Util import DataBaseOperate


class PotentialSellerAgent(object):
    L = Log("PotentialSellerAgent")
    data = Config('RegionAU').data
    state = {"1": "待开发", "2": "已开发"}
    gender = {1: "男", 2: "女"}
    fake = Faker()
    heads = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012058085.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012097899.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012131136.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012158702.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012174832.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012206259.png",
             "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012246905.png"]

    def __init__(self):
        state = list(self.data.keys())[self.fake.random_int(0, 7)]
        location = list(self.data[state][0].values())[0]
        self.image = self.heads[self.fake.random_int(0, 6)]
        self.L.logger.debug("待开发中介 头像 为 %s " % str(self.image))
        self.real_name = self.fake.name()
        self.L.logger.debug("待开发中介 姓名 为 %s " % str(self.real_name))
        self.status = "1"
        self.L.logger.debug("待开发中介 状态 为 %s " % self.state[self.status])
        self.mobile = self.fake.random_int(610000000, 619999999)
        self.L.logger.debug("待开发中介 手机 为 %s " % str(self.mobile))
        self.address = location['address']
        self.L.logger.debug("待开发中介 住址 为 %s " % str(self.address))
        self.lat = location['lat']
        self.L.logger.debug("待开发中介 维度 为 %s " % str(self.lat))
        self.lng = location['lng']
        self.L.logger.debug("待开发中介 经度 为 %s " % str(self.lng))
        self.sex = self.fake.random_int(1, 2)
        self.L.logger.debug("待开发中介 性别 为 %s " % self.gender[self.sex])
        self.published_farm_num = self.fake.random_int(1, 9)
        self.L.logger.debug("待开发中介 发布农场数 为 %s " % str(self.published_farm_num))

    def add(self):
        DataBaseOperate().operate("39.104.28.40", "farm-trade",
                                  "INSERT INTO `farm-trade`.`t_out_seller_agency` "
                                  "(`real_name`,`image`,`sex`,`mobile`,`lng`,`lat`,`status`,"
                                  "`published_farm_num`,`address`) "
                                  "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s');"
                                  % (self.real_name, self.image, self.sex, self.mobile,
                                     self.lng, self.lat, self.status, self.published_farm_num, self.address))


# if __name__ == '__main__':
#     # 此方法会往 待开发中介数据库`farm-trade`.`t_out_seller_agency`插入新的记录
#     PotentialSellerAgent().add()
