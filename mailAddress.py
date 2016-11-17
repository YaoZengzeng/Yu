#!/usr/bin/python
#coding=UTF-8

"""
This file is used to get a name-mailaddress directory from excel
"""

import xlrd
import sys

debug = 0

def getMailAddrMap(excel_name):
	data = xlrd.open_workbook(excel_name)
	sheet = data.sheets()[0]
	nrows_num = sheet.nrows
	ncols_num = sheet.ncols

	reload(sys)
	sys.setdefaultencoding('utf-8')

	dict = {'姚增增' : 'yaozengzeng@foxmail.com'}
	for r in range(1, nrows_num):
		name = sheet.cell(r, 0).value
		addr = sheet.cell(r, 1).value
		if dict.has_key(name):
			continue
		dict[name] = addr
	if debug:
		for key in dict:
			print key, " email is", dict[key]
	return dict

