#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 4:34 PM
# @Author  : Yongchin

import pytest
import os
import sys

if __name__ == '__main__':
    args = ['./', '-q', '--report', 'result/report.html']
    # args = ['./', '-q', '--alluredir', './report']
    pytest.main(args)
