#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import sys
import requests


from urllib import parse

from CONFIG import *


def get_one_html(url):
    """
    根据url下载对应网页内容，这里是JSON数据
    :param url:
    :return:
    """
    try:
        response = requests.get(url=url, headers=HEADERS)
        response.raise_for_status()
    except:
        return None

    else:
        return response.text

def extract_albummid(data):
    """
    用于提取albummid
    :param data:
    :return:
    """
    result = re.search(r'"mid":"(\w+?)"', data)
    if result:
        return result.group(1)
    else:
        return None

def extract_songmid(data):
    """
    1. 用于提取songid
    2. 用于提取歌手名字
    :param data:
    :return:
    """
    global SONGNAME
    global SINGER

    SINGER = re.search(r'"singername":"(.+?)"', data).group(1)
    results = re.findall(r'"songmid":"(\w+?)","songname":"(.+?)"', data)

    print("【歌曲名字：{songname}】".format(songname=SONGNAME))
    print("【歌手名字：{singer}】".format(singer=SINGER))

    if results:
        for result in results:
            if SONGNAME in result:
                return result[0]
        else:
            return None
    else:
        return None

def extract_vkey(data):
    """
    用于提取vkey
    :param data:
    :return:
    """
    result = re.search(r'"vkey":"(\w+?)"', data)
    if result:
        return result.group(1)
    else:
        return None
