import unittest
import pymssql

class PythonDatabaseTests(unittest.TestCase):

    def setUp(self):
        #create a MSSQL Connection
        self.conn=pymssql.connect(host='TESTAUTOMATION\SMTEST',user='sa',password='pass@word',database='AdventureWorks2012')
    def test_verify_record_exist(self):
        conn = self.conn
        #create a cursor
        cursor = conn.cursor(as_dict=True)
        #get all records from the Name column of the table HumanResources.Department
        cursor.execute('select Name from HumanResources.Department')
        #fetch all records as dictionary
        records=cursor.fetchall()
        #close the cursor
        cursor.close()
        #print all records
        print records
        #create a list to contain department names
        department_names=[]
        #add each department name to the list above
        for record in records:
            department_name=record.get('Name')
            department_names.append(department_name)
            print department_name
        print "total records=%d" % len(department_names)
        #assert the record exist
        self.assertTrue(department_names.index('Shipping and Receiving')!=-1)

    def tearDown(self):
        self.conn.close()
        
if __name__ == "__main__":
    unittest.main()