# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json

class ReportAction(object):

    def __init__(self, Report):
        self.log = Log('Report')
        self.request = Request()
        self.Report = Report

    def _admin_buyerMonthRank_list(self, numSort, efficiencySort, pn, ps):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/buyerMonthRank/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['numSort'] = numSort
        data['efficiencySort'] = efficiencySort
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/buyerMonthRank/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_buyerMonthRank_user_list(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/buyerMonthRank/user-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/buyerMonthRank/user-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_buyerWeekRank_list(self, numSort, efficiencySort, pn, ps):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/buyerWeekRank/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['numSort'] = numSort
        data['efficiencySort'] = efficiencySort
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/buyerWeekRank/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_buyerWeekRank_user_list(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/buyerWeekRank/user-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/buyerWeekRank/user-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_buyerYearRankWeb_list(self, numSort, efficiencySort, pn, ps):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/buyerYearRankWeb/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['numSort'] = numSort
        data['efficiencySort'] = efficiencySort
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/buyerYearRankWeb/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_buyerYearRankWeb_user_list(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/buyerYearRankWeb/user-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/buyerYearRankWeb/user-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_statistics_list(self, year):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/cs/statistics/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['year'] = year
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/cs/statistics/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_promoter_statistics_list(self, year):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/promoter/statistics/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['year'] = year
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/promoter/statistics/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_sale_statistics_list(self, year):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/admin/sale/statistics/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['year'] = year
        response = self.request.post(url='http://dev.report.worldfarm.com/admin/sale/statistics/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_month_my_rank(self, type):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/mobile/promoter/month/my-rank')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['type'] = type
        response = self.request.post(url='http://dev.report.worldfarm.com/mobile/promoter/month/my-rank', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_month_rank_list(self, type, pn, ps):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/mobile/promoter/month/rank-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['type'] = type
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.report.worldfarm.com/mobile/promoter/month/rank-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_statistics_achievement_detail(self, staDate, pn, ps):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/mobile/promoter/statistics/achievement-detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['staDate'] = staDate
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.report.worldfarm.com/mobile/promoter/statistics/achievement-detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_total_my_rank(self, type):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/mobile/promoter/total/my-rank')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['type'] = type
        response = self.request.post(url='http://dev.report.worldfarm.com/mobile/promoter/total/my-rank', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_total_rank_list(self, type, pn, ps):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/mobile/promoter/total/rank-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['type'] = type
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.report.worldfarm.com/mobile/promoter/total/rank-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_promoterDailySta(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/promoterDailySta')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/promoterDailySta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_promoterMonthRank(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/promoterMonthRank')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/promoterMonthRank', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_promoterTotalRank(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/promoterTotalRank')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/promoterTotalRank', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_saleDailySta(self, date):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/saleDailySta')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['date'] = date
        response = self.request.post(url='http://dev.report.worldfarm.com/test/saleDailySta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_saleHistorySta(self, startDate, endDate):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/saleHistorySta')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['startDate'] = startDate
        data['endDate'] = endDate
        response = self.request.post(url='http://dev.report.worldfarm.com/test/saleHistorySta', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_test_cs(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/test-cs')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/test-cs', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_test_month(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/test-month')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/test-month', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_test_week(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/test-week')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/test-week', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_test_year(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/test-year')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/test-year', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_test1(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/test1')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/test1', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_test2(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/test2')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/test2', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _test_test3(self):
        data = self.Report.get('http://dev.report.worldfarm.com').get('/test/test3')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.report.worldfarm.com/test/test3', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
