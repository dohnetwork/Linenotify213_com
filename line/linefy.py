#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import requests,json
#import urllib.parse
import pymysql

LINE_ACCESS_TOKEN="xhWM6CBeU6XRDXWdE0aqs1G816KGZhjxZlbRKNbPYdt"
url = "https://notify-api.line.me/api/notify"

#conn = pymysql.connect(host='172.16.1.212', unix_socket='/tmp/mysql.sock', user='root', passwd='camel', db='newphpmonitordb',charset='utf8')
conn = pymysql.connect(host='172.16.1.212', unix_socket='/tmp/mysql.sock', user='root', passwd='camel', db='phpmon32',charset='utf8')
cur = conn.cursor()
cur.execute("SELECT p1.label,p1.port,p2.message,p2.datetime,p2.line1 FROM psm_servers AS p1 ,psm_log AS p2 where p1.server_id = p2.server_id AND  p2.line1 <> 1")
# print cur.description
rows = cur.fetchall()
#if len(r) >0:
if len(rows) >0:
   for row in rows:
           if row[2].find("DOWN") == -1:
               #message = "เครื่อง " +  "%s"% (row[0])+" ใช้งานได้แล้ว "+ "เวลา  "+str(row[3]
               #message = row[0]
               #message="เครื่อง "+row[0]+"ใช้งานได้แล้ว เวลา "+str(row[3])
               message="เครื่อง "+row[0]+" SERVICE:"+str(row[1])+" ใช้งานได้แล้ว เวลา: "+str(row[3])
               msg = urllib.parse.urlencode({"message":message})
               LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
               session = requests.Session()
               a=session.post(url, headers=LINE_HEADERS, data=msg)
               print(a.text)
               #print(message)
               #op_list.sendMessage("เครื่อง " +  "%s"% (row[0])+" ใช้งานได้แล้ว "+ "เวลา  "+str(row[3]))
               #op_list.sendSticker(stickerId=random.choice(up),stickerPackageId="1",stickerVersion="100")
               #op_list.sendSticker(stickerId=str(up),stickerPackageId="1",stickerVersion="100")
           else:
               #message = "เปิด" #op_list.sendMessage("เครื่อง " +  "%s"% (row[0])+" พังอีกแล้ว "+ "เวลา  "+str(row[3]))
               #message="เครื่อง "+row[0]+"ระบบล้มเหลว  เวลา "+str(row[3])
               message="เครื่อง "+row[0]+" SERVICE:"+ str(row[1])+ " ล่ม เวลา: "+str(row[3])
               msg = urllib.parse.urlencode({"message":message})
               LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
               session = requests.Session()
               a=session.post(url, headers=LINE_HEADERS, data=msg)
               print(a.text)
   cur.execute("UPDATE psm_log set line1 = 1 where psm_log.line1 <>1")
               #pr
               #message = "เครื่องเปิด"

   #print(r)
   #message = row[0]
cur.close()
conn.close()

#message ="ทดสอบการทำงานิ" # ข้อความที่ต้องการส่ง
#----------------------------------------------------------
#print(message)
#msg = urllib.parse.urlencode({"message":message})
#LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
#session = requests.Session()
#a=session.post(url, headers=LINE_HEADERS, data=msg)
#print(a.text)
