import unittest
import pymssql

class PythonDatabaseTests(unittest.TestCase):

    def setUp(self):
        #create a MSSQL Connection
        self.conn=pymssql.connect(host='TESTAUTOMATION\SMTEST',user='sa',
                                  password='pass@word',database='AdventureWorks2012')

    def test_verify_record_update(self):
        conn = self.conn
        #create a cursor for update
        cursor_update=conn.cursor()
        cursor_update.execute("Update HumanResources.Department Set Name=\'Selenium Master Java\' Where Name=%s"
                              ,'Selenium Master Python')
        conn.commit()
        #create a cursor for select
        cursor = conn.cursor()
        #get the record from the Name column of the table HumanResources.Department for the condition
        cursor.execute('select Name from HumanResources.Department WHERE Name=%s','Selenium Master Java')
        #fetch all records and print
        print (cursor.fetchall())
        records=cursor.rowcount
        print "Number of rows are:",records
        #close the cursor
        cursor.close()
        self.assertTrue(records==1)

    def tearDown(self):
        self.conn.close()
        
if __name__ == "__main__":
    unittest.main()