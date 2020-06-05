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
        #���������ļ��е�KEYֵ�������뱨��ͷ�ͱ���������޸ġ�
        #000450req=0:17:2:ACCOUNTNO;0:4:2:FROMNO;0:2:2:TRANTYPE;0:8:2:FROMDATE
        None
        
        #������ͷ
        self.SetHeaderValue("JYDM",         "000450")
        self.SetHeaderValue("BANCSRQ",      "20130726")
        #self.SetHeaderValue("FLAG2",       "2")   
        self.SetHeaderValue("FLAG1",        "0" )               # ��ͨ����
        #self.SetHeaderValue("FLAG1",       "2" )               # ��Ȩ����
        self.SetHeaderValue("ZDHM",         "000009")
        self.SetHeaderValue("ZGHM",         "2005039")   
        self.SetHeaderValue("XHXLSH",       "000000021")        # ������ˮ��
        #self.SetHeaderValue("WWXTGZH",      "12345678901234567890123456789029")   # ��Χ��ˮ��
        self.SetHeaderValue("WWXTGZH",       "55520131213000000000000%09ld"     %( int(random.random()*(10**9)) ))  #UUID  
        
        #�������� 
        self.SetBodyValue("CXZH",           "19913000008016100")
        #self.SetBodyValue("ZZHLB",         "CNY0")
        self.SetBodyValue("ZZHLB",          "    ")
        self.SetBodyValue("CH",             "001")
        self.SetBodyValue("XH",             "01")
        self.SetBodyValue("JYQSHM",         "0003")
        self.SetBodyValue("JYLX",           "01")

 
        

 
        
 
   

