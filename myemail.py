#!/usr/bin/python
#coding=UTF-8

# just define function sendMail to wrap the smtplib and email module

import smtplib
from email.header import Header
from email.mime.text import MIMEText

def sendMail(subject, fromAddr, password, smtpServer, toAddr, htmlStr):
	msg = MIMEText(htmlStr, 'html', 'utf-8')
	msg['From'] = fromAddr
	msg['To'] = toAddr
	msg['Subject'] = Header(subject, 'utf8').encode()
	server = smtplib.SMTP(smtpServer, 25)
	server.login(fromAddr, password)
	server.sendmail(fromAddr, [toAddr], msg.as_string())
	server.quit()
