# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json

class TradeAction(object):

    def __init__(self, Trade):
        self.log = Log('Trade')
        self.request = Request()
        self.Trade = Trade

    def _admin_bs_order_close(self, orderNo, reason):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/bs/order/close')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        data['reason'] = reason
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/bs/order/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_bs_order_detail(self, orderNo):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/bs/order/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/bs/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_bs_order_list(self, orderStatus, startDate, endDate, orderNo, buyerName, sellerAgencyName, farmName, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/bs/order/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderStatus'] = orderStatus
        data['startDate'] = startDate
        data['endDate'] = endDate
        data['orderNo'] = orderNo
        data['buyerName'] = buyerName
        data['sellerAgencyName'] = sellerAgencyName
        data['farmName'] = farmName
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/bs/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_buyer_resource_audit(self, id, type, reason):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/buyer-resource/audit')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        data['type'] = type
        data['reason'] = reason
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/buyer-resource/audit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_buyer_resource_detail_resource_list(self, id):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/buyer-resource/detail-resource-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/buyer-resource/detail-resource-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_buyer_resource_list(self, orderNo, status, buyerName, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/buyer-resource/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        data['status'] = status
        data['buyerName'] = buyerName
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/buyer-resource/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_buyer_resource_pending_count(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/buyer-resource/pending-count')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/buyer-resource/pending-count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_seller_agency_audit(self, id, type, reason):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/seller-agency/audit')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        data['type'] = type
        data['reason'] = reason
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/audit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_seller_agency_detail(self, sellerAgencyId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/seller-agency/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sellerAgencyId'] = sellerAgencyId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_seller_agency_detail_resource_list(self, id):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/seller-agency/detail-resource-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/detail-resource-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_seller_agency_list(self, status, sellerAgencyName, mobileRegion, mobile, confirmTimeStart, confirmTimeEnd, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/seller-agency/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['status'] = status
        data['sellerAgencyName'] = sellerAgencyName
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['confirmTimeStart'] = confirmTimeStart
        data['confirmTimeEnd'] = confirmTimeEnd
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_cs_seller_agency_pending_count(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/cs/seller-agency/pending-count')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/cs/seller-agency/pending-count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_customer_service_remark_add_farm(self, orderId, title, remark):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/customer-service-remark/add-farm')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderId'] = orderId
        data['title'] = title
        data['remark'] = remark
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/add-farm', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_customer_service_remark_add_user(self, userId, remark):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/customer-service-remark/add-user')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['remark'] = remark
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/add-user', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_customer_service_remark_farm_list(self, farmId, buyerId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/customer-service-remark/farm-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['buyerId'] = buyerId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/farm-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_customer_service_remark_update_farm(self, id, title, remark):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/customer-service-remark/update-farm')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        data['title'] = title
        data['remark'] = remark
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/update-farm', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_customer_service_remark_update_user(self, id, remark):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/customer-service-remark/update-user')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        data['remark'] = remark
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/update-user', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_customer_service_remark_user_list(self, userId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/customer-service-remark/user-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/user-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_information_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm-information/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm-information/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_information_list(self, farmId, farmName, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm-information/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['farmName'] = farmName
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm-information/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_manage_audit(self, farmId, auditStatus, failReason):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm-manage/audit')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['auditStatus'] = auditStatus
        data['failReason'] = failReason
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm-manage/audit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_manage_confirm_update(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm-manage/confirm-update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm-manage/confirm-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_manage_detail(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm-manage/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm-manage/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_manage_list(self, farmName, farmId, farmer, sellerAgencyName, publishTimeStart, publishTimeEnd, isSale, auditStatus, translateStatus, saleStatus, confirmStatus, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm-manage/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmName'] = farmName
        data['farmId'] = farmId
        data['farmer'] = farmer
        data['sellerAgencyName'] = sellerAgencyName
        data['publishTimeStart'] = publishTimeStart
        data['publishTimeEnd'] = publishTimeEnd
        data['isSale'] = isSale
        data['auditStatus'] = auditStatus
        data['translateStatus'] = translateStatus
        data['saleStatus'] = saleStatus
        data['confirmStatus'] = confirmStatus
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm-manage/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_manage_off(self, farmId, closeType):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm-manage/off')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['closeType'] = closeType
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm-manage/off', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_manage_open(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm-manage/open')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm-manage/open', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_detail(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_gather_farm_publish(self, id, farmName, farmNameEn, type, totalPrice, unitCode, area, areaCode, unitPrice, address, addressEn, lng, lat, content, contentEn, landRights, soilPh, soilType, waterRights, waterRightsEn, regulations, regulationsEn, disadvantage, disadvantageEn, rainfall, imgList, nationId, provinceId, cityId, country):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/gather-farm-publish')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        data['farmName'] = farmName
        data['farmNameEn'] = farmNameEn
        data['type'] = type
        data['totalPrice'] = totalPrice
        data['unitCode'] = unitCode
        data['area'] = area
        data['areaCode'] = areaCode
        data['unitPrice'] = unitPrice
        data['address'] = address
        data['addressEn'] = addressEn
        data['lng'] = lng
        data['lat'] = lat
        data['content'] = content
        data['contentEn'] = contentEn
        data['landRights'] = landRights
        data['soilPh'] = soilPh
        data['soilType'] = soilType
        data['waterRights'] = waterRights
        data['waterRightsEn'] = waterRightsEn
        data['regulations'] = regulations
        data['regulationsEn'] = regulationsEn
        data['disadvantage'] = disadvantage
        data['disadvantageEn'] = disadvantageEn
        data['rainfall'] = rainfall
        data['imgList'] = imgList
        data['nationId'] = nationId
        data['provinceId'] = provinceId
        data['cityId'] = cityId
        data['country'] = country
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/gather-farm-publish', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_im_list(self, sellerAgencyId, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/im-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sellerAgencyId'] = sellerAgencyId
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/im-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_published_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/published-detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/published-detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_published_list(self, language, farmType, search, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/published-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['language'] = language
        data['farmType'] = farmType
        data['search'] = search
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/published-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_published_update(self, id, imgList, farmName, farmNameEn, type, totalPrice, unitCode, unitPrice, area, areaCode, nationId, provinceId, cityId, address, addressEn, lng, lat, content, contentEn, landRights, isResidential, soilPh, soilType, waterRights, waterRightsEn, regulations, regulationsEn, disadvantage, disadvantageEn, rainfall):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/published-update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        data['imgList'] = imgList
        data['farmName'] = farmName
        data['farmNameEn'] = farmNameEn
        data['type'] = type
        data['totalPrice'] = totalPrice
        data['unitCode'] = unitCode
        data['unitPrice'] = unitPrice
        data['area'] = area
        data['areaCode'] = areaCode
        data['nationId'] = nationId
        data['provinceId'] = provinceId
        data['cityId'] = cityId
        data['address'] = address
        data['addressEn'] = addressEn
        data['lng'] = lng
        data['lat'] = lat
        data['content'] = content
        data['contentEn'] = contentEn
        data['landRights'] = landRights
        data['isResidential'] = isResidential
        data['soilPh'] = soilPh
        data['soilType'] = soilType
        data['waterRights'] = waterRights
        data['waterRightsEn'] = waterRightsEn
        data['regulations'] = regulations
        data['regulationsEn'] = regulationsEn
        data['disadvantage'] = disadvantage
        data['disadvantageEn'] = disadvantageEn
        data['rainfall'] = rainfall
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/published-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_translate_detail_{id}(self, id):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/translate-detail/{id}')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/translate-detail/{id}', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_translate_list(self, search, type, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/translate-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['search'] = search
        data['type'] = type
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/translate-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_farm_translate_save(self, id, farmName, farmNameEn, address, addressEn, content, contentEn, waterRights, waterRightsEn, regulations, regulationsEn, disadvantage, disadvantageEn):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/farm/translate-save')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        data['farmName'] = farmName
        data['farmNameEn'] = farmNameEn
        data['address'] = address
        data['addressEn'] = addressEn
        data['content'] = content
        data['contentEn'] = contentEn
        data['waterRights'] = waterRights
        data['waterRightsEn'] = waterRightsEn
        data['regulations'] = regulations
        data['regulationsEn'] = regulationsEn
        data['disadvantage'] = disadvantage
        data['disadvantageEn'] = disadvantageEn
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/farm/translate-save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_im_buyer_before_send_auth_url(self, orderId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/im-buyer/before-send-auth-url')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderId'] = orderId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/im-buyer/before-send-auth-url', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_im_buyer_buyer_detail(self, buyerId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/im-buyer/buyer-detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['buyerId'] = buyerId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/im-buyer/buyer-detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_im_buyer_order_list(self, buyerId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/im-buyer/order-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['buyerId'] = buyerId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/im-buyer/order-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_im_buyer_sub_detail(self, buyerId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/im-buyer/sub-detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['buyerId'] = buyerId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/im-buyer/sub-detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_intent_order_add(self, orderNo, name, serviceType, mobile, status, farmId, comment, creatorId, editorId, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/intent-order/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        data['name'] = name
        data['serviceType'] = serviceType
        data['mobile'] = mobile
        data['status'] = status
        data['farmId'] = farmId
        data['comment'] = comment
        data['creatorId'] = creatorId
        data['editorId'] = editorId
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/intent-order/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_intent_order_close(self, orderId, comment):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/intent-order/close')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderId'] = orderId
        data['comment'] = comment
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/intent-order/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_intent_order_complete(self, orderId, comment):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/intent-order/complete')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderId'] = orderId
        data['comment'] = comment
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/intent-order/complete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_intent_order_list(self, orderNo, name, serviceType, mobile, status, farmId, comment, creatorId, editorId, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/intent-order/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        data['name'] = name
        data['serviceType'] = serviceType
        data['mobile'] = mobile
        data['status'] = status
        data['farmId'] = farmId
        data['comment'] = comment
        data['creatorId'] = creatorId
        data['editorId'] = editorId
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/intent-order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_order_add(self, orderNo, orderStatus, farmId, sellerAgencyId, buyerId, price, paidPrice, serviceType, comment, creatorId, editorId, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/order/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        data['orderStatus'] = orderStatus
        data['farmId'] = farmId
        data['sellerAgencyId'] = sellerAgencyId
        data['buyerId'] = buyerId
        data['price'] = price
        data['paidPrice'] = paidPrice
        data['serviceType'] = serviceType
        data['comment'] = comment
        data['creatorId'] = creatorId
        data['editorId'] = editorId
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/order/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_order_close(self, orderId, comment):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/order/close')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderId'] = orderId
        data['comment'] = comment
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/order/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_order_complete(self, orderId, paidPrice, comment):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/order/complete')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderId'] = orderId
        data['paidPrice'] = paidPrice
        data['comment'] = comment
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/order/complete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_order_detail(self, orderId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/order/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderId'] = orderId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/order/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_order_list(self, orderNo, orderStatus, farmId, sellerAgencyId, buyerId, price, paidPrice, serviceType, comment, creatorId, editorId, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/order/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        data['orderStatus'] = orderStatus
        data['farmId'] = farmId
        data['sellerAgencyId'] = sellerAgencyId
        data['buyerId'] = buyerId
        data['price'] = price
        data['paidPrice'] = paidPrice
        data['serviceType'] = serviceType
        data['comment'] = comment
        data['creatorId'] = creatorId
        data['editorId'] = editorId
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_user_detail(self, sellerAgencyId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/admin/user/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sellerAgencyId'] = sellerAgencyId
        response = self.request.post(url='http://dev.trade.worldfarm.com/admin/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_promoter_status_add(self, userId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/promoter-status/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/promoter-status/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_promoter_status_distribution(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/promoter-status/distribution')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/promoter-status/distribution', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_seller_agency_allot_exclusive_service(self, userId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/seller-agency/allot-exclusive-service')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/seller-agency/allot-exclusive-service', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_seller_agency_detail(self, userId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/seller-agency/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/seller-agency/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_seller_agency_get(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/seller-agency/get')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/seller-agency/get', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_seller_agency_get_auth_state(self, userId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/seller-agency/get-auth-state')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/seller-agency/get-auth-state', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_seller_agency_get_exclusive_service(self, userId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/seller-agency/get-exclusive-service')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/seller-agency/get-exclusive-service', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_service_status_close(self, userId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/service-status/close')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/service-status/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_service_status_init(self, userId, serviceType):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/service-status/init')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['serviceType'] = serviceType
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/service-status/init', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_service_status_update(self, userId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/api/service-status/update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.trade.worldfarm.com/api/service-status/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_farm_upload_ext(self, file):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/common/farm/upload-ext')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['file'] = file
        response = self.request.post(url='http://dev.trade.worldfarm.com/common/farm/upload-ext', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_farm_upload_img(self, file):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/common/farm/upload-img')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['file'] = file
        response = self.request.post(url='http://dev.trade.worldfarm.com/common/farm/upload-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_farm_upload_img_url(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/common/farm/upload-img-url')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/common/farm/upload-img-url', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_farm_upload_information(self, file):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/common/farm/upload-information')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['file'] = file
        response = self.request.post(url='http://dev.trade.worldfarm.com/common/farm/upload-information', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_user_upload_ext(self, file):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/common/user/upload-ext')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['file'] = file
        response = self.request.post(url='http://dev.trade.worldfarm.com/common/user/upload-ext', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _common_user_upload_head_img(self, file):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/common/user/upload-head-img')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['file'] = file
        response = self.request.post(url='http://dev.trade.worldfarm.com/common/user/upload-head-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_all_farm_dict(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-all-farm-dict')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-all-farm-dict', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_app_dict_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-app-dict-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-app-dict-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_area_range_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-area-range-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-area-range-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_banner_type(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-banner-type')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-banner-type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_city_list(self, pid):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-city-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pid'] = pid
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-city-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_farm_audit_status(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-farm-audit-status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-farm-audit-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_farm_is_sale(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-farm-is-sale')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-farm-is-sale', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_farm_sale_status(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-farm-sale-status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-farm-sale-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_farm_translate_status(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-farm-translate-status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-farm-translate-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_farm_type_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-farm-type-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-farm-type-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_farm_update_status(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-farm-update-status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-farm-update-status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_land_rights_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-land-rights-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-land-rights-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_mobile_sort_type_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-mobile-sort-type-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-mobile-sort-type-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_nation_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-nation-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-nation-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_price_range_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-price-range-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-price-range-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_soil_ph_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-soil-ph-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-soil-ph-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_soil_type_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-soil-type-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-soil-type-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _config_common_get_sort_type_list(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/config/common/get-sort-type-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/config/common/get-sort-type-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_banner_get_by_type(self, type, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/banner/get-by-type')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['type'] = type
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/banner/get-by-type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_resource_add(self, farmId, orderNo, companyName, businessLicenseNo, businessLicenseImgs, bankDepositProveImgs, bankStatementImgs, financingProductImgs):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer-resource/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['orderNo'] = orderNo
        data['companyName'] = companyName
        data['businessLicenseNo'] = businessLicenseNo
        data['businessLicenseImgs'] = businessLicenseImgs
        data['bankDepositProveImgs'] = bankDepositProveImgs
        data['bankStatementImgs'] = bankStatementImgs
        data['financingProductImgs'] = financingProductImgs
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer-resource/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_resource_detail(self, orderNo):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer-resource/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer-resource/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_resource_is_add(self, orderNo):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer-resource/is-add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer-resource/is-add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_resource_resource_list(self, orderNo, status, buyerName, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer-resource/resource-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        data['status'] = status
        data['buyerName'] = buyerName
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer-resource/resource-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_farm_detail(self, lng, lat, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/farm/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['lng'] = lng
        data['lat'] = lat
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/farm/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_farm_list(self, nationId, provinceId, farmTypeList, minArea, maxArea, minPrice, maxPrice, sortCode, lng, lat, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/farm/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['nationId'] = nationId
        data['provinceId'] = provinceId
        data['farmTypeList'] = farmTypeList
        data['minArea'] = minArea
        data['maxArea'] = maxArea
        data['minPrice'] = minPrice
        data['maxPrice'] = maxPrice
        data['sortCode'] = sortCode
        data['lng'] = lng
        data['lat'] = lat
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/farm/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_farm_map_list(self, trigger, leftTopLng, leftTopLat, rightBottomLng, rightBottomLat, zoomLevel, nationId, provinceId, farmTypeList, minArea, maxArea, minPrice, maxPrice, sortCode, lng, lat, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/farm/map-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['trigger'] = trigger
        data['leftTopLng'] = leftTopLng
        data['leftTopLat'] = leftTopLat
        data['rightBottomLng'] = rightBottomLng
        data['rightBottomLat'] = rightBottomLat
        data['zoomLevel'] = zoomLevel
        data['nationId'] = nationId
        data['provinceId'] = provinceId
        data['farmTypeList'] = farmTypeList
        data['minArea'] = minArea
        data['maxArea'] = maxArea
        data['minPrice'] = minPrice
        data['maxPrice'] = maxPrice
        data['sortCode'] = sortCode
        data['lng'] = lng
        data['lat'] = lat
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/farm/map-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_farm_recommend_list(self, pn, farmId, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/farm/recommend-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['farmId'] = farmId
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/farm/recommend-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_interest_batch_cancel_interest(self, farmIds):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/interest/batch-cancel-interest')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmIds'] = farmIds
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/interest/batch-cancel-interest', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_interest_interest_farm_list(self, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/interest/interest-farm-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/interest/interest-farm-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_interest_interest_or_not(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/interest/interest-or-not')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/interest/interest-or-not', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_subscribe_add(self, cityIds, farmType, minPrice, maxPrice, minArea, maxArea):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/subscribe/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['cityIds'] = cityIds
        data['farmType'] = farmType
        data['minPrice'] = minPrice
        data['maxPrice'] = maxPrice
        data['minArea'] = minArea
        data['maxArea'] = maxArea
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/subscribe/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_subscribe_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/subscribe/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/subscribe/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_subscribe_farm_list(self, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/subscribe/farm-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/subscribe/farm-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_subscribe_update(self, cityIds, farmType, minPrice, maxPrice, minArea, maxArea):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/subscribe/update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['cityIds'] = cityIds
        data['farmType'] = farmType
        data['minPrice'] = minPrice
        data['maxPrice'] = maxPrice
        data['minArea'] = minArea
        data['maxArea'] = maxArea
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/subscribe/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_user_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_user_query_sale(self, invitationCode):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/query-sale')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/user/query-sale', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_user_sale_bind(self, invitationCode):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/sale-bind')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/user/sale-bind', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_user_sale_bind_update(self, invitationCode, reason):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/sale-bind-update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        data['reason'] = reason
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/user/sale-bind-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_user_sale_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/sale-detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/user/sale-detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_user_send_auth_email(self, email):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/send-auth-email')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['email'] = email
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/user/send-auth-email', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_user_update(self, headImg, realName, sex, companyName, companyPosition):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['headImg'] = headImg
        data['realName'] = realName
        data['sex'] = sex
        data['companyName'] = companyName
        data['companyPosition'] = companyPosition
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/user/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_user_update_show_auth(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/buyer/user/update-show-auth')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/buyer/user/update-show-auth', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_common_suggestion_add(self, content, source):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/common/suggestion/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['content'] = content
        data['source'] = source
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/common/suggestion/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_farm_owner_add_farm(self, nationId, provinceId, cityId, country, lng, lat, address, images, propertyRightBoundaryList, government, governmentManager, workers, farmName, area, type, totalPrice, purchaseTimeStr, language):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/farm-owner/add-farm')
        data['_tk_'] = None
        data['_deviceId_'] = None
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
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/farm-owner/add-farm', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_farm_owner_detail(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/farm-owner/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/farm-owner/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_farm_owner_edit(self, farmId, farmName, area, type, totalPrice, purchaseTimeStr, language):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/farm-owner/edit')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['farmName'] = farmName
        data['area'] = area
        data['type'] = type
        data['totalPrice'] = totalPrice
        data['purchaseTimeStr'] = purchaseTimeStr
        data['language'] = language
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/farm-owner/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_farm_owner_list(self, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/farm-owner/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/farm-owner/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_farm_recommend_list(self, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/farm-recommend/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/farm-recommend/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

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

    def _mobile_intent_order_add_livestock(self, name, mobile, contactInformation):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/intent-order/add-livestock')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['name'] = name
        data['mobile'] = mobile
        data['contactInformation'] = contactInformation
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/intent-order/add-livestock', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_intent_order_add_translation(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/intent-order/add-translation')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/intent-order/add-translation', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_intermediary_bind(self, invitationCode):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/intermediary/bind')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/intermediary/bind', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_intermediary_detail(self, invitationCode):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/intermediary/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/intermediary/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_order_card_list(self, type, farmName, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/card-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['type'] = type
        data['farmName'] = farmName
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/order/card-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_order_del(self, orderNoList):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/del')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNoList'] = orderNoList
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/order/del', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_order_list(self, type, farmName, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['type'] = type
        data['farmName'] = farmName
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_order_promotion_buyer_list(self, farmId, sellerAgencyId, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/promotion/buyer-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['sellerAgencyId'] = sellerAgencyId
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/order/promotion/buyer-list', data=data)
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

    def _mobile_order_submit_intention_order(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/order/submit-intention-order')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/order/submit-intention-order', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_bind_detail(self, sellerAgencyId, lng, lat):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/bind/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sellerAgencyId'] = sellerAgencyId
        data['lng'] = lng
        data['lat'] = lat
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/bind/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_bind_list(self, sortCode):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/bind/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sortCode'] = sortCode
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/bind/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_bind_update_remark(self, sellAgencyId, remark):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/bind/update-remark')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sellAgencyId'] = sellAgencyId
        data['remark'] = remark
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/bind/update-remark', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_detail(self, farmId, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_dynamic_list(self, lng, lat, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/dynamic/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['lng'] = lng
        data['lat'] = lat
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/dynamic/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_im_send_farm_list(self, sellerAgencyId, nameLike, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/im/send-farm/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sellerAgencyId'] = sellerAgencyId
        data['nameLike'] = nameLike
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/im/send-farm/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_potential_agency_add_remark(self, sellerId, remark):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/potential-agency/add-remark')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sellerId'] = sellerId
        data['remark'] = remark
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/potential-agency/add-remark', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_potential_agency_bind(self, agencyId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/potential-agency/bind')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['agencyId'] = agencyId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/potential-agency/bind', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_potential_agency_detail(self, sellerId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/potential-agency/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sellerId'] = sellerId
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/potential-agency/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_farm_potential_agency_list(self, sortCode, sortType, lng, lat, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/farm/potential-agency/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sortCode'] = sortCode
        data['sortType'] = sortType
        data['lng'] = lng
        data['lat'] = lat
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/farm/potential-agency/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_user_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/user/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_user_update_birthday(self, birthday):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/user/update-birthday')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['birthday'] = birthday
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-birthday', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_user_update_head_img(self, headImg):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/user/update-head-img')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['headImg'] = headImg
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-head-img', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_user_update_mobile(self, mobileRegion, mobile):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/user/update-mobile')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_user_update_real_name(self, realName):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/user/update-real-name')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['realName'] = realName
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-real-name', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_user_update_sex(self, sex):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/user/update-sex')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sex'] = sex
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-sex', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_user_update_signature(self, signature):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/promoter/user/update-signature')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['signature'] = signature
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/promoter/user/update-signature', data=data)
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

    def _mobile_visa_add(self, visaTime, expiryTime, visaImgUrl):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/visa/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['visaTime'] = visaTime
        data['expiryTime'] = expiryTime
        data['visaImgUrl'] = visaImgUrl
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/visa/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_visa_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/visa/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/visa/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_visa_update(self, visaTime, expiryTime, visaImgUrl):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/mobile/visa/update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['visaTime'] = visaTime
        data['expiryTime'] = expiryTime
        data['visaImgUrl'] = visaImgUrl
        response = self.request.post(url='http://dev.trade.worldfarm.com/mobile/visa/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_resource_add(self, farmId, orderNo, companyName, businessLicenseNo, businessLicenseImgs, bankDepositProveImgs, bankStatementImgs, financingProductImgs):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['orderNo'] = orderNo
        data['companyName'] = companyName
        data['businessLicenseNo'] = businessLicenseNo
        data['businessLicenseImgs'] = businessLicenseImgs
        data['bankDepositProveImgs'] = bankDepositProveImgs
        data['bankStatementImgs'] = bankStatementImgs
        data['financingProductImgs'] = financingProductImgs
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer-resource/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_resource_confirmed_list(self, orderNo, status, buyerName, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/confirmed-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        data['status'] = status
        data['buyerName'] = buyerName
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer-resource/confirmed-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_resource_detail(self, orderNo):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer-resource/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_resource_is_add(self, orderNo):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/is-add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['orderNo'] = orderNo
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer-resource/is-add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_resource_update(self, id, companyName, businessLicenseNo, businessLicenseImgs, bankDepositProveImgs, bankStatementImgs, financingProductImgs):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer-resource/update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['id'] = id
        data['companyName'] = companyName
        data['businessLicenseNo'] = businessLicenseNo
        data['businessLicenseImgs'] = businessLicenseImgs
        data['bankDepositProveImgs'] = bankDepositProveImgs
        data['bankStatementImgs'] = bankStatementImgs
        data['financingProductImgs'] = financingProductImgs
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer-resource/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_farm_detail(self, lng, lat, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/farm/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['lng'] = lng
        data['lat'] = lat
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/farm/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_farm_list(self, provinceId, cityId, country, farmTypeList, minArea, maxArea, minPrice, maxPrice, sortCode, sortType, lng, lat, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/farm/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['provinceId'] = provinceId
        data['cityId'] = cityId
        data['country'] = country
        data['farmTypeList'] = farmTypeList
        data['minArea'] = minArea
        data['maxArea'] = maxArea
        data['minPrice'] = minPrice
        data['maxPrice'] = maxPrice
        data['sortCode'] = sortCode
        data['sortType'] = sortType
        data['lng'] = lng
        data['lat'] = lat
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/farm/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_farm_recommend_list(self, pn, farmId, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/farm/recommend-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['farmId'] = farmId
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/farm/recommend-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_user_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/user/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_user_query_sale(self, invitationCode):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/query-sale')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/user/query-sale', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_user_sale_bind(self, invitationCode):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/sale-bind')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/user/sale-bind', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_user_sale_bind_update(self, invitationCode, reason):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/sale-bind-update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['invitationCode'] = invitationCode
        data['reason'] = reason
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/user/sale-bind-update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_user_sale_detail(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/sale-detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/user/sale-detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_user_send_auth_email(self, email):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/send-auth-email')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['email'] = email
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/user/send-auth-email', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_user_update(self, headImg, realName, sex, companyName, companyPosition):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/buyer/user/update')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['headImg'] = headImg
        data['realName'] = realName
        data['sex'] = sex
        data['companyName'] = companyName
        data['companyPosition'] = companyPosition
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/buyer/user/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_order_list(self, provinceId, farmTypeList, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/order/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['provinceId'] = provinceId
        data['farmTypeList'] = farmTypeList
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/order/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_order_seller_agency_farm_buyer_list(self, farmId, type, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/order/seller-agency/farm/buyer-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['type'] = type
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/order/seller-agency/farm/buyer-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_order_seller_agency_message_buyer_list(self, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/order/seller-agency/message/buyer-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/order/seller-agency/message/buyer-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_order_submit_order(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/order/submit-order')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/order/submit-order', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farm_add_farm(self, nationId, provinceId, cityId, country, farmName, type, area, totalPrice, lng, lat, address, images, propertyRightBoundary, propertyRightCopy, content, realName, sex, birthday, mobile, headImg, farmerAddress, ownedFarmerNum, landRights, soilType, waterRights, regulations, disadvantage, rainfall, soilPh, language):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farm/add-farm')
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
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/add-farm', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farm_add_remark(self, farmId, remark):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farm/add-remark')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['remark'] = remark
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/add-remark', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farm_close(self, farmId, type):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farm/close')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        data['type'] = type
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/close', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farm_closed_list(self, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farm/closed-list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/closed-list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farm_detail(self, lng, lat, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farm/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['lng'] = lng
        data['lat'] = lat
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farm_im_send_farm_list(self, nameLike, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farm/im/send-farm/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['nameLike'] = nameLike
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/im/send-farm/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farm_list(self, sortCode, sortType, status, type, pn, ps):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farm/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['sortCode'] = sortCode
        data['sortType'] = sortType
        data['status'] = status
        data['type'] = type
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farm_update_farm(self, nationId, provinceId, cityId, country, farmName, type, area, totalPrice, lng, lat, address, images, content, landRights, soilType, waterRights, regulations, disadvantage, rainfall, soilPh, language, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farm/update-farm')
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
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farm/update-farm', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farmer_detail(self, farmId):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farmer/detail')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['farmId'] = farmId
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farmer/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_farmer_update(self, farmId, realName, sex, birthday, mobile, headImg, farmerAddress, ownedFarmerNum):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/farmer/update')
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
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/farmer/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_user_add(self, realName, companyName, abnCode, resource):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/user/add')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['realName'] = realName
        data['companyName'] = companyName
        data['abnCode'] = abnCode
        data['resource'] = resource
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/user/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_seller_agency_user_status(self):
        data = self.Trade.get('http://dev.trade.worldfarm.com').get('/web/seller-agency/user/status')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.trade.worldfarm.com/web/seller-agency/user/status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
