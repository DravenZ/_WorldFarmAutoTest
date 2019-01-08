#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/20'
"""

import unittest
from utils.Log import Log
from utils.Config import Config
from backend.Tool import Tool
from backend.User import User
from actions.AppBuyerAction import AppBuyerAction
from actions.WebBuyerAction import WebBuyerAction
from actions.ServiceAction import ServiceAction
from actions.PromoterAction import PromoterAction
from backend.Employee import Employee
from actions.SellerAgent import SellerAgent
import json


class Main(unittest.TestCase):
    L = Log('Main')
    tool = Tool()
    user = User("18602832572", "123456a", register=False)
    appbuyeraction = AppBuyerAction(user)
    webbuyeraction = WebBuyerAction(user)
    pa = PromoterAction(Employee('100028', '123456'))
    # user = User("13658082213", "123456a", register=False)
    # buyeraction = BuyerAction(user)
    # employee = Employee(buyeraction.get_customer_account(), '123456')
    emp = Employee("100005", "123456")
    dataTRADE = Config('trade').data
    service = ServiceAction(emp)
    seller_agent = SellerAgent(user)

    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test2000(self):
        """
        mobile卖家中介模糊搜索农场
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.mobile_seller_agent_search_farm("漫花庄园", language='zh')

    def test2001(self):
        """
        mobile卖家中介新增农场备注
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.mobile_seller_agency_add_remark(415, "lalal", language='zh')

    def test2002(self):
        """
        mobile卖家中介关闭农场
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.mobile_seller_agency_close_farm(522, 30, language='zh')

    def test2003(self):
        """
        mobile卖家中介关闭农场列表
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.mobile_seller_agency_close_farm_list(419, language='zh')

    def test2004(self):
        """
        mobile卖家中介农场详情
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_farm_detail(140.7842627, 37.8301386, 523, language='zh')

    def test2005(self):
        """
        mobile卖家中介已发布农场列表
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_farm_list(2, language='zh')

    def test2006(self):
        """
        mobile卖家中介已发布农场地图页
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_map_list(140.7842627, 37.8301386, language='zh')

    def test2007(self):
        """
        mobile卖家中介农场详情
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_update_farm(
            516, {"area": 12}, language='zh')

    def test2008(self):
        """
        mobile卖家中介农场主
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_farmer_detail(528, language='zh')

    def test2009(self):
        """
        mobile卖家中介更新农场主
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_farmer_update(
            528, '王二麻子', 1, "2018-01-01", 18602883456,
            "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1535092943322.jpg",
            '嘿嘿嘿', 11, language='zh')

    def test2010(self):
        """
        mobile卖家中介增加资质
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_use_add(
            '王二麻子', "叽里呱啦大公司",
            '[{"type": "2",'
            '"url": "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1535093109545.jpg"},'
            '{"type": "3",'
            '"url": "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1535092873551.jpg"},'
            '{"type": "4",'
            '"url": "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1535092943322.jpg"}]',
            language='zh')

    def test2011(self):
        """
        mobile卖家中介资质状态
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_use_status(language='zh')

    def test2012(self):
        """
        mobile卖家中介农场意向买家列表
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_farm_buyer_list(414, 3, 1, language='zh')

    def test2013(self):
        """
        mobile卖家中介消息意向买家列表
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.mobile_seller_agency_message_buyer_list(language='zh')

    def test2014(self):
        """
        mobile卖家中介IM发送农场
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.mobile_seller_agency_im_send_farm_list("庄园", language='zh')

    def test2015(self):
        """
        web卖家中介新增备注
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.web_seller_agency_add_remark(415, "web自动化测试备注", language='zh')

    def test2016(self):
        """
        web卖家中介新增农场
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.web_seller_agent_add_farm("web测试大娃二娃农场名", "种植", "南澳大利亚",
                                               "2000万-3500万", "5000亩-10000亩", language='zh')

    def test2017(self):
        """
        web卖家中介关闭农场
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.web_seller_agency_close_farm(522, 30, language='zh')

    def test2018(self):
        """
        web卖家中介关闭农场列表
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.web_seller_agency_close_farm_list(419, language='zh')

    def test2019(self):
        """
        web卖家中介农场详情
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_farm_detail(140.7842627, 37.8301386, 523, language='zh')

    def test2020(self):
        """
        web卖家中介已发布农场列表
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_farm_list(2, language='zh')

    def test2021(self):
        """
        web卖家中介更新农场
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_update_farm(
            516, {"area": 12}, language='zh')

    def test2022(self):
        """
        web卖家中介农场主
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_farmer_detail(528, language='zh')

    def test2023(self):
        """
        web卖家中介更新农场主
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_farmer_update(
            528, {'realName': ' web测试'}, language='zh')

    def test2024(self):
        """
        web卖家中介增加资质
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_use_add(
            '王二麻子', "叽里呱啦大公司",
            '[{"type": "2",'
            '"url": "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1535093109545.jpg"},'
            '{"type": "3",'
            '"url": "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1535092873551.jpg"},'
            '{"type": "4",'
            '"url": "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1535092943322.jpg"}]',
            language='zh')

    def test2025(self):
        """
        web卖家中介资质状态
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_use_status(language='zh')

    def test2026(self):
        """
        web卖家中介农场意向买家列表
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_farm_buyer_list(414, 3, 1, language='zh')

    def test2027(self):
        """
        web卖家中介消息意向买家列表
        :return:
        """
        seleragency = SellerAgent(self.user)
        seleragency.web_seller_agency_message_buyer_list(language='zh')

    def test2028(self):
        """
        mobile卖家中介新增农场
        :return:
        """
        selleragency = SellerAgent(self.user)
        selleragency.mobile_seller_agent_add_farm("web测试大娃二娃农场名", "种植", "南澳大利亚",
                                                  "2000万-3500万", "5000亩-10000亩", language='zh')

    def test0001(self):
        """
        app买家绑定销售ID
        :return:
        """

        re = self.appbuyeraction.app_buyer_sale_bind(487)
        print(re)
        re = self.appbuyeraction.app_buyer_query_sale(487)
        print(re)

    def test0002(self):
        """
        app查询用户个人信息
        :return:
        """
        user_info = self.appbuyeraction.app_buyer_user_detail()
        print(user_info)

    def test0003(self):
        """
        app感兴趣
        :return:
        """
        print(self.appbuyeraction.app_get_order_no(self.appbuyeraction.app_get_farm_list_first_id()))

    def test0004(self):
        """
        app用户修改个人信息
        :return:
        """
        self.appbuyeraction.app_buyer_update_user("星买家", "男", "成都大农科技有限公司", "前端工程师",
                                "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012058085.png")

    def test0005(self):
        """
        app上传购买资质
        :return:
        """
        farm_id = self.appbuyeraction.app_get_farm_list_first_id()
        is_add = self.appbuyeraction.app_buyer_resource_is_add(self.appbuyeraction.app_get_order_no(farm_id))
        r = self.appbuyeraction.app_buyer_resource_add(farm_id,
                                                       self.appbuyeraction.app_get_order_no(farm_id))
        print(is_add)
        print(r)

    def test0006(self):
        """
        app查看购买资质详情
        :return:
        """
        farm_id = self.appbuyeraction.app_get_farm_list_first_id()
        r = self.appbuyeraction.app_buyer_resource_detail(self.appbuyeraction.app_get_order_no(farm_id))
        print(r)

    def test0008(self):
        """
        app卖家中介上传及认证
        :return:
        """
        self.seller_agent.mobile_approve_seller_agent("张鹏飞", "大农科技")
        self.tool.operator_approve_seller_agent("18380581401", True)

    def test0009(self):
        """
        app卖家中介绑定客服,地推
        :return:
        """
        self.pa.promoter_bind_seller_agent(self.user.user_id)

    def test0007(self):
        """
        app卖家发布场--买家感兴趣--客服邀请上传资质--买家上传资质--客服审核资质
        :return:
        """
        farm_id = self.seller_agent.mobile_seller_agent_add_farm("调试农场名", "种植", "南澳大利亚", "2000万-3500万",
                                                                 "5000亩-10000亩", language='zh')
        # farm_id = self.buyeraction.app_get_farm_id()
        order_no = self.appbuyeraction.app_get_order_no(farm_id)
        order_id = self.tool.query_order_id_by_order_no(order_no)
        self.service.service_send_auth_url(order_id)
        self.appbuyeraction.app_buyer_resource_is_add(order_no)
        self.appbuyeraction.app_buyer_resource_add(farm_id, order_no)
        response_resource_list = self.service.service_buyer_resource_list(order_no, self.user.real_name)
        response_resource_list = json.loads(response_resource_list)
        resource_list = response_resource_list.get('content').get('datas')
        resource_id = None
        for resource in resource_list:
            resource_order_no = resource.get('orderNo')
            if resource_order_no == order_no:
                resource_id = resource.get('id')
        self.service.service_buyer_resource_audit(resource_id, 2, "接口测试不通过")

    def test0010(self):
        """
        app农场列表
        :return:
        """
        print(self.appbuyeraction.app_get_farm_list())

    def test0011(self):
        """
        app农场详情
        :return:
        """
        self.appbuyeraction.app_get_farm_detail(self.appbuyeraction.app_get_farm_list_first_id())

    def test0012(self):
        """
        web端
        卖家发布场--买家感兴趣--客服邀请上传资质--买家上传资质--客服审核资质
        :return:
        """
        farm_id = self.seller_agent.web_seller_agent_add_farm("调试农场名", "种植", "南澳大利亚", "2000万-3500万",
                                                              "5000亩-10000亩", language='zh')
        order_no = self.webbuyeraction.web_get_order_no(farm_id)
        order_id = self.tool.query_order_id_by_order_no(order_no)
        self.service.service_send_auth_url(order_id)
        self.webbuyeraction.web_buyer_resource_is_add(order_no)
        self.webbuyeraction.web_buyer_resource_add(farm_id, order_no)
        response_resource_list = self.service.service_buyer_resource_list(order_no, self.user.real_name)
        response_resource_list = json.loads(response_resource_list)
        resource_list = response_resource_list.get('content').get('datas')
        resource_id = None
        for resource in resource_list:
            resource_order_no = resource.get('orderNo')
            if resource_order_no == order_no:
                resource_id = resource.get('id')
        self.service.service_buyer_resource_audit(resource_id, 2, "接口测试不通过")

    def test0013(self):
        """
        app查询是都显示认证提示
        :return:
        """
        self.appbuyeraction.app_buyer_update_show_auth()

    def test0014(self):
        """
        添加订阅规则
        :return:
        """
        self.appbuyeraction.app_buyer_subscribe_add()

    def test0015(self):
        """
        订阅规则详情
        :return:
        """
        self.appbuyeraction.app_buyer_subscribe_detail()

    def test0016(self):
        """
        修改订阅规则
        :return:
        """
        self.appbuyeraction.app_buyer_subscribe_update()


if __name__ == '__main__':
    m = Main()
    # m.seller_agent_add_farm("18602832572", "123456a", "调试农场名", "种植", "南澳大利亚", "2000万-3500万", "5000亩-10000亩")

