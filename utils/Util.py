#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/3/28'
"""


import requests
import pymysql
import redis
import json
import datetime
import decimal
import subprocess
import platform
import re
import mimetypes
from utils.Log import Log
from time import sleep
import urllib


class Request(object):
    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
               "Accept": "application/json",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/68.0.3440.106 Safari/537.36"
               }
    L = Log("Request")

    @staticmethod
    def url_encode(string):
        cn = ''
        for ch in string.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                cn += urllib.quote(ch.encode('utf-8'))
            else:
                cn += ch.encode('utf-8')
        return cn

    def post(self, url, data):
        client = requests.session()
        response = client.post(url=url, data=data, headers=self.headers, cookies=None).content
        self.L.logger.debug('''
                               request: %s,
                               data: %s,
                               response: %s
                            ''' % (url, data, response.decode("utf-8")))
        try:
            response_json = json.loads(response)
            self.L.logger.debug("\n" + json.dumps(response_json, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
        except ValueError:
            self.L.logger.debug(response)
        return response.decode("utf-8")

    def get(self, url):
        client = requests.session()
        response = client.get(url=url, headers=self.headers).content
        try:
            self.L.logger.debug('''
                                   request: %s,
                                   response: %s
                                ''' % (url, response.decode("utf-8")))
            response_json = json.loads(response.decode("utf-8"))
            self.L.logger.debug("\n" + json.dumps(response_json, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
        except ValueError:
            self.L.logger.debug(response)
        return response.decode("utf-8")

    def post_file(self, url, file_path, data_dict=None):
        file_name = file_path.split("/")[-1:][0]
        file_bin_data = open(file_path, 'rb')
        content_type = str(mimetypes.types_map.get("." + file_path.split(".")[-1:][0], None))
        files = {'file': (file_name, file_bin_data, content_type)}
        response = requests.post(url=url, data=data_dict, files=files).content
        self.L.logger.debug('''
                               request: %s,
                               file: %s,
                               response: %s
                            ''' % (url, file_path, response.decode("utf-8")))
        try:
            response_json = json.loads(response)
            self.L.logger.debug("\n" + json.dumps(response_json, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
        except ValueError:
            self.L.logger.debug(response)
        return response.decode("utf-8")


class DataBaseOperate(object):
    L = Log("DataBaseOperate")

    def operate(self, host_ip, database_name, sql):
        if host_ip == "39.104.28.40":
            user, password, port = "root", "YYJNo$QsaaSjgb8U3JoigB", 3306
        elif host_ip == "47.74.129.65":
            user, password, port = "farm_test", "r2rublBL4qJMc", 3306
        elif host_ip == "67.218.159.111":
            user, password, port = "root", "Knight01", 3306
        else:
            raise Exception('数据库IP地址错误: %s' % host_ip)
        try:
            db = pymysql.connect(host=host_ip,
                                 port=port,
                                 user=user,
                                 db=database_name,
                                 passwd=password)
            con = db.cursor(cursor=pymysql.cursors.DictCursor)
            con.execute(sql)
            results = con.fetchall()
            # print(results)
            for result in results:
                for fields in result:
                    if isinstance(result[fields], datetime.datetime):
                        result[fields] = str(result[fields].strftime('%Y-%m-%d %H:%M:%S'))
                    elif isinstance(result[fields], datetime.date):
                        result[fields] = str(result[fields].strftime('%Y-%m-%d'))
                    elif isinstance(result[fields], decimal.Decimal):
                        result[fields] = float(result[fields])
            db.commit()
            con.close()
            # print(results)
            self.L.logger.debug("\n" + json.dumps(results, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
            return results
        except Exception as e:
            self.L.logger.error(e)


class Redis(object):
    L = Log("Redis")
    pool = redis.ConnectionPool(host='67.218.159.111', port=6699, db=7, password='Knight01')
    r = redis.Redis(connection_pool=pool)

    def set(self, key, value):
        self.r.set(key, value)
        self.L.logger.debug('Set %s = %s' % (str(key), str(value)))

    def get(self, key):
        value = self.r.get(key)
        self.L.logger.debug('Get %s = %s' % (str(key), str(value)))
        return value.decode()

    def delete(self, key):
        self.r.delete(key)
        self.L.logger.debug('Delete %s' % str(key))

    def exists(self, key):
        exist = self.r.exists(key)
        self.L.logger.debug('exist? %s' % str(exist))
        return exist


class AndroidTool(object):
    from uiautomator import device as u
    d = u
    L = Log("AndroidTool")

    @staticmethod
    def run_command(shell_command):
        handle = subprocess.Popen(shell_command, stdout=subprocess.PIPE, shell=True)
        value = handle.stdout.read().decode("utf-8")
        return value

    def reset_app(self, package_name):
        status = self.run_command("adb shell pm clear %s" % package_name)
        if status == "Success":
            self.L.logger.debug(u"初始化管理版 %s" % status)
            return True
        else:
            self.L.logger.debug(u"初始化管理版 %s" % status)
            return False

    def get_device(self):
        if self.run_command("adb devices") == "List of devices attached\n\n":
            self.L.logger.debug("No Android Device Connected, Please Connect One")
            return False
        else:
            return True

    @staticmethod
    def get_info(shell_command):
        handle = subprocess.Popen(shell_command, stdout=subprocess.PIPE, shell=True)
        response = handle.stdout.read().decode("utf-8")
        if response:
            if platform.system() == "Windows":
                return response.split(":")[1][1:-3]
            elif platform.system() == "Darwin":
                return response.split(":")[1][1:-2]
        else:
            return 'unknown'

    def get_brand(self):
        # 手机品牌
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.product.brand"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.product.brand"')

    def get_model(self):
        # 手机型号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.product.model"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.product.model"')

    def get_android_version(self):
        # Android版本号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.build.version.release"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.build.version.release"')

    def get_sdk_version(self):
        # SDK版本号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.build.version.sdk"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.build.version.sdk"')

    def get_manufacturer(self):
        # 手机制造商
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.product.manufacturer"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.product.manufacturer"')

    def get_sn(self):
        # 序列号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.serialno"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "persist.sys.product.serialno"')

    def get_device_name(self):
        # 设备号
        if platform.system() == "Windows":
            return self.get_info('adb shell getprop | findstr "ro.serialno"')
        elif platform.system() == "Darwin":
            return self.get_info('adb shell getprop | grep "ro.serialno"')

    def get_resolution(self):
        # 设备分辨率
        # adb shell dumpsys window displays | head -n 3
        if platform.system() == "Windows":
            return self.run_command('adb shell dumpsys window displays | findstr "init"').split(" ")[4][5:]
        elif platform.system() == "Darwin":
            return self.run_command('adb shell dumpsys window displays | grep "init" | head -n 3').split(" ")[4][5:]
        # return self.getInfo('adb shell wm size') #仅适用于高通平台

    def get_cpu(self):
        # 处理器
        if platform.system() == "Windows":
            return self.get_info('adb shell cat /proc/cpuinfo | findstr "Processor"')[:-12]
        elif platform.system() == "Darwin":
            return self.get_info('adb shell cat /proc/cpuinfo | grep "Processor"')

    def get_device_info(self):
        return ("%s_[%s]_%s_%s_%s" % (
            self.get_model(), self.get_resolution()[:-1], self.get_android_version(),
            self.get_sdk_version()[:-1], self.get_cpu()))

    def set_unicode_ime(self):
        adb_return = self.run_command("adb shell ime list -a")
        ime_list = re.findall('.*/.*:', str(adb_return))
        try:
            unicode_index = ime_list.index('io.appium.android.ime/.UnicodeIME:')
            set_ime_return = self.run_command("adb shell ime set %s" % ime_list[unicode_index][:-1])
            self.L.logger.debug(set_ime_return)
            self.L.logger.debug(u"unicode输入法 已设置")
        except ValueError:
            self.L.logger.debug(u"未安装 unicode输入法")
            install_return = self.run_command("adb install -r ./unicode_keyboard.apk")
            self.L.logger.debug(install_return)
            self.L.logger.debug(u"unicode输入法 已安装")
            adb_return = self.run_command("adb shell ime list -a")
            ime_list = re.findall('.*/.*:', str(adb_return))
            unicode_index = ime_list.index('io.appium.android.ime/.UnicodeIME:')
            set_ime_return = self.run_command("adb shell ime set %s" % ime_list[unicode_index][:-1])
            self.L.logger.debug(set_ime_return)
            self.L.logger.debug(u"unicode输入法 已设置")

    def reset_ime(self):
        set_ime_return = self.run_command("adb shell ime set %s" % "com.sohu.inputmethod.sogou.xiaomi/.SogouIME")
        self.L.logger.debug(set_ime_return)
        self.L.logger.debug(u"输入法 已恢复")

    def set_up_admin(self):
        self.L.logger.info(u"测试设备: " + self.get_device_info())
        self.set_unicode_ime()
        self.reset_app("com.wuliuqq.client")
        sleep(3)
        self.d.freeze_rotation(False)
        self.d.screen.on()
        self.d.press.home()
        self.d(text=u"管理版").click()
        self.L.logger.info(u"测试开始, 启动管理版")

    def tear_down_admin(self):
        self.reset_ime()
        self.reset_app("com.wuliuqq.client")
        self.L.logger.info(u"测试完成, 清理测试")

    def enter_new_truck_page(self, login_mobile, verify_code):
        sleep(2)
        if self.d(text="允许").exists:
            self.d(text="允许").click()
        self.d(resourceId="com.wuliuqq.client:id/et_account").set_text(str(login_mobile))
        self.d(resourceId="com.wuliuqq.client:id/et_password").set_text(str(verify_code))
        self.d(resourceId="com.wuliuqq.client:id/btn_login").click()
        sleep(2)
        self.L.logger.info(u"管理版 %s 登录成功" % str(login_mobile))
        self.d(text=u"确定").click()
        self.d(text=u"车后服务").click()
        self.d(text=u"新车业务").click()
        self.L.logger.info(u"进入 新车业务")


# if __name__ == '__main__':
#     dbOperate = DataBaseOperate()
#     query = dbOperate.operate("39.104.28.40", "farm-uc",
#                               'SELECT * FROM t_user WHERE mobile = "18602832572";')

