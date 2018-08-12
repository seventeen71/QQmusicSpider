#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from download_song import *


def notice_format():
    """
    提示格式
    :return:
    """
    print("-+-"*15)
    print("python main.py 歌曲名")
    print("-+-"*15)


def main():
    # print(sys.argv)
    if len(sys.argv) != 2:
        print("输入指定格式：")
        notice_format()
        return

    else:
        qqmusic(sys.argv[1])


if __name__ == "__main__":
    main()
