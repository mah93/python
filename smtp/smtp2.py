# -*- coding: utf-8 -*-
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import encoders
from email import Encoders

mailto_add1=["目标邮箱1"]
mailto_add2=["目标邮箱2"]
mailto_file1 = [u"./smtptest.txt",u"./测试图片.jpg"]
mailto_file2 = [u"./测试图片.jpg"]
mailto_total = [[mailto_add1,mailto_file1],[mailto_add2,mailto_file2]]
mail_host="smtp.邮箱后缀.com"  
mail_user="你的邮箱用户名"    
mail_pass="邮箱密码"    
mail_postfix="邮箱后缀"  

def send_mail(add_list,sub,file_list):
    msg = MIMEMultipart()
    att1 = MIMEText("", 'base64', 'gbk')
    att1["Content-Type"] = 'application/octet-stream'

    for file_address in file_list:
        part = MIMEBase('application', 'octet-stream')
        file_name = os.path.basename(file_address)
        part.set_payload(open(file_address,'rb').read())
        encoders.encode_base64(part)
        part["Content-Disposition"] = 'attachment; filename=' + "\"" + file_name.encode('gbk') + "\""
        msg.attach(part)

    me = "关钰林"+"<"+mail_user+"@"+mail_postfix+">"   
    msg['Subject'] = sub   
    msg['From'] = me
    msg['To'] = ";".join(add_list)
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  
        s.login(mail_user,mail_pass)  
        s.sendmail(me, add_list, msg.as_string())  
        s.close()
        return True  
    except Exception, e:  
        print str(e)  
        return False
    
if __name__ == '__main__':
    for mailto_total_content in mailto_total:
        if send_mail(mailto_total_content[0],"我是主题",mailto_total_content[-1]):  
            print "success"  
        else:  
            print "fail"  
