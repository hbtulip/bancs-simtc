#! /usr/bin/python
# -*- coding: gbk -*-
'''
    @ Project : simtc
    @ File Name : txnbase.py
    @ Date : 2013/12/10
    @ Author : disp
'''

class TxnBase:

    m_cfg_header        = ""
    m_cfg_body          = ""
    m_msgtext           = ""   
    m_inheaddict_value  = {}
    m_reqdict_value     = {}  
    m_nTcode            = 0
    
    def __init__(self):
        m_inheaddict_value  = {}
        m_reqdict_value     = {}      
        
    def SetHeaderValue(self,key,value):
        self.m_inheaddict_value[key] = value
        
    def SetBodyValue(self,key,value):
        self.m_reqdict_value[key] = value   

    def LoadCfgFile(self,nTcode):
        self.m_nTcode = nTcode
        fileCfg = open('./ncbsmsgfix_bancs.cfg','r')
        
        sFlag = "IN_HEAD="
        while True:
            sLine = fileCfg.readline()
            if not sLine: break
            if sLine.find(sFlag) == 0:
                sLine = sLine.strip('\n')               #删除换行符
                self.m_cfg_header = sLine[len(sFlag):]
                break;
                
        sFlag = "%06dreq="%(nTcode)
        while True:
            sLine = fileCfg.readline()
            if not sLine: break
            if sLine.find(sFlag) == 0:
                sLine = sLine.strip('\n')               #删除换行符
                self.m_cfg_body = sLine[len(sFlag):]
                break;
        
        fileCfg.close()                      
        
    def GetTcode(self):
        return self.m_nTcode    
        
    def Options(self):
        print("TxnBase.Options")
    
    def MakeMsg(self):
        inheadlist = self.m_cfg_header.split(';')
        inheadlist_key = []
        inheaddict_valuelen = {}
        inheaddict_value = self.m_inheaddict_value  #引用地址
        
        for x in range(len(inheadlist)):
            tmp = inheadlist[x].split(':')
            inheadlist_key.append(tmp[3])
            inheaddict_valuelen[tmp[3]]=tmp[1]

       
        reqlist = self.m_cfg_body.split(';')
        reqlist_key = []
        reqdict_valuelen = {}
        reqdict_value = self.m_reqdict_value        #引用地址
        
        for x in range(len(reqlist)):
            #print("list[%d]: %s" %(x,reqlist[x]))
            tmp = reqlist[x].split(':')
            #for y in range(0,4):
            #    print("y[%d]: %s" %(y,tmp[y]))
            reqlist_key.append(tmp[3])
            reqdict_valuelen[tmp[3]]=tmp[1]
            

        sTcpHeader = self.m_msgtext[0:5];
        #print("TCPHEADER: %s" %sTcpHeader);
        
        nPos = 0   
        sMsgTmp = self.m_msgtext[5:]
        for m in range(len(inheadlist_key)):
            nLen = int(inheaddict_valuelen[inheadlist_key[m]])
            sValue = sMsgTmp[ nPos : nPos+nLen ]
            #print("[O] %s: %s" %(inheadlist_key[m],sValue) )
            inheaddict_value[inheadlist_key[m]]=sValue
            nPos +=  nLen
             
        #print("nPos=%d" %nPos)    #122  

        for m in range(len(reqlist_key)):
            nLen = int(reqdict_valuelen[reqlist_key[m]])
            sValue = sMsgTmp[ nPos : nPos+nLen ]
            #print("[O] %s: %s" %(reqlist_key[m],sValue) )
            reqdict_value[reqlist_key[m]]=sValue
            nPos +=  nLen
            
        #print("Old:[%s]" %(self.m_msgtext));
                
        self.Options()
        
        print("------------------------------------------")
        sMsgHeader=""
        for m in range(len(inheadlist_key)):
            sMsgHeader += str(inheaddict_value[inheadlist_key[m]])
            print(" %-10s : [%s]" %( inheadlist_key[m],inheaddict_value[inheadlist_key[m]] ) )
        
        sMsgBody=""
        for m in range(len(reqlist_key)):
            sMsgBody += str(reqdict_value[reqlist_key[m]])
            print(" %-10s : [%s]" %( reqlist_key[m],reqdict_value[reqlist_key[m]] ) )
       
        sTmp = sMsgHeader+sMsgBody  
        nLen = len(sTmp.encode('gb2312'))
        sMsgNew = "-%04d%s%s" %(nLen,sMsgHeader,sMsgBody)

        
        #print("------------------------------------------")
        #print("New:[%s]" %(sMsgNew));
          
        return sMsgNew    
        
        

        
        
        