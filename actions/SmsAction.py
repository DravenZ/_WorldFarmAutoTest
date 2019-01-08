# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json

class SmsAction(object):

    def __init__(self, Sms):
        self.request = Request()
        self.log = Log('Sms')
        self.request = Request()
        self.Sms = Sms

    def _admin_im_auth_get_im_account_service(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/admin/im-auth/get/im-account/service')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/admin/im-auth/get/im-account/service', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _admin_im_auth_service_get_accid(self, userId):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/admin/im-auth/service-get/accid')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.sms.worldfarm.com/admin/im-auth/service-get/accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_im_send(self, fromUid, fromUserType, toUid, toUserType, content, ext):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/api/im/send')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['fromUid'] = fromUid
        data['fromUserType'] = fromUserType
        data['toUid'] = toUid
        data['toUserType'] = toUserType
        data['content'] = content
        data['ext'] = ext
        response = self.request.post(url='http://dev.sms.worldfarm.com/api/im/send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_shortMessage_validate_verify_code(self, mobileRegion, mobile, verifyCode, businessType):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/api/shortMessage/validate-verify-code')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['verifyCode'] = verifyCode
        data['businessType'] = businessType
        response = self.request.post(url='http://dev.sms.worldfarm.com/api/shortMessage/validate-verify-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_message_center_list(self, category, pn, ps):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/buyer/message-center/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['category'] = category
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/buyer/message-center/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_message_center_read(self, category):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/buyer/message-center/read')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['category'] = category
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/buyer/message-center/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_message_center_unread(self, category):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/buyer/message-center/unread')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['category'] = category
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/buyer/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_sub_message_read(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/buyer/sub-message/read')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/buyer/sub-message/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_buyer_sub_message_unread(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/buyer/sub-message/unread')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/buyer/sub-message/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_im_auth_buyer_and_seller_allot_exclusive_service_accid(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/im-auth/buyer-and-seller/allot/exclusive-service-accid')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/im-auth/buyer-and-seller/allot/exclusive-service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_im_auth_buyer_and_seller_get_exclusive_service_accid(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/im-auth/buyer-and-seller/get/exclusive-service-accid')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/im-auth/buyer-and-seller/get/exclusive-service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_im_auth_buyer_and_seller_get_im_account(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/im-auth/buyer-and-seller/get/im-account')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/im-auth/buyer-and-seller/get/im-account', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_im_auth_buyer_and_seller_get_service_accid(self, userId):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/im-auth/buyer-and-seller/get/service-accid')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/im-auth/buyer-and-seller/get/service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_im_auth_promoter_get_im_account(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/im-auth/promoter/get/im-account')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/im-auth/promoter/get/im-account', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_im_auth_promoter_get_seller_agency_accid(self, userId):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/im-auth/promoter/get/seller-agency-accid')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/im-auth/promoter/get/seller-agency-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_center_list(self, pn, ps):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/message-center/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/message-center/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_message_center_read(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/message-center/read')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/message-center/read', data=data)
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

    def _mobile_promoter_push_message_count_unread(self, category):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/promoter/push-message/count-unread')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['category'] = category
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/promoter/push-message/count-unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_push_message_list(self, category, pn, ps):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/promoter/push-message/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['category'] = category
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/promoter/push-message/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_promoter_push_message_read(self, msgId):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/promoter/push-message/read')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['msgId'] = msgId
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/promoter/push-message/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_push_auth_get_alias_buyer(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/push-auth/get/alias/buyer')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/push-auth/get/alias/buyer', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_push_auth_get_alias_buyer_and_seller(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/push-auth/get/alias/buyer-and-seller')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/push-auth/get/alias/buyer-and-seller', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_push_auth_get_alias_promoter(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/mobile/push-auth/get/alias/promoter')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/mobile/push-auth/get/alias/promoter', data=data)
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

    def _tx_get_user_info(self, accid):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/tx/get/user-info')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['accid'] = accid
        response = self.request.post(url='http://dev.sms.worldfarm.com/tx/get/user-info', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_message_center_list(self, category, pn, ps):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/buyer/message-center/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['category'] = category
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/buyer/message-center/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_message_center_read(self, category):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/buyer/message-center/read')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['category'] = category
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/buyer/message-center/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_buyer_message_center_unread(self, category):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/buyer/message-center/unread')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['category'] = category
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/buyer/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_im_auth_buyer_and_seller_allot_exclusive_service_accid(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/im-auth/buyer-and-seller/allot/exclusive-service-accid')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/im-auth/buyer-and-seller/allot/exclusive-service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_im_auth_buyer_and_seller_get_exclusive_service_accid(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/im-auth/buyer-and-seller/get/exclusive-service-accid')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/im-auth/buyer-and-seller/get/exclusive-service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_im_auth_buyer_and_seller_get_im_account(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/im-auth/buyer-and-seller/get/im-account')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/im-auth/buyer-and-seller/get/im-account', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_im_auth_buyer_and_seller_get_service_accid(self, userId):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/im-auth/buyer-and-seller/get/service-accid')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/im-auth/buyer-and-seller/get/service-accid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_message_center_list(self, pn, ps):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/message-center/list')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['pn'] = pn
        data['ps'] = ps
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/message-center/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_message_center_read(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/message-center/read')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/message-center/read', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_message_center_unread(self):
        data = self.Sms.get('http://dev.sms.worldfarm.com').get('/web/message-center/unread')
        data['_tk_'] = None
        data['_deviceId_'] = None
        response = self.request.post(url='http://dev.sms.worldfarm.com/web/message-center/unread', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
