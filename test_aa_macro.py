#!/usr/bin/python

import unittest
from aa_macro import macro

class TestAAMacro(unittest.TestCase):

    def test_simple_style(self):
        '''
        Test a simple substitution style.
        '''
        input = '[style hello Why hello, [b], how are you?]{hello Ben}'
        expected = 'Why hello, Ben, how are you?'
        output = macro().do(input)
        self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
