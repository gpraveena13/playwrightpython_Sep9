class Emp:

    emp_name = "praveena"

    def __init__(self,emp_no,emp_name):
        #pass
        self.emp_no = emp_no
        self.emp_name = emp_name 
        
    def samsung(self):
        print("OMADM employee:", self.emp_name)
        print("OMADM employee:", self.emp_no)
        
# class Imp(Emp):
    
#     def __init__(self):
#           #pass
#           self.emp_no = 1001
#           self.emp_name ="ajay"
          
#     def samsung(self):
#           print("OMADM employee:", self.emp_name)
#           print("OMADM employee:", self.emp_no)

obj1 = Emp(100,"krithin")
obj1.samsung()

# obj2 =Imp()
# obj2.samsung()    






        # def __init__(self):
        #     self.emp_no = 500
        #     self.emp_name ="ram"
    
    
        # def test(self,d1="ram"):
        #     print("testing:",self.d1)

# obj1 = Emp()
# obj1.samsung()

# obj2 =Imp()
# obj2.test()
        
        