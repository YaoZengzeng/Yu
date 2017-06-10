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

fteTableMap = myexcel.getSalaryTables("salary.xlsx", 0)
pteTableMap = myexcel.getSalaryTables("salary.xlsx", 1)
internTableMap = myexcel.getSalaryTables("salary.xlsx", 2)

for name in fteTableMap:
	if addrMap.has_key(name) == False :
		continue
	toAddr = addrMap[name]
	htmlStr = text2html.text2html(prefix.split('\n'), fteTableMap[name], postfix.split('\n'))
	if debug :
		print "FTE Employee: destination mail address is " + toAddr
		print htmlStr
	else :
		myemail.sendMail(subject, fromAddr, password, smtpServer, portNum, toAddr, htmlStr)

for name in pteTableMap:
	if addrMap.has_key(name) == False :
		continue
	toAddr = addrMap[name]
	htmlStr = text2html.text2html(prefix.split('\n'), pteTableMap[name], postfix.split('\n'))
	if debug :
		print "PTE Employee: destination mail address is " + toAddr
		print htmlStr
	else :
		myemail.sendMail(subject, fromAddr, password, smtpServer, portNum, toAddr, htmlStr)

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

print "Job done!"
