#!/usr/bin/python
#coding=UTF-8

"""
(1) Input from salary excel
(2) Combine head and one entry as a new table
(3) Output many new tables described above
"""
 
import xlrd
import sys
 
def sheetRowToSlice(sheet, r, colnum):
        res = []
        for c in range(colnum):
                cell_value = sheet.cell(r, c).value
                s = str(cell_value)
                p = -1
                for i in range(len(s)):
					if s[i] == '.':
						p = i
                if p >= 0 and p + 2 < len(s) - 1:
                	s = s[ : (p + 3)]
                res.append(s)
        return res

def newFTETextTable(data_row):
	head_row = ['部门', '姓名', '基本工资', '月度奖金', '质量奖金', \
                    '项目奖金', '加班费', '请假扣减', '电脑补贴', '餐补', \
                    '应发小计', '社保基数', '养老保险', '失业保险', '门诊医疗', \
                    '公积金', '四金总计', '计税工资', '代扣个税', '实发金额']
	data_row = data_row[:len(head_row)]
	table = [head_row, data_row]
	return table

def newPTETextTable(data_row):
	head_row = ['部门', '姓名', '标准薪资', '项目奖金', '质量奖金', \
				'标准工时', '有效工时', '按工时时薪', '加减薪', '餐补', \
				'交通补贴', '应发数', '计税工资', '代扣个税', '实发数']
	data_row = data_row[:len(head_row)]
	table = [head_row, data_row]
	return table

def newInternTextTable(data_row):
	head_row = ['部门', '姓名', '标准薪资', '全勤奖', '质量奖金',\
                '标准工时', '有效工时', '按工时月薪', '加减薪', '电脑补贴', \
                '餐补', '交通津贴', '应发数', '谐云应发', '学校应发']
	data_row = data_row[:len(head_row)]
	table = [head_row, data_row]
	return table

textTable = [newFTETextTable, newPTETextTable, newInternTextTable]
    
def getSalaryTables(excel_name, index):
	data = xlrd.open_workbook(excel_name)
	sheet = data.sheets()[index]
	nrows_num = sheet.nrows
	ncols_num = sheet.ncols

	reload(sys)
	sys.setdefaultencoding('utf-8')

	start = 0
	end = nrows_num
	for r in range(nrows_num):
		cell_value = str(sheet.cell(r, 1).value)
		if "姓名" in cell_value:
			start = r + 1
		if '合计' in cell_value:
			end = r

		ret = {}

	for r in range(start, end):
		data_row = sheetRowToSlice(sheet, r, ncols_num)
		ret[sheet.cell(r, 1).value] = textTable[index](data_row)
	return ret
