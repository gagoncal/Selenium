import unittest

from AssertTitle import AssertTitle

from waitForElements import WaitForElements

from waitForElements_2tests import WaitForElements

class FirstTestSuite(unittest.TestSuite): 
	def suite():
		suite = FirstTestSuite()
		suite.addTest(AssertTitle('test_AssertTitle'))
		suite.addTest(waitForElements('test_WaitForCheckOutPhotosButton'))
		suite.addTest(waitForElements_2tests('test_WaitForCheckOutPhotosButton'))
		return suite

if __name__ == "__main__":
	unittest.main()
