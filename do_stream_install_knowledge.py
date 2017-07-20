#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: do_stream_install_knowledge.py
@time: 2017/07/20/22:11
"""

import urlparse
import os
#urlparse 该模块主要是用来切割url中的各个部分

#
# url = "http://192.168.5.30:8088/jenkins/view/%E5%B9%B3%E5%8F%B0%E4%BA%A7%E5%93%81%E7%BA%BF/job/build_platform_fsp_stream/lastSuccessfulBuild/artifact/fsp-sss-stream-1.0.0.1.tar.gz"
#
# parts = urlparse.urlparse(url)
# # import pdb
# # pdb.set_trace()
#
# print parts

uncompress_destdir = "/tmp"
print os.chdir("{0}".format(uncompress_destdir))