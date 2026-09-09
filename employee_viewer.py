import mysql.connector
from datetime import datetime

class ConnectDb:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nikheth@20",
                database="companydb"

            )
            return self.connection
        except Exception as e:
            return None

class EmployeeManager(ConnectDb):
    def post(self,**kwargs):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="insert into employee(name,place,mobile,email,department,salary,joining_date) values(%s,%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Employee Added Successfully")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query="select * from employee"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            for rec in records:
                print(rec)
        except Exception as e:
             print(e)


    def get_object(self,id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id =%s"
            values=(id,)
            self.cursor.execute(query,values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            return None
    def retrieve(self,id=None):
        try:
            self.get_object(id=id)
            values=(id,)
            query="select * from employee where id =%s"
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)


    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record != None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k +"=%s ,"
                placeholder=placeholder.rstrip(",")
                query=f"update employee set {placeholder} where id =%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print( "Employee Updated Successfully.")
                self.get()
            else:
                print("Employee NOT Found")
        except Exception as e :
            print(e)

    def delete(self,id=None):
        try:
            records=self.get_object(id=id)
            values=(id,)
            if records != None:
                query="delete from employee where id =%s"
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Employee Deleted Successfully.")
                self.get()
        except Exception as e:
            print(e)




employee_instances=EmployeeManager()
#employee_instances.post(name="Nikheth",place="Kakkanad",mobile="9074490523",email="nikheth@gmail.com",department="Developer",salary=50000,joining_date="2026-12-03")
# employee_instances.post(name="Jomy",place="Thevara",mobile="9114470503",email="jomy@gmail.com",department="Finance",salary=75000,joining_date="2023-06-16")
# employee_instances.get()
# employee_instances.put(2,name="Anu",email="anu@gamil.com",salary=40000,joining_date=datetime.today())
# employee_instances.delete(1)
employee_instances.retrieve(2)