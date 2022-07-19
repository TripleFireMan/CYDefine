# -*-coding:utf-8-*-
# !/usr/bin/env python
# encoding: utf-8
'''
@author: 成焱
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: ab364743113@126.com
@file: moveFileToXcode.python.py
@time: 2020/10/9 5:09 下午
@desc:
'''

import os
def test():
    # print("123")
    str = os.getcwd()
    print(str)

    print(os.getcwd())
    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.abspath('.'))
    print(os.path.abspath(os.path.join(os.getcwd(), "../")))


def  move_files():
    file_location_path = os.path.abspath(os.path.join(os.getcwd(), "../"))
    os.system("echo 'chengyan251' | sudo -S cp -R {0} /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/Xcode/Templates/File\ Templates/User\ Interface".format(file_location_path))

if __name__ == '__main__':
    move_files()
    # test()