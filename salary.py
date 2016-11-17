#!/usr/bin/python
#coding=UTF-8

import myemail
import myexcel
import mailAddress

debug = 0 

tableMap = myexcel.getSalaryTables("test.xlsx")

addrMap = mailAddress.getMailAddrMap("mailAddress.xlsx")

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

for name in tableMap:
	if addrMap.has_key(name) == False :
		continue
	toAddr = addrMap[name]
	content = prefix + "\n\n" + tableMap[name] + "\n\n" + postfix
	if debug :
		print "destination mail address is " + toAddr
		print content
	else :
		myemail.sendMail(subject, fromAddr, password, smtpServer, toAddr, content)

print "Job done!"
