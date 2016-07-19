import unittest
import pymssql

class PythonDatabaseTests(unittest.TestCase):

    def setUp(self):
        #create a MSSQL Connection
        self.conn=pymssql.connect(host='TESTAUTOMATION\SMTEST',user='sa',
                                  password='pass@word',database='AdventureWorks2012')

    def test_verify_record_delete(self):
        conn = self.conn
        #create a cursor for delete
        cursor_delete=conn.cursor()
        cursor_delete.execute('Delete From HumanResources.Department Where Name=%s'
                              ,'Selenium Master')
        conn.commit()
        #create a cursor for select
        cursor = conn.cursor()
        #get the record from the Name column of the table HumanResources.Department for the condition
        cursor.execute('select Name from HumanResources.Department WHERE Name=%s','Selenium Master')
        #fetch all records and print
        print (cursor.fetchall())
        records=cursor.rowcount
        print "Number of rows are:",records
        #close the cursor
        cursor.close()
        cursor_delete.close()
        self.assertTrue(records==0)

    def tearDown(self):
        self.conn.close()
        
if __name__ == "__main__":
    unittest.main()