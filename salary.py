#!/usr/bin/python

import myemail
import myexcel

tables = myexcel.getSalaryTables("test.xlsx")

fromAddr = 'yaozengzeng123@163.com'

password = '940512yzz'

smtpServer = 'smtp.163.com'

toAddr = 'yaozengzeng@foxmail.com'

for table in tables:
	myemail.sendMail(fromAddr, password, smtpServer, toAddr, table)

print "Job done!"
