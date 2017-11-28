#!/usr/bin/python

import unittest
from aa_macro import *
import difflib
import sys
from aa_ansiicolor import *

c = htmlAnsii()

def nocrlf(s):
	while len(s) > 0 and (s[-1] == '\n' or s[-1] == '\r'):
		s = s[:-1]
	return s

def diffme(fna,fnb,barlen):
	global c
	bar = '-' * barlen
	bar = c.c(bar,'blue')
	fh = open(fna)
	fa = fh.read().splitlines(1)
	fh.close()

	fh = open(fnb)
	fb = fh.read().splitlines(1)
	fh.close()

	d = difflib.Differ()

	result = list(d.compare(fa, fb))

	print bar
	missingcolor  = 'red'
	addedcolor    = 'white'
	quotecolor    = 'yellow'
	stringcolor   = 'aqua'
	for line in result:
		if line[0] != ' ':
			line = nocrlf(line) # terminating cr/lf removed
			if line[0] == '-':
				out = c.c('-',missingcolor) + c.c(' "',quotecolor) + c.c(line[2:],'aqua')+c.c('"',quotecolor)
			elif line[0] == '+':
				out = c.c('+',addedcolor) + c.c(' "',quotecolor) + c.c(line[2:],'aqua')+c.c('"',quotecolor)
			out += '\n'
			sys.stdout.write(out)
	print bar
	print c.c('End of differences','green')

class TestAAMacro(unittest.TestCase):

	def test_aa_macro(self):
		"""
Test aa_macro.py functionality
"""
		global c
		bar = '-' * 40
		print c.c(bar,'blue')
		expect = 'expected.html'
		badout = 'badoutput.html'

		rebuild = 1
		fh = open('mactest.txt')
		testBlock = fh.read()
		fh.close()
#		mod = macro()
		mod = macro(debug=True)
		output = mod.do(testBlock)
		dtrace = mod.getdebug()
		fh = open("aam_dtrace.txt",'w')
		fh.write(dtrace)
		fh.close()
		
		mod = macro(noembrace=True)
		output2 = mod.do('[embrace embrace-example.py]\n')
		output = output + output2
		
		mod = macro(noinclude=True)
		output3 = mod.do('[include aagen-example.txt]\n')
		output = output + output3
		
		mod = macro(noshell=True)
		output4 = mod.do('[sys echo shell test]\n[gload othervar forvariable.txt]\n[load myvar forvariable.txt]\n')
		output = output + output4

		if rebuild == 1:
			fileName = 'testresult.html'
			try:
				fileHandle = open(fileName,'w')
			except:
				print 'Unable to open "%s"' % fileName
			else:
				try:
					fileHandle.write(output)
				except:
					print 'Unable to write output to "%s"' % fileName
				try:
					fileHandle.close()
				except:
					print 'Unable to close "%s"' % fileName

		fh = open(expect)
		expected = fh.read()
		fh.close()
		if expected == output:
			result = True
		else:
			print c.c('ERROR: expected != output','red')
			s = 'Comparing %s with %s:' % (expect,badout)
			bl = len(s)
			print c.c(s,'yellow')
			result = False
			ok = True
			try:
				fh = open(badout,'w')
				fh.write(output)
			except:
				ok = False
				print '>>> Could not write "%s". Do permissions need adjustment?' % (badout,)
			try:
				fh.close()
			except:
			    ok = False
			if ok == True:
				diffme(expect,badout,bl)
		try:
			self.assertEqual(True,result,'expected != output\nCompare expected.html with badoutput.html')
		except:
			pass

if __name__ == '__main__':
	unittest.main()
