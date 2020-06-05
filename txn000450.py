#! /usr/bin/python
# -*- coding: gbk -*-
'''
    @ Project : simtc
    @ File Name : txn000450.py
    @ Date : 2013/12/10
    @ Author : disp
'''

import random
from txnbase import TxnBase

class Txn000450(TxnBase):

    def __init__(self):
        self.LoadCfgFile(450)
        self.m_msgtext = " 1355                    **            00320005039200503900045000000000000000000 02  0 20050011                                13                       02910113500008016459    00000000000000000000000000000000000000000000+000000000000000000000000000000000000000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 0000000000000000000000 00000000000000000                "
       
    def Options(self):
        #根据配置文件中的KEY值，对输入报文头和报文体进行修改。
        #000450req=0:17:2:ACCOUNTNO;0:4:2:FROMNO;0:2:2:TRANTYPE;0:8:2:FROMDATE
        None
        
        #请求报文头
        self.SetHeaderValue("JYDM",         "000450")
        self.SetHeaderValue("BANCSRQ",      "20130726")
        #self.SetHeaderValue("FLAG2",       "2")   
        self.SetHeaderValue("FLAG1",        "0" )               # 普通交易
        #self.SetHeaderValue("FLAG1",       "2" )               # 授权交易
        self.SetHeaderValue("ZDHM",         "000009")
        self.SetHeaderValue("ZGHM",         "2005039")   
        self.SetHeaderValue("XHXLSH",       "000000021")        # 核心流水号
        #self.SetHeaderValue("WWXTGZH",      "12345678901234567890123456789029")   # 外围流水号
        self.SetHeaderValue("WWXTGZH",       "55520131213000000000000%09ld"     %( int(random.random()*(10**9)) ))  #UUID  
        
        #请求报文体 
        self.SetBodyValue("CXZH",           "19913000008016100")
        #self.SetBodyValue("ZZHLB",         "CNY0")
        self.SetBodyValue("ZZHLB",          "    ")
        self.SetBodyValue("CH",             "001")
        self.SetBodyValue("XH",             "01")
        self.SetBodyValue("JYQSHM",         "0003")
        self.SetBodyValue("JYLX",           "01")

 
        

 
        
 
   

