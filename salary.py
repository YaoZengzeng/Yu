#!/usr/bin/python
#coding=UTF-8

import myemail
import myexcel
import mailAddress
import text2html
import ConfigParser

debug = 0

config  = ConfigParser.ConfigParser()
config.readfp(open("config.ini", "rb"))

smtpServer = config.get("global", "smtpServer")
portNum = int(config.get("global", "portNum"))
subject = config.get("global", "subject")
fromAddr = config.get("global", "fromAddr")
password = config.get("global", "password")

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
		myemail.sendMail(subject, fromAddr, password, smtpServer, portNum, toAddr, htmlStr)

for name in employeeTableMap:
	if addrMap.has_key(name) == False :
		continue
	toAddr = addrMap[name]
	htmlStr = text2html.text2html(prefix.split('\n'), employeeTableMap[name], postfix.split('\n'))
	if debug :
		print "Employee: destination mail address is " + toAddr
		print htmlStr
	else :
		myemail.sendMail(subject, fromAddr, password, smtpServer, portNum, toAddr, htmlStr)

print "Job done!"
