#!/usr/bin/python
#coding=UTF-8

import myemail
import myexcel
import mailAddress
import text2html

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
	htmlStr = text2html.text2html(prefix.split('\n'), internTableMap[name], postfix.split('\n'))
	if debug :
		print "Internship: destination mail address is " + toAddr
		print htmlStr
	else :
		myemail.sendMail(subject, fromAddr, password, smtpServer, toAddr, htmlStr)

for name in employeeTableMap:
	if addrMap.has_key(name) == False :
		continue
	toAddr = addrMap[name]
	htmlStr = text2html.text2html(prefix.split('\n'), employeeTableMap[name], postfix.split('\n'))
	if debug :
		print "Employee: destination mail address is " + toAddr
		print htmlStr
	else :
		myemail.sendMail(subject, fromAddr, password, smtpServer, toAddr, htmlStr)

print "Job done!"
