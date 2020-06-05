#! /usr/bin/python
# -*- coding: gbk -*-
'''
    @ Project : simtc
    @ File Name : simtc.py
    @ Date : 2013/12/10
    @ Author : disp
'''

def PrintText(msg,name,pos,len):
    #strncpy(sStr1,sStr2,n)
    pos-=1  #调整索引从0开始
    value = msg[pos:pos+len]
    print("%s [%2d] : %s" %(name,len,value) )
    return 0
    
def PrintHeader(msg):
    print("------------------------------------------")
    PrintText(msg,"连接类型  ",1,1)    
    PrintText(msg,"报文长度  ",2,4)
    PrintText(msg,"Filler    ",6,2) 
    PrintText(msg,"报文类型  ",8,2) 
    PrintText(msg,"报文长度  ",10,4)    
    PrintText(msg,"循环数    ",14,6) 
    PrintText(msg,"消息数    ",20,6) 
    PrintText(msg,"片段数    ",26,4) 
    PrintText(msg,"前端号    ",30,4) 
    PrintText(msg,"终端号    ",34,6) 
    PrintText(msg,"银行号    ",40,3) 
    PrintText(msg,"机构号    ",43,5) 
    PrintText(msg,"操作工位号",48,3) 
    PrintText(msg,"柜员号    ",51,7) 
    PrintText(msg,"交易码    ",58,6) 
    PrintText(msg,"流水号    ",64,9) 
    PrintText(msg,"日期      ",73,8) 
    PrintText(msg,"半自动标识",81,1) 
    PrintText(msg,"终端类型  ",82,1) 
    PrintText(msg,"FLAG1     ",83,1) 
    PrintText(msg,"FLAG2     ",84,1) 
    PrintText(msg,"FLAG3     ",85,1) 
    PrintText(msg,"FLAG4     ",86,1) 
    PrintText(msg,"子系统渠道",87,1) 
    PrintText(msg,"主管ID    ",88,7) 
    PrintText(msg,"旧账号标识",95,1) 
    PrintText(msg,"UUID      ",96,32) 	

def MainSim(sIP,nPort,sMsg):
    import time  
    import datetime
    import socket  
    
    print("===========================================================")  
    print("开始连接 NCBS ...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    try:
        sock.connect((sIP, nPort))           
    except Exception as ex:
        print("连接失败：%s:%d" %(sIP,nPort) )
        print("失败原因：",ex)
        #sys.exit(-1)
        return -1
 
    input("连接成功，按任意键开始发送数据...")
 
    sIn = sMsg.encode('gb2312');
    sock.send(sIn)
    print("发送完毕，Len=%d\n" %len(sIn))
   
    nCount = int(1)
    while True:
        starttime = datetime.datetime.now()

        print("开始接收返回数据（序号：%02d）..." %nCount)
        try:
            #    time.sleep(2)
            #    sock.setblocking(0)
            sock.settimeout(30)
            sOut = sock.recv(2048)
            print("数据长度：",len(sOut))
            print("数据内容：",sOut)   
            
            #PrintHeader(sOut) 
            
            sOutStr = sOut.decode('gb2312');
            WriteFile(sOutStr)
          
        except Exception as ex:
            print(" 异常 <timeout>，",ex)
            break
            
        endtime = datetime.datetime.now()
        interval1=(endtime - starttime).seconds  
        interval2=(endtime - starttime).microseconds      
        print( "返回耗时：%d 秒，%d 微妙\n" %(interval1,interval2) ) 
        
        sFlag2 = sOutStr[83:84]
        if int(sFlag2) == 2:
            break;
        else:
            nCount += 1;
    
    print("关闭连接")
    sock.close()  

def WriteFile(sText):
    import datetime 
    sFileName = "./rspmsg.txt"
    
    fileRsp = open(sFileName,'a')
    curtime = datetime.datetime.now()
    fileRsp.write(str(curtime)+"\n" )
    fileRsp.write('['+sText+']')
    fileRsp.write("\n\n")
    fileRsp.close()
   
def InitTxnDict():
    from txn001045 import Txn001045
    from txn000440 import Txn000440
    from txn000450 import Txn000450
    
    msg_dict = {}
    txn = Txn001045();
    msg_dict[txn.GetTcode()] = txn
    txn = Txn000440();
    msg_dict[txn.GetTcode()] = txn
    txn = Txn000450();
    msg_dict[txn.GetTcode()] = txn
    
    return msg_dict
   
   
if __name__ == '__main__':  
    import sys 
     
    if len(sys.argv) == 2:      #指定交易码
        sTcode = sys.argv[1]        
    else:                       #参数错误，退出
        print("参数个数错误，用法；simtc.py  <TransCode Number>" ) 
        sys.exit(-1)
        
    try:    
        nTcode = int(sTcode)     #转换为整形
    except Exception as ex:
        print("参数错误，异常:",ex)
        sys.exit(-2)
        
    print("开始模拟交易 : %06d" %(nTcode) )
    
    txndict = InitTxnDict()
    
    if nTcode not in txndict.keys():
        print("不支持当前交易的模拟")   
        sys.exit(-3)
    
    txn = txndict[nTcode]
    sMsgSend = str(txn.MakeMsg())
 
    MainSim("192.168.x.x",51800,str(sMsgSend))
 
    
    


 


  
   
   

