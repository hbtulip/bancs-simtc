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
        #���������ļ��е�KEYֵ�������뱨��ͷ�ͱ���������޸ġ�
        None
        
        #������ͷ
        self.SetHeaderValue("FLAG1",    "0")                #0-�������� 2-��Ȩ����
        self.SetHeaderValue("FLAG2",    "2")                #Ĭ�ϵ���      
        self.SetHeaderValue("YHDM",     "003")              #������
        self.SetHeaderValue("GYH",      "2005039")          #��Ա��  
        self.SetHeaderValue("BANCSRQ",  "20130726")         #����         
        #self.SetHeaderValue("WWXTGZH",  "33320131213000000000000000001002")                                    #UUID
        #self.SetHeaderValue("WWXTGZH",  "333201312130000000000000000%05d"  %(random.randint(1,60000)))         #UUID 
        self.SetHeaderValue("WWXTGZH",   "33320131213000000000000%09ld"     %( int(random.random()*(10**9)) ))  #UUID  
        
        #�������� 
        self.SetBodyValue("CXZH",    "199130000080161aX")   #��ѯ�˺� 1991300000801614

        #self.SetBodyValue("ZZHLX",  "CNY0")                #���˻�����
        #self.SetBodyValue("CH",     "5506")                #���
        #self.SetBodyValue("XH",     "0611")                #���   
        

 
        
 
   

