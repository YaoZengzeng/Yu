#!/usr/bin/python
#coding=UTF-8

import myemail
import myexcel
import mailAddress

debug = 0 

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

addrMap = mailAddress.getMailAddrMap("mailAddress.xlsx")

internTableMap = myexcel.getSalaryTables("test.xlsx", True)
employeeTableMap = myexcel.getSalaryTables("test.xlsx", False)

for name in internTableMap:
	if addrMap.has_key(name) == False :
		continue
	toAddr = addrMap[name]
	content = prefix + "\n\n" + internTableMap[name] + "\n\n" + postfix
	if debug :
		print "Internship: destination mail address is " + toAddr
		print content
	else :
		myemail.sendMail(subject, fromAddr, password, smtpServer, toAddr, content)

for name in employeeTableMap:
	if addrMap.has_key(name) == False :
		continue
	toAddr = addrMap[name]
	content = prefix + "\n\n" + employeeTableMap[name] + "\n\n" + postfix
	if debug :
		print "Employee: destination mail address is " + toAddr
		print content
	else :
		myemail.sendMail(subject, fromAddr, password, smtpServer, toAddr, content)

print "Job done!"
