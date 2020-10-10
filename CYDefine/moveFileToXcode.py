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

def  move_files():
    os.system("echo 'chengyan251' | sudo -S cp -R /Users/chengyan/Documents/Defines/CYDefine /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/Xcode/Templates/File\ Templates/User\ Interface")

if __name__ == '__main__':
    move_files()