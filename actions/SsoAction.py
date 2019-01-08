# encoding: utf-8

from utils.Config import Config
from utils.Util import Request
from backend.Tool import Tool
from utils.Log import Log
import json

class SsoAction(object):

    def __init__(self, Sso):
        self.log = Log('Sso')
        self.request = Request()
        self.Sso = Sso

    def _admin_user_validate_email(self, userId, timeStamp, token):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/admin/user/validate-email')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['userId'] = userId
        data['timeStamp'] = timeStamp
        data['token'] = token
        response = self.request.post(url='http://dev.sso.worldfarm.com/admin/user/validate-email', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _api_sso_check_token(self, ip, deviceType, deviceId, token):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/api/sso/check-token')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['ip'] = ip
        data['deviceType'] = deviceType
        data['deviceId'] = deviceId
        data['token'] = token
        response = self.request.post(url='http://dev.sso.worldfarm.com/api/sso/check-token', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_automatic_login(self, token, encryptedPwd, deviceId):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/automatic-login')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['token'] = token
        data['encryptedPwd'] = encryptedPwd
        data['deviceId'] = deviceId
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/automatic-login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_emp_login(self, account, password, deviceId, deviceType):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/emp-login')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['account'] = account
        data['password'] = password
        data['deviceId'] = deviceId
        data['deviceType'] = deviceType
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/emp-login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_login(self, mobileRegion, mobile, password, deviceId, deviceType):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/login')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        data['deviceId'] = deviceId
        data['deviceType'] = deviceType
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_logout(self, tk):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/logout')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['tk'] = tk
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/logout', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_query_lock_time(self, loginName):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/query-lock-time')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['loginName'] = loginName
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/query-lock-time', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_register(self, mobileRegion, mobile, newPassword, deviceId, businessToken):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/register')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newPassword'] = newPassword
        data['deviceId'] = deviceId
        data['businessToken'] = businessToken
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/register', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_register_send(self, mobileRegion, mobile):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/register/send')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/register/send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_register_validate_verify_code(self, mobileRegion, mobile, verifyCode):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/register/validate-verify-code')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['verifyCode'] = verifyCode
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/register/validate-verify-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_update_mobile(self, mobileRegion, mobile, newMobileRegion, newMobile, verifyCode):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/update-mobile')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newMobileRegion'] = newMobileRegion
        data['newMobile'] = newMobile
        data['verifyCode'] = verifyCode
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_update_mobile_send(self, mobileRegion, mobile, newMobileRegion, newMobile, businessToken):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/update-mobile/send')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newMobileRegion'] = newMobileRegion
        data['newMobile'] = newMobile
        data['businessToken'] = businessToken
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/update-mobile/send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_update_mobile_validate_pwd(self, mobileRegion, mobile, password, token, deviceId):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/update-mobile/validate-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        data['token'] = token
        data['deviceId'] = deviceId
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/update-mobile/validate-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_update_pwd(self, mobileRegion, mobile, password, newPassword, token, deviceId):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/update-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        data['newPassword'] = newPassword
        data['token'] = token
        data['deviceId'] = deviceId
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/update-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_update_pwd_forget_password(self, mobileRegion, mobile, newPassword, businessToken):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/update-pwd/forget-password')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newPassword'] = newPassword
        data['businessToken'] = businessToken
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/update-pwd/forget-password', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_update_pwd_send(self, mobileRegion, mobile):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/update-pwd/send')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/update-pwd/send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _mobile_sso_update_pwd_validate(self, mobileRegion, mobile, verifyCode):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/mobile/sso/update-pwd/validate')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['verifyCode'] = verifyCode
        response = self.request.post(url='http://dev.sso.worldfarm.com/mobile/sso/update-pwd/validate', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_login(self, mobileRegion, mobile, password, deviceId, deviceType):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/login')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        data['deviceId'] = deviceId
        data['deviceType'] = deviceType
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_logout(self, tk):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/logout')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['tk'] = tk
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/logout', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_operator_emp_login(self, account, password):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/operator-emp-login')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['account'] = account
        data['password'] = password
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/operator-emp-login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_query_lock_time(self, loginName):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/query-lock-time')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['loginName'] = loginName
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/query-lock-time', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_register(self, mobileRegion, mobile, newPassword, deviceId, businessToken):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/register')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newPassword'] = newPassword
        data['deviceId'] = deviceId
        data['businessToken'] = businessToken
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/register', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_register_send(self, mobileRegion, mobile):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/register/send')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/register/send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_register_validate_verify_code(self, mobileRegion, mobile, verifyCode):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/register/validate-verify-code')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['verifyCode'] = verifyCode
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/register/validate-verify-code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_service_emp_login(self, account, password):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/service-emp-login')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['account'] = account
        data['password'] = password
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/service-emp-login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_update_mobile(self, mobileRegion, mobile, newMobileRegion, newMobile, verifyCode):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/update-mobile')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newMobileRegion'] = newMobileRegion
        data['newMobile'] = newMobile
        data['verifyCode'] = verifyCode
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/update-mobile', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_update_mobile_send(self, mobileRegion, mobile, newMobileRegion, newMobile, businessToken):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/update-mobile/send')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newMobileRegion'] = newMobileRegion
        data['newMobile'] = newMobile
        data['businessToken'] = businessToken
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/update-mobile/send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_update_mobile_validate_pwd(self, mobileRegion, mobile, password, token, deviceId):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/update-mobile/validate-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        data['token'] = token
        data['deviceId'] = deviceId
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/update-mobile/validate-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_update_pwd(self, mobileRegion, mobile, password, newPassword, token, deviceId):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/update-pwd')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['password'] = password
        data['newPassword'] = newPassword
        data['token'] = token
        data['deviceId'] = deviceId
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/update-pwd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_update_pwd_forget_password(self, mobileRegion, mobile, newPassword, businessToken):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/update-pwd/forget-password')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['newPassword'] = newPassword
        data['businessToken'] = businessToken
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/update-pwd/forget-password', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_update_pwd_send(self, mobileRegion, mobile):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/update-pwd/send')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/update-pwd/send', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")

    def _web_sso_update_pwd_validate(self, mobileRegion, mobile, verifyCode):
        data = self.Sso.get('http://dev.sso.worldfarm.com').get('/web/sso/update-pwd/validate')
        data['_tk_'] = None
        data['_deviceId_'] = None
        data['mobileRegion'] = mobileRegion
        data['mobile'] = mobile
        data['verifyCode'] = verifyCode
        response = self.request.post(url='http://dev.sso.worldfarm.com/web/sso/update-pwd/validate', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            pass
        elif json_response["status"] == "ERROR":
            pass
        else:
            raise Exception("status未返回OK或ERROR")
