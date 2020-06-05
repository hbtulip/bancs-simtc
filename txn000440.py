#! /usr/bin/python
# -*- coding: gbk -*-
'''
    @ Project : simtc
    @ File Name : txn000440.py
    @ Date : 2013/12/10
    @ Author : disp
'''
import random
from txnbase import TxnBase

class Txn000440(TxnBase):

    def __init__(self):
        self.LoadCfgFile(440)
        self.m_msgtext = " 1355                    **            00300002007000200700044000000000000000000 02  0 00020011                                13                       02910113000008016704    0000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 0000000000000000000000 00000000000000000                "
       
    def Options(self):
        #根据配置文件中的KEY值，对输入报文头和报文体进行修改。
        None
        
        #请求报文头
        self.SetHeaderValue("FLAG1",    "0")                #0-正常交易 2-授权交易
        self.SetHeaderValue("FLAG2",    "2")                #默认单包      
        self.SetHeaderValue("YHDM",     "003")              #机构号
        self.SetHeaderValue("GYH",      "2005039")          #柜员号  
        self.SetHeaderValue("BANCSRQ",  "20130726")         #日期         
        #self.SetHeaderValue("WWXTGZH",  "33320131213000000000000000001002")                                    #UUID
        #self.SetHeaderValue("WWXTGZH",  "333201312130000000000000000%05d"  %(random.randint(1,60000)))         #UUID 
        self.SetHeaderValue("WWXTGZH",   "33320131213000000000000%09ld"     %( int(random.random()*(10**9)) ))  #UUID  
        
        #请求报文体 
        self.SetBodyValue("CXZH",    "199130000080161aX")   #查询账号 1991300000801614

        #self.SetBodyValue("ZZHLX",  "CNY0")                #子账户类型
        #self.SetBodyValue("CH",     "5506")                #册号
        #self.SetBodyValue("XH",     "0611")                #序号   
        

 
        
 
   

