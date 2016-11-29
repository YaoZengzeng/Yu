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
              #  if isinstance(cell_value, unicode):
               #         cell_value = '\n'.join(cell_value.split(' '))
                res.append(str(cell_value))
        return res

def newInternTextTable(data_row):
	head_row = ['姓名', '标准薪资', '全勤奖', '总工时', '有效工时',\
		'按工时月薪', '加减薪', '餐补', '电脑补贴', '交通津贴',\
		 '应发数','谐云应发', '学校应发']
	data_row = data_row[:len(head_row)]
	table = [head_row, data_row]
	return table

def newEmployeeTextTable(data_row):
	head_row = ['姓名', '基本工资', '月度奖金', '项目奖金', '加班费', \
		 '请假扣减', '加减薪', '应发小计', '社保基数',\
		'养老保险', '失业保险', '门诊医疗', '公积金', '四金总额',\
		'计税总额','代扣个税', '实发金额']
	data_row = data_row[:len(head_row)]
	table = [head_row, data_row]
	return table
    
def getSalaryTables(excel_name, internship):
	data = xlrd.open_workbook(excel_name)
	if internship:
		sheet = data.sheets()[0]
	else:
		sheet = data.sheets()[1]
	nrows_num = sheet.nrows
	ncols_num = sheet.ncols

	reload(sys)
	sys.setdefaultencoding('utf-8')

	start = 0
	end = nrows_num
	for r in range(nrows_num):
		cell_value = str(sheet.cell(r, 0).value)
		if "Name" in cell_value:
			start = r
		if '合计' in cell_value:
			end = r

		ret = {}

	for r in range(start, end):
		data_row = sheetRowToSlice(sheet, r, ncols_num)
		if internship:
			ret[sheet.cell(r, 0).value] = newInternTextTable(data_row)
		else:
			table = newEmployeeTextTable(data_row)
			ret[sheet.cell(r, 0).value] = newEmployeeTextTable(data_row)
	return ret
