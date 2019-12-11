'''
Created on Mar 9, 2015

@author: Sylvain Garcia <garcia.6l20@gmail.com>
'''
import unittest
import mainwindow
import generator

class Test(unittest.TestCase):

    def testMain(self):
        #mainwindow.main()
        md_filename = 'test_file.md'
        generator.Generator.generatePDF(md_filename)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
