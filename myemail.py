#!/usr/bin/python
#coding=UTF-8

# just define function sendMail to wrap the smtplib and email module

import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

def sendMail(subject, fromAddr, password, smtpServer, portNum, toAddr, htmlStr):
	msg = MIMEText(htmlStr, 'html', 'utf-8')
	msg['From'] = fromAddr
	msg['To'] = toAddr
	msg['Subject'] = Header(subject, 'utf8').encode()
	if portNum == 25:
		server = smtplib.SMTP(smtpServer, 25)
		server.login(fromAddr, password)
		server.sendmail(fromAddr, [toAddr], msg.as_string())
		server.quit()
	else:
		server = SMTP_SSL(smtpServer)
		server.login(fromAddr, password)
		server.sendmail(fromAddr, [toAddr], msg.as_string())
		server.quit()
