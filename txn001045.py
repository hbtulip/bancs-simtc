#! /usr/bin/python
# -*- coding: gbk -*-
'''
    @ Project : simtc
    @ File Name : txn001045.py
    @ Date : 2013/12/10
    @ Author : disp
'''
import random
from txnbase import TxnBase

class Txn001045(TxnBase):

    def __init__(self):
        self.LoadCfgFile(1045)
        self.m_msgtext = " 1355                    **            00320005039200500100104500000000000000000 0   0 00000002                                13                       05713                       12219913500008016708                  00000000000100000+            19913000008016146    0000                                                              CNY00000000000100000+CNY00000000000100000+00000000000000000+00000000000000000+0100IV           01                                                                                                                                                                                                                                                                                                                 00000                                        00000000                                                  CNY0550210010000 00000                                               90011                   6      00000000                                                                             99999900000+    R                                                            N02    00IV0100000100000000010000000000                                                                                                                                  00IV                         CNY05502100100000000000000 00000000000000000                "
       
    def Options(self):
        #根据配置文件中的KEY值，对输入报文头和报文体进行修改。
        #001045req="0:2:2:SDM;0:23:1:ZCJZH;2:3:2:JZHPYW1:057;0:2:2:SDMZRF;0:23:1:ZRJZH;2:3:2:JZHPYW2:122;0:17:2:ZCZH;0:18:1:FILLER1;8:18:2:ZCJE:00000000000000000+;0:10:1:FILLER2;8:2:1:TSM:NF;0:17:2:ZRZH;0:2:1:FILLER3;0:2:1:BQXTS;0:2:2:YCJXTS;0:2:2:JJYCJXTS;0:62:1:FILLER4;8:3:1:ZCBZ:CNY;8:18:2:DHJE:00000000000000000+;8:3:1:ZRBZ:CNY;8:18:2:BBJE:00000000000000000+;8:18:2:YJ:00000000000000000+;8:18:2:ZL:00000000000000000+;8:2:2:HLLX1:01;0:4:1:HBBB;0:11:1:FILLER5;8:2:2:HLLX2:01;0:94:1:FILLER6;0:2:1:ZJLX;0:32:1:ZJHM;0:16:1:MM1;0:161:1:FILLER7;0:3:2:ZCCH;0:2:2:ZCXH;0:22:1:FILLER8;0:8:2:YQCRQ;0:9:2:YQCLSH;0:1:1:QTZQBZ;0:8:2:DQDQR;0:50:1:DZDZY;0:4:1:ZCZZHLX;0:4:2:CPLX;0:4:2:CPZL;0:4:2:CQ;0:1:1:JQ;0:3:2:ZRCH;0:2:2:CRXH;0:47:1:FILLER9;0:4:2:PZLX;0:20:1:PZHM;0:1:2:ZFFS;0:6:1:MM;0:8:2:PZQFRQ;0:76:1:FILLER10;0:1:1:HLLX;8:6:2:YJLL:999999;8:6:2:LLJJD:00000+;0:4:1:FCLLZB;8:1:1:DQXCLX:R;0:22:1:FILLER11;0:19:1:ZCJJKH;0:19:1:ZRJJKH;8:1:1:ZFMMCGBZ:N;2:2:2:JZHBS:02;0:4:1:FILLERX;0:4:1:WB_HBBB2;0:2:2:WB_HLLX;0:10:2:WB_ZHHL;0:10:2:WB_DHHL;0:6:2:WB_JSHTJM;0:60:1:WB_GHDW;0:20:1:WB_GHYY;0:20:1:WB_TGPJMC;0:30:1:WB_PZDWMC;0:4:1:WB_HBBB1"
        None
        
        #请求报文头
        self.SetHeaderValue("JYDM",  "001045")
        self.SetHeaderValue("FLAG1",  "0" )    # 0-普通交易 2-授权交易

        self.SetHeaderValue("GYH",  "2005001")   # 柜员号
        self.SetHeaderValue("ZDHM",  "000009")
        self.SetHeaderValue("JYDM",  "001045")
        self.SetHeaderValue("FLAG2",  "2")
        self.SetHeaderValue("FLAG3",  "0")
        self.SetHeaderValue("BANCSRQ",  "20140317")   
        self.SetHeaderValue("ZGHM",  "2005039")    #授权柜员
        self.SetHeaderValue("XHXLSH",  "000000020")   # 核心流水号
#       self.SetHeaderValue("WWXTGZH",  "12345678901234567891123456789030")   # 外围流水号
        self.SetHeaderValue("WWXTGZH",  "12345678901234567891123%09ld"     %( int(random.random()*(10**9)) ))  #UUID  

        #请求报文体 
        self.SetBodyValue("ZRZH",  "19913500008016775")
#       self.SetBodyValue("ZRZH",  "19913500008011234")
        self.SetBodyValue("ZCZH",  "19913500008016701" )   
        self.SetBodyValue("ZCJE",  "00000000000000020+" )   # 交易金额
        self.SetBodyValue("ZCZZHLX",  "CNY0")
        self.SetBodyValue("CPLX",  "5502")
        self.SetBodyValue("CPZL",  "1001")
        self.SetBodyValue("ZRZZHLX",  "CNY0")
        self.SetBodyValue("ZCCH",  "   ")
        self.SetBodyValue("ZCXH",  "  ")
        self.SetBodyValue("ZRCH",  "   ")
        self.SetBodyValue("ZRXH",  "  ")
        self.SetBodyValue("ZFFS",  "A"  )  # 证件支取
        self.SetBodyValue("ZJLX",  "01"  )  
        self.SetBodyValue("ZJHM",  "430105198212131525              " )  
        self.SetBodyValue("PZLX",  "0001" )           

#       self.SetBodyValue("ZFFS",  "9" )   # 强制扣划
#       self.SetBodyValue("ZFFS",  "8"  )  # 一票一密

        
 
   

