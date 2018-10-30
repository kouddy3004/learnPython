class Manager:
    def Manager_details(row,employe_list):
        ret=False
        print("Welcome Manager");
        print(" ------------- ")
        while(ret==False):
            choice=input("Enter 1 to write,\nEnter 2 to view all records,\nEnter 3 to select particular employee details,\nEnter 4 to close\n")
            manager=Manager();            
            if (choice=="1"):
                row=row+1;
                print("Row :"+str(row))
                employe_list[row,"ID"]=input("Enter ID :");
                employe_list[row,"Name"]=input("Enter Name :");
                employe_list[row,"Role"]=input("Enter Role :");           
                            
            elif (choice =="2"):            
                for key in employe_list:
                    print (key[1] + " : " + employe_list[key]);
            elif(choice=="3"):
                sid=0
                user = input("Enter user ID you want to search")
                search=False
                for key in employe_list:
                    if(employe_list[key]==user):
                        sid=key[0]                        
                        search=True
                        break
                if(search==True):
                    print(sid)
                    for key in employe_list:
                        if (key[0]==sid):
                            print(key[1]+" : "+employe_list[key])
                elif(search==False):
                    print("No values Found")                
            elif(choice=="4"):
                ret=True
            else:
                print("Please enter given option");
        return employe_list;
        
                 
          
