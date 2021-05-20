#coding: utf-8
import os
import time
from email.message import EmailMessage
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def auto_report(receiver,sender,mail_license,smtpserver,mail_body,mail_title):
    message = MIMEText( mail_body, 'plain', 'utf-8' )
    message ['From'] = sender                                              
    message['To'] = receiver                                              
    message['Subject'] = Header( mail_title, 'utf-8' )  
    smtp = smtplib.SMTP()                                               
    smtp.connect( smtpserver )                                        
    smtp.login( sender, mail_license )                               
    smtp.sendmail( sender, receiver, message.as_string() )     
    smtp.quit()
    return

def auto_check(pbs_id,time_scan = 3600):
    #pbs_id = 'test'
    id_status = os.popen('qstat')
    id_str = id_status.read()
    while True:
        if pbs_id not in id_str:
            return 0
            break
        else:
            time.sleep(time_scan)


