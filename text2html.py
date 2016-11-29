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
	for row in table:
		htmlStr += '<tr>'
		for cell in row:
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
