# encoding: utf-8


from utils.Config import Config
from utils.Util import Request
from utils.Log import Log


class ServiceAction(object):

    def __init__(self, employee, buyer_action=None):
        self.service = employee
        self.buyer_action = buyer_action
        self.log = Log('Customer')

    def service_send_auth_url(self, order_id):
        # 邀请上传资质(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/im-buyer/before-send-auth-url']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['orderId'] = order_id
        send_auth_url = Request().post(url='http://dev.trade.worldfarm.com/admin/im-buyer/before-send-auth-url',
                                       data=data)
        return send_auth_url

    def service_get_order_list(self, buyer_id):
        # 进入对话窗口调用-买家农场列表(返回为空)
        data_trade = Config('trade').data
        order_list_param = data_trade['http://dev.trade.worldfarm.com']['/admin/im-buyer/order-list']
        order_list_param['_tk_'] = self.service.token
        order_list_param['_deviceId_'] = self.service.device_id
        order_list_param['buyerId'] = buyer_id
        order_list = Request().post(url='http://dev.trade.worldfarm.com/admin/im-buyer/order-list',
                                    data=order_list_param)
        return order_list

    def service_see_buyer_detail(self, buyer_id):
        # 买家资料信息(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/im-buyer/buyer-detail']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['buyerId'] = buyer_id
        see_buyer_detail = Request().post(url='http://dev.trade.worldfarm.com/admin/im-buyer/buyer-detail', data=data)
        return see_buyer_detail

    def service_see_sub_detail(self, buyer_id):
        # 查看订阅规则(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/im-buyer/sub-detail']
        if data is None:
            data = {}
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['buyerId'] = buyer_id
        see_sub_detail = Request().post(url='http://dev.trade.worldfarm.com/admin/im-buyer/sub-detail', data=data)
        return see_sub_detail

    def service_buyer_resource_count(self):
        # 买家待审核条数(回测)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/cs/buyer-resource/pending-count']
        if data:
            pass
        else:
            data = {}
        data['status'] = 1
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        buyer_resource_count = Request().post(url='http://dev.trade.worldfarm.com'
                                                  '/admin/cs/buyer-resource/pending-count', data=data)
        print(buyer_resource_count)

    def service_buyer_resource_list(self, order_no, buyer_name):
        # 买家资料列表(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/cs/buyer-resource/list']
        data['status'] = 1
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['orderNo'] = order_no
        data['buyerName'] = buyer_name
        buyer_resource_list = Request().post(url='http://dev.trade.worldfarm.com/'
                                                 'admin/cs/buyer-resource/list', data=data)
        return buyer_resource_list

    def service_buyer_detail_resource_list(self, resource_id):
        # 买家资料详情资源列表()
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/cs/buyer-resource/detail-resource-list']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['id'] = resource_id
        detail_resource_list = Request().post(url='http://dev.trade.worldfarm.com'
                                                  '/admin/cs/buyer-resource/detail-resource-list', data=data)
        return detail_resource_list

    def service_buyer_resource_audit(self, resource_id, audit_type, reason):
        # 买家资料审核(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/cs/buyer-resource/audit']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['id'] = resource_id
        data['reason'] = reason
        data['type'] = audit_type
        # type=1表示通过,type=2表示不通过
        resource_audit = Request().post(url='http://dev.trade.worldfarm.com/admin/cs/buyer-resource/audit', data=data)
        return resource_audit

    def service_remark_add_user(self, remark, user_id):
        # 添加用户备注,返回备注ID(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/customer-service-remark/add-user']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['userId'] = user_id
        data['remark'] = remark
        remark_add_user = Request().post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/add-user',
                                         data=data)
        return remark_add_user

    def service_remark_add_farm(self, remark, title, order_id):
        # 添加农场备注,返回备注ID(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/customer-service-remark/add-farm']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['remark'] = remark
        data['title'] = title
        data['orderId'] = order_id
        remark_add_farm = Request().post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/add-farm',
                                         data=data)
        return remark_add_farm

    def service_remark_update_farm(self, service_remark_id, title, remark):
        # 修改农场备注
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/customer-service-remark/update-farm']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['Id'] = service_remark_id
        data['title'] = title
        data['remark'] = remark
        remark_update_farm = Request().post(url='http://dev.trade.worldfarm.com'
                                            '/admin/customer-service-remark/update-farm', data=data)
        return remark_update_farm

    def service_remark_update_user(self, user_remark_id, remark):
        # 修改用户备注
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/customer-service-remark/update-user']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['Id'] = user_remark_id
        data['remark'] = remark
        remark_update_user = Request().post(url='http://dev.trade.worldfarm.com'
                                            '/admin/customer-service-remark/update-user', data=data)
        return remark_update_user

    def service_remark_farm_list(self, farm_id, buyer_id):
        # 农场备注列表(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/customer-service-remark/farm-list']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['buyerId'] = buyer_id
        data['farmId'] = farm_id
        remark_farm_list = Request().post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/farm-list',
                                          data=data)
        return remark_farm_list

    def service_remark_user_list(self, user_id):
        # 用户备注列表(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/customer-service-remark/user-list']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['userId'] = user_id
        remark_farm_list = Request().post(url='http://dev.trade.worldfarm.com/admin/customer-service-remark/user-list',
                                          data=data)
        return remark_farm_list

    def service_farm_im_list(self, seller_agency_id):
        # 联系卖家中介-农场列表(通过)
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/farm/im-list']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['sellerAgencyId'] = seller_agency_id
        farm_im_list = Request().post(url='http://dev.trade.worldfarm.com/admin/farm/im-list', data=data)
        return farm_im_list

    def service_seller_agency_detail(self, seller_agent_id):
        # 卖家中介信息(通过 )
        data = Config('trade').data['http://dev.trade.worldfarm.com']['/admin/seller-agency/detail']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['sellerAgencyId'] = seller_agent_id
        seller_agency_detail = Request().post(url='http://dev.trade.worldfarm.com/admin/seller-agency/detail',
                                              data=data)
        return seller_agency_detail

    def service_im_account(self):
        # 登录IM,获取账号IM信息-failed
        data = Config('ms').data['http://dev.ms.worldfarm.com']['/admin/im-auth/get/im-account/service']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        im_auth_account = Request().post(url='http://dev.ms.worldfarm.com/admin/im-auth/get/im-account/service',
                                         data=data)
        return im_auth_account

    def service_get_acc_id(self, user_id):
        # 客服通过聊天获取对方IM账号-failed
        data = Config('ms').data['http://dev.ms.worldfarm.com']['/admin/im-auth/service-get/accid']
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        data['userId'] = user_id
        get_acc_id = Request().post(url='http://dev.ms.worldfarm.com/admin/im-auth/service-get/accid',
                                    data=data)
        return get_acc_id

    def service_gather_farm_publish(self, farm_id, farm_name, farm_name_en, farm_type, total_price, unit_code, area_range,
                                    area_code, unit_price, address, address_en, lat, lng, content, content_en, soil_ph,
                                    soil_type, water_rights, water_rights_en, regulations, regulations_en, disadvantage,
                                    disadvantage_en, rainfall, img_list, nation_id, province_id, city_id):
        data = {}
        data['id'] = farm_id
        data['farmName'] = farm_name
        data['farmNameEn'] = farm_name_en
        data['type'] = farm_type
        data['totalPrice'] = total_price
        data['unitCode'] = unit_code
        data['area'] = area_range
        data['areaCode'] = area_code
        data['unitPrice'] = unit_price
        data['address'] = address
        data['addressEn'] = address_en
        data['lat'] = lat
        data['lng'] = lng
        data['content'] = content
        data['contentEn'] = content_en
        data['soilPh'] = soil_ph
        data['soilType'] = soil_type
        data['waterRights'] = water_rights
        data['waterRightsEn'] = water_rights_en
        data['regulations'] = regulations
        data['regulationsEn'] = regulations_en
        data['disadvantage'] = disadvantage
        data['disadvantageEn'] = disadvantage_en
        data['rainfall'] = rainfall
        data['imgList'] = img_list
        data['nationId'] = nation_id
        data['provinceId'] = province_id
        data['cityId'] = city_id
        data['_tk_'] = self.service.token
        data['_deviceId_'] = self.service.device_id
        Request().post(url="http://dev.trade.worldfarm.com/admin/farm/gather-farm-publish",
                       data=data)

    # def /admin/farm/translate-list


if __name__ == '__main__':
    from backend.Employee import Employee
    from backend.Farm import Farm
    service = Employee(100051, 123456)
    sa = ServiceAction(service)
    fm = Farm()
    sa.service_gather_farm_publish(6773, fm.farm_name, fm.farm_name_en, fm.farm_type, fm.total_price, fm.unitCode, fm.area,
                                   fm.area_code, fm.unit_price, fm.farm_address, fm.farm_address_en, fm.lat, fm.lng,
                                   fm.content, fm.content_en, fm.soil_ph, fm.soil_type, fm.water_rights,
                                   fm.water_rights_en, fm.regulations, fm.regulations_en, fm.disadvantage,
                                   fm.disadvantage_en, fm.rainfall, fm.images, fm.nation_id, fm.province_id, fm.city_id)
