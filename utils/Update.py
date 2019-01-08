#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/11'
"""

from utils.Log import Log
import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from utils.Util import Request
import os
import json
import codecs
import time


L = Log('Update')
hosts = ['http://39.104.28.40:9600']


def get_paths(host_name):
    json_content = Request().get(str(host_name) + '/v2/api-docs')
    paths = json.loads(json_content)["paths"]
    path_detail_list = []
    for p in paths:
        para_desc_list = []
        try:
            desc = paths[p]["post"].get("tags", [])[0]
            para_desc_list.append(desc)
            # L.logger.debug("{'%s': '%s'}" % (p, desc))
            paras = paths[p]["post"].get("parameters", [])
        except KeyError:
            desc = paths[p]["get"].get("tags", [])[0]
            para_desc_list.append(desc)
            # L.logger.debug("{'%s': '%s'}" % (p, desc))
            paras = paths[p]["get"].get("parameters", [])
        if paras is None:
            pass
        else:
            p_dict = {}
            for para in paras:
                p_dict[para['name']] = u"%s_%s_%s" % (para.get('type', 'noType'),
                                                      para.get('required', 'noRequired'),
                                                      para.get('description', 'noDescription'))
        para_desc_list.append(p_dict)
        path_detail_list.append({p: para_desc_list})
    # demand_list = sorted(path_detail_list)
    now = time.strftime("_%Y-%m-%d_%H%M%S", time.localtime())
    # L.logger.debug(path_detail_list)
    current_path = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(current_path + "/Docs"):
        os.makedirs(current_path + "/Docs")
    with codecs.open('./Docs/' + str(host_name).split(".")[1] + now + '.yaml', 'a', 'utf-8') as f:
        f.write(host_name + ':\n')
        for item in path_detail_list:
            for k, v in item.items():
                if isinstance(v[1], dict):
                    f.write('  %s:\n' % k)
                    for x, y in v[1].items():
                        f.write('    %s:\n' % x)
    with codecs.open('./Docs/' + str(host_name).split(".")[1] + now + '.txt', 'a', 'utf-8') as f:
        f.write(host_name + '\n')
        for item in path_detail_list:
            for k, v in item.items():
                if isinstance(v[1], dict):
                    f.write('\n  %s, %s\n' % (k, v[0]))
                    for x, y in v[1].items():
                        f.write('    %s, %s\n' % (x, y))


def get_geo_info_from_aus():
    cities = ["Hobart, Tasmania", "Smithton, Tasmania"]
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    geo_locator = Nominatim(user_agent="farm_test", scheme='http')
    for city_name in cities:
        print("\n  - " + city_name + ":")
        try:
            location = geo_locator.geocode(city_name, timeout=20, language="en")
            print("      state:\n    " + "    285")
            print("      city:\n    " + "    3538")
            print("      address:\n        " + str(location.address))
            lat = location.latitude
            print("      lat:\n        " + str(lat))
            lng = location.longitude
            print("      lng:\n        " + str(lng))
        except GeocoderTimedOut as e:
            print("Error: geocode failed on input %s with message %s" % (city_name, e))


if __name__ == '__main__':
    for p in hosts:
        get_paths(p)
    get_geo_info_from_aus()
