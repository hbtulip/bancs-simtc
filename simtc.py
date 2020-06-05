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
    pos-=1  #����������0��ʼ
    value = msg[pos:pos+len]
    print("%s [%2d] : %s" %(name,len,value) )
    return 0
    
def PrintHeader(msg):
    print("------------------------------------------")
    PrintText(msg,"��������  ",1,1)    
    PrintText(msg,"���ĳ���  ",2,4)
    PrintText(msg,"Filler    ",6,2) 
    PrintText(msg,"��������  ",8,2) 
    PrintText(msg,"���ĳ���  ",10,4)    
    PrintText(msg,"ѭ����    ",14,6) 
    PrintText(msg,"��Ϣ��    ",20,6) 
    PrintText(msg,"Ƭ����    ",26,4) 
    PrintText(msg,"ǰ�˺�    ",30,4) 
    PrintText(msg,"�ն˺�    ",34,6) 
    PrintText(msg,"���к�    ",40,3) 
    PrintText(msg,"������    ",43,5) 
    PrintText(msg,"������λ��",48,3) 
    PrintText(msg,"��Ա��    ",51,7) 
    PrintText(msg,"������    ",58,6) 
    PrintText(msg,"��ˮ��    ",64,9) 
    PrintText(msg,"����      ",73,8) 
    PrintText(msg,"���Զ���ʶ",81,1) 
    PrintText(msg,"�ն�����  ",82,1) 
    PrintText(msg,"FLAG1     ",83,1) 
    PrintText(msg,"FLAG2     ",84,1) 
    PrintText(msg,"FLAG3     ",85,1) 
    PrintText(msg,"FLAG4     ",86,1) 
    PrintText(msg,"��ϵͳ����",87,1) 
    PrintText(msg,"����ID    ",88,7) 
    PrintText(msg,"���˺ű�ʶ",95,1) 
    PrintText(msg,"UUID      ",96,32) 	

def MainSim(sIP,nPort,sMsg):
    import time  
    import datetime
    import socket  
    
    print("===========================================================")  
    print("��ʼ���� NCBS ...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    try:
        sock.connect((sIP, nPort))           
    except Exception as ex:
        print("����ʧ�ܣ�%s:%d" %(sIP,nPort) )
        print("ʧ��ԭ��",ex)
        #sys.exit(-1)
        return -1
 
    input("���ӳɹ������������ʼ��������...")
 
    sIn = sMsg.encode('gb2312');
    sock.send(sIn)
    print("������ϣ�Len=%d\n" %len(sIn))
   
    nCount = int(1)
    while True:
        starttime = datetime.datetime.now()

        print("��ʼ���շ������ݣ���ţ�%02d��..." %nCount)
        try:
            #    time.sleep(2)
            #    sock.setblocking(0)
            sock.settimeout(30)
            sOut = sock.recv(2048)
            print("���ݳ��ȣ�",len(sOut))
            print("�������ݣ�",sOut)   
            
            #PrintHeader(sOut) 
            
            sOutStr = sOut.decode('gb2312');
            WriteFile(sOutStr)
          
        except Exception as ex:
            print(" �쳣 <timeout>��",ex)
            break
            
        endtime = datetime.datetime.now()
        interval1=(endtime - starttime).seconds  
        interval2=(endtime - starttime).microseconds      
        print( "���غ�ʱ��%d �룬%d ΢��\n" %(interval1,interval2) ) 
        
        sFlag2 = sOutStr[83:84]
        if int(sFlag2) == 2:
            break;
        else:
            nCount += 1;
    
    print("�ر�����")
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
     
    if len(sys.argv) == 2:      #ָ��������
        sTcode = sys.argv[1]        
    else:                       #���������˳�
        print("�������������÷���simtc.py  <TransCode Number>" ) 
        sys.exit(-1)
        
    try:    
        nTcode = int(sTcode)     #ת��Ϊ����
    except Exception as ex:
        print("���������쳣:",ex)
        sys.exit(-2)
        
    print("��ʼģ�⽻�� : %06d" %(nTcode) )
    
    txndict = InitTxnDict()
    
    if nTcode not in txndict.keys():
        print("��֧�ֵ�ǰ���׵�ģ��")   
        sys.exit(-3)
    
    txn = txndict[nTcode]
    sMsgSend = str(txn.MakeMsg())
 
    MainSim("192.168.x.x",51800,str(sMsgSend))
 
    
    


 


  
   
   

