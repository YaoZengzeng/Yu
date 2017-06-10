#!/usr/bin/python
#coding=UTF-8

def text2html(prefixes, table, postfixes):
	htmlStr = '<html><pre><body>'

	htmlStr += '<p>'
	for prefix in prefixes:
		htmlStr += (prefix + '\n')
	htmlStr += '</p>'

	htmlStr += '<br><br>'

	htmlStr += '<table border="1">'

	th = table[0]
	htmlStr += '<tr>'
	for cell in th:
		htmlStr += ('<th>' + cell + '</th>')
	htmlStr += '</tr>'

	td = table[1]
	htmlStr += '<tr>'
	for cell in td:
		htmlStr += ('<td>' + cell + '</td>')
	htmlStr += '</tr>'

	htmlStr += '</table>'

	htmlStr += '<br><br>'

	htmlStr += '<p>'
	for postfix in postfixes:
		htmlStr += (postfix + '\n')
	htmlStr += '</p>'

	htmlStr += '</body></pre></html>'

	return htmlStr
