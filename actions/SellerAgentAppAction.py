# encoding: utf-8

"""
__author__ = "Bai Ying"
__date__ = 2018/10/22
"""
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

    def _mobile_farm_search(self, keyWords):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/farm/search')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['keyWords'] = keyWords
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/farm/search', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_add_farm(self, nationId, provinceId, cityId, country, farmName, type, area, totalPrice, lng, lat, address, images, propertyRightBoundary, propertyRightCopy, content, realName, sex, birthday, mobile, headImg, farmerAddress, ownedFarmerNum, landRights, soilType, waterRights, regulations, disadvantage, rainfall, soilPh, language):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/add-farm')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['nationId'] = nationId
        data['provinceId'] = provinceId
        data['cityId'] = cityId
        data['country'] = country
        data['farmName'] = farmName
        data['type'] = type
        data['area'] = area
        data['totalPrice'] = totalPrice
        data['lng'] = lng
        data['lat'] = lat
        data['address'] = address
        data['images'] = images
        data['propertyRightBoundary'] = propertyRightBoundary
        data['propertyRightCopy'] = propertyRightCopy
        data['content'] = content
        data['realName'] = realName
        data['sex'] = sex
        data['birthday'] = birthday
        data['mobile'] = mobile
        data['headImg'] = headImg
        data['farmerAddress'] = farmerAddress
        data['ownedFarmerNum'] = ownedFarmerNum
        data['landRights'] = landRights
        data['soilType'] = soilType
        data['waterRights'] = waterRights
        data['regulations'] = regulations
        data['disadvantage'] = disadvantage
        data['rainfall'] = rainfall
        data['soilPh'] = soilPh
        data['language'] = language
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/add-farm', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_add_remark(self, farmId, remark):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/add-remark')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['remark'] = remark
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/add-remark', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_close(self, farmId, type):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/close')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['type'] = type
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_closed_list(self, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/closed-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/closed-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_detail(self, lng, lat, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['lng'] = lng
        data['lat'] = lat
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_im_send_farm_list(self, nameLike, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/im/send-farm/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['nameLike'] = nameLike
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/im/send-farm/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_list(self, sortCode, sortType, status, type, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sortCode'] = sortCode
        data['sortType'] = sortType
        data['status'] = status
        data['type'] = type
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_map_list(self, farmName, lng, lat, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/map-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmName'] = farmName
        data['lng'] = lng
        data['lat'] = lat
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/map-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_open(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/open')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/open', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farm_update_farm(self, nationId, provinceId, cityId, country, farmName, type, area, totalPrice, lng, lat, address, images, content, landRights, soilType, waterRights, regulations, disadvantage, rainfall, soilPh, language, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farm/update-farm')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['nationId'] = nationId
        data['provinceId'] = provinceId
        data['cityId'] = cityId
        data['country'] = country
        data['farmName'] = farmName
        data['type'] = type
        data['area'] = area
        data['totalPrice'] = totalPrice
        data['lng'] = lng
        data['lat'] = lat
        data['address'] = address
        data['images'] = images
        data['content'] = content
        data['landRights'] = landRights
        data['soilType'] = soilType
        data['waterRights'] = waterRights
        data['regulations'] = regulations
        data['disadvantage'] = disadvantage
        data['rainfall'] = rainfall
        data['soilPh'] = soilPh
        data['language'] = language
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farm/update-farm', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farmer_detail(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farmer/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farmer/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_farmer_update(self, farmId, realName, sex, birthday, mobile, headImg, farmerAddress, ownedFarmerNum):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/farmer/update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['realName'] = realName
        data['sex'] = sex
        data['birthday'] = birthday
        data['mobile'] = mobile
        data['headImg'] = headImg
        data['farmerAddress'] = farmerAddress
        data['ownedFarmerNum'] = ownedFarmerNum
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/farmer/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_user_add(self, realName, companyName, abnCode, resource):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/user/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['realName'] = realName
        data['companyName'] = companyName
        data['abnCode'] = abnCode
        data['resource'] = resource
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/user/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_user_status(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/seller-agency/user/status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/seller-agency/user/status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_order_seller_agency_farm_buyer_list(self, farmId, type, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/seller-agency/farm/buyer-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['type'] = type
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/order/seller-agency/farm/buyer-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_order_seller_agency_message_buyer_list(self, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/seller-agency/message/buyer-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/order/seller-agency/message/buyer-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_center_unread(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/message-center/unread')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_push_message_count_unread(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/seller-agency/push-message/count-unread')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/seller-agency/push-message/count-unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_push_message_detail(self, id):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/seller-agency/push-message/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/seller-agency/push-message/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_push_message_list(self, pn, ps):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/seller-agency/push-message/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/seller-agency/push-message/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_seller_agency_push_message_read(self, msgId):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/seller-agency/push-message/read')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['msgId'] = msgId
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/seller-agency/push-message/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_push_auth_get_alias_seller_agency(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/push-auth/get/alias/seller-agency')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/push-auth/get/alias/seller-agency', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")


