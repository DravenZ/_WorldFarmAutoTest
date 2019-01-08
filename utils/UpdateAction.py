# encoding: utf-8

"""
__author__ = Zhang Pengfei
__date__ = 2018/10/18
"""
import os
from utils.Config import Config


class UpdateAction(object):

    def get_file_list(self, path=None):
        """
        :param path: 获取文件的文件路径
        :return: 返回该路径下所有筛选出来的文件列表
        """
        file_list = []
        if path is None:
            path = os.path.dirname(os.path.realpath(__file__))  # 设置路径
        dirs = os.listdir(path)  # 获取指定路径下的文件
        for i in dirs:  # 循环读取路径下的文件并筛选输出
            if os.path.splitext(i)[1] == ".yaml":  # 筛选yaml文件
                file_list.append(i)
        return file_list

    def create_action(self, filename):
        """
        :param filename: 文件名不能全为数字
        :return:
        """
        try:
            int(filename.split(".")[0])
        except Exception:
            file_data = Config(filename.split(".")[0]).data
            for key, value in file_data.items():
                url = key
                data = value
                if data is not None and isinstance(data, dict):
                    with open("../actions/" + filename.split(".")[0].capitalize()+"Action.py", "w", encoding='utf-8') as f:
                        f.writelines("# encoding: utf-8\n\nfrom utils.Config import Config\n"
                                     "from utils.Util import Request\nfrom backend.Tool import Tool\n"
                                     "from utils.Log import Log\nimport json\n\n")
                        f.write("class "+filename.split(".")[0]+"Action(object):\n\n")
                        f.write("    def __init__(self, %s):\n" % filename.split(".")[0])
                        f.write("        self.log = Log('%s')\n" % filename.split(".")[0])
                        f.write("        self.request = Request()\n")
                        f.write("        self.%s = %s\n" % (filename.split(".")[0], filename.split(".")[0]))
                        for key, value in data.items():
                            fun_name = key.replace("/", "_").replace("-", "_")
                            fun_data = "\n    def %s(self" % fun_name
                            if value is not None:
                                paramlist = list(value.keys())
                                for param in paramlist:
                                    fun_data += ", " + param
                            fun_data += "):\n"
                            fun_data += "        data = self.%s.get('%s').get('%s')\n" % (filename.split(".")[0], url, key)
                            fun_data += "        data['_tk_'] = None\n"
                            fun_data += "        data['_deviceId_'] = None\n"
                            if value is not None:
                                paramlist = list(value.keys())
                                for param in paramlist:
                                    fun_data += "        data['%s'] = %s\n" % (param, param)
                            fun_data += "        response = self.request.post(url='%s', data=data)\n" % (url+key)
                            fun_data += "        json_response = json.loads(response)\n"
                            fun_data += "        if json_response[\"status\"] == \"OK\":\n"
                            fun_data += "            pass\n"
                            fun_data += "        elif json_response[\"status\"] == \"ERROR\":\n"
                            fun_data += "            pass\n"
                            fun_data += "        else:\n            raise Exception(\"status未返回OK或ERROR\")\n"
                            f.write(fun_data)


if __name__ == '__main__':
    updateaction = UpdateAction()
    file_list = updateaction.get_file_list()
    for filename in file_list:
        try:
            updateaction.create_action(filename)
        except AttributeError as e:
            print(e)
        except BaseException as be:
            print(be)
