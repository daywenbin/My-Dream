# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:51:16 2020

@author: Administrator
"""

import tushare as ts
print(ts.__version__)
df1 = ts.get_realtime_quotes('600745')
df1.columns
import talib 
import numpy
import talib
import sys
sys.path
