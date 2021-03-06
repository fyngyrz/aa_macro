#!/usr/bin/python

import unittest
import codecs
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

		# read unicode sample:
		try:
			fh = codecs.open('unisample.txt', encoding='utf-8')
			testBlock = fh.read()
			fh.close()
			st = str(type(testBlock))
			if st != "<type 'unicode'>": print 'failure to convert file to unicode'
		except:
			print 'failed to read unicode sample'

		# process unicode to ASCII:
		try:
			umod = macro(ucin=True)
			s = umod.unido(testBlock)
			st = str(type(s))
			if st != "<type 'str'>": print 'failure to convert unicode to ASCII'
		except:
			print 'failed to process unicode to ASCII'

		# process unicode to unicode:
		try:
			umod = macro(ucin=True,ucout=True)
			umod.unido(testBlock)
			s = umod.uniget()
			st = str(type(s))
			if st != "<type 'unicode'>": print 'failure to process unicode to unicode'
		except:
			print 'failed to process unicode to unicode'

		rebuild = 1
		fh = open('mactest.txt')
		testBlock = fh.read()
		fh.close()
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

		mod = macro(xlimit=5)
		output5 = mod.do('[style dome [b]]\n[for dome,0,10,1]\n[repeat 10 x-]\n[dup 10,y-]\n[eval 10,z-]')
		output = output + output5

		# for, repeat, dup, eval
		mod = macro(dlimit=1)
		output6 = mod.do('[style dome2 [b]][style dome [for dome2,0,2,1]]\n[for dome,0,2,1]\n')
		output = output + output6

		mod = macro(dlimit=1)
		output7 = mod.do('[repeat 2 [repeat 2 aB]]\n')
		output = output + output7

		mod = macro(dlimit=1)
		output8 = mod.do('[repeat 2 [dup 2,[dup 2,aB]]]\n')
		output = output + output8

		mod = macro(dlimit=1)
		output9 = mod.do('[repeat 2 [eval 2,[eval 2,oX]]]\n')
		output = output + output9

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
