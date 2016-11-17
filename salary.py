#!/usr/bin/python
#coding=UTF-8

import myemail
import myexcel

debug = 0

tables = myexcel.getSalaryTables("test.xlsx")

subject = '10月工资明细'

fromAddr = 'yaozengzeng123@163.com'

password = '940512yzz'

smtpServer = 'smtp.163.com'

toAddr = 'yaozengzeng@foxmail.com'

fo = open("prefix.txt", "r")

prefix = fo.read()

fo.close()

fo = open("postfix.txt", "r")

postfix = fo.read()

fo.close()

for table in tables:
	table = prefix + "\n\n" + table + "\n\n" + postfix
	if debug :
		print table
	else:
		myemail.sendMail(subject, fromAddr, password, smtpServer, toAddr, table)

print "Job done!"
