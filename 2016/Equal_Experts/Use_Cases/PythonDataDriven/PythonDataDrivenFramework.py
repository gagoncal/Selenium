import csv
import unittest
from selenium import webdriver

##define a function that returns number of rows in a csv file

def getNumberOfCount(filename):
        with open(filename) as f:
                reader=csv.reader(f,delimiter=";")
                next(reader, None)  # skip the headers
                row_count = sum(1 for row in reader)
                return row_count
               
class SiteInfoVerification(unittest.TestCase):    

##setup method
        
        def setUp(self):
                self.driver=webdriver.Chrome()
##test method
                
        def test_site_info_verification(self):
                numberOfSites=getNumberOfCount('siteinfo.csv')
                print("Number of Sites: ",numberOfSites)
                driver = self.driver
                with open('siteinfo.csv') as SiteInfoFile:
                        driver=self.driver
                        reader=csv.reader(SiteInfoFile,delimiter=";")
                        next(reader, None)  # skip the headers
                        #for row in reader:
                        for i, line in enumerate(reader):                               
                                print(line[0],line[1])
                                #driver.get(''.join(line[0]))
                                driver.get(line[0])
                                self.assertIn(line[1],driver.title)
                                
##tear down method
                                
        def tearDown(self):
                self.driver.close()

   

if __name__=="__main__":
        nose.main()