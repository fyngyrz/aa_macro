#!/usr/bin/python

import unittest
from aa_macro import *


class TestAAMacro(unittest.TestCase):

	def test_aa_macro(self):
		rebuild = 1
		"""
Test a simple substitution style.
"""
		fh = open('mactest.txt')
		testBlock = fh.read()
		fh.close()
		mod = macro()
		output = mod.do(testBlock)

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

		fh = open('expected.html')
		expected = fh.read()
		fh.close()		
		self.assertEqual(expected, output)

if __name__ == '__main__':
	unittest.main()
