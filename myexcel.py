#!/usr/bin/python
#coding=UTF-8

"""
(1) Input from salary excel
(2) Combine head and one entry as a new table
(3) Output many new tables described above
"""
 
import xlrd
import sys
from texttable import Texttable
 
def sheetRowToSlice(sheet, r, colnum):
        res = []
        for c in range(colnum):
                cell_value = sheet.cell(r, c).value
              #  if isinstance(cell_value, unicode):
               #         cell_value = '\n'.join(cell_value.split(' '))
                res.append(str(cell_value))
        return res

def newInternTextTable(data_row):
#    head_row = ['Name', 'Standard\nSalary', 'Total\nProject\nBonus', 'Working\nHour', 'Effective\nWorking\nHour', '(A)Salary', '(B)Adjustment', '(C)Meal\nAllowance', '(D)Transportation\nAllowance', '(S=A+B+C+D)\nTotal\nIncome', 'Company\nPart', 'School\nPart']
	head_row = ['姓名', '标准薪资', '全勤奖', '总工时', '有效工时',\
		'按工时月薪', '加减薪', '餐补', '电脑补贴', '交通津贴',\
		 '应发数','谐云应发', '学校应发']
	data_row = data_row[:len(head_row)]
	table = Texttable(200)
	table.set_precision(2)
	table.set_cols_dtype(['t', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'])
	table.set_cols_align(["c", "c", "c",  "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
	table.set_deco(Texttable.HEADER)
	table.add_rows([head_row, data_row])
	return table

def newEmployeeTextTable(data_row):
	virtual_head = ['    ', '    ', '    ', '    ', '    ',
		'    ', '    ', '    ', '    ', '    ',
		'    ', '    ', '    ', '    ', '    ',
		'    ', '    ']

	head_row1 = ['姓名', '基本', '月度', '项目', '加班', \
		 '请假', '加减', '应发', '社保',\
		'养老', '失业', '门诊', '公积', '四金',\
		'计税','代扣', '实发']
	head_row2 = ['啦啦', '工资', '奖金', '奖金', '费啦', '扣减', '薪啦', '小计', '基数', '保险', '保险', '医疗', '金啦', '总额', '总额', '个税', '金额']
	data_row = data_row[:len(head_row1)]
	table = Texttable(170)
	table.set_precision(2)
#	table.set_cols_dtype(['t', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'])
	table.set_cols_dtype(['t', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't'])
	table.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
	table.set_cols_width([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
	#table.set_deco(Texttable.HEADER)
	table.set_deco(0)
	table.add_rows([virtual_head, head_row1, head_row2, data_row])
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

#	data_row = ['姚增增', 3000.00, 1200.00, 168.00, 140.00, 3700.00, 520.00, 291.67, 0.00, 4511.67, 2255.83, 2255.83, 0.00 ]
	start = 0
	end = nrows_num
	for r in range(nrows_num):
		cell_value = str(sheet.cell(r, 0).value)
		if "Name" in cell_value:
			start = r
		if '合计' in cell_value:
			end = r

		ret = {}

	for r in range(start + 1, end):
		data_row = sheetRowToSlice(sheet, r, ncols_num)
		if internship:
			table = newInternTextTable(data_row)
		else:
			table = newEmployeeTextTable(data_row)
		ret[sheet.cell(r, 0).value] = table.draw()
	return ret
