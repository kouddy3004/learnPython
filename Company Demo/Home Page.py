from Manager import Manager as M;
from Associate import Associate as A;

class EmployeeEntry:
    row=0
    employee_list={}
    def main(self):        
        close=False;      
        print("Welcome to Data entry");
        print("  -----------------");        
        while close==False:            
            role=input ("Enter your designation\n1 For Associate,\n2 For Manager,\n3 For Exit\n");
            if (role=="1"):
                A.Associate_details(self.employee_list);
            elif (role=="2"):
                employee_list=M.Manager_details(self.row,self.employee_list)                
                for key in self.employee_list:
                    self.row=int(key[0])                                
               
            elif(role=="3"):
                close=True;
            else:
                print("Please enter given option");
            
if (__name__ == '__main__'):
    obj = EmployeeEntry()
    obj.main()
