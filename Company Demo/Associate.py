class Associate:
    def Associate_details(employee_list):
        print ("Welcome Associate");
        print(" -------------- ");  
        close= False;
        while(close==False):
            choice=input("Enter\n1 - > To View Details\n2 -> Search by ID Values\n3 - > To close")
            if (choice=="1"):
                if not employee_list:
                    print("No employee is available for the respective Manager\nPlease Ask respective Manager to enter Associate details")
                else:
                    for key in employee_list:
                        print(key[1] + " : " + employee_list[key])
            elif (choice=="2"):
                if not employee_list:
                    print("No employee is available for the respective Manager\nPlease Ask respective Manager to enter Associate details")
                else:
                    sid=0
                    user = input("Enter user ID you want to search")
                    search=False
                    for key in employee_list:
                        if(employee_list[key]==user):
                            sid=key[0]                        
                            search=True
                            break
                    if(search==True):
                        for key in employee_list:
                            if(key[0]==sid):
                                print (key[1] + " : " + employee_list[key]);
                    elif(search==False):
                        print("No values Found")
                
                     
            elif(choice=="3"):
                close=True;

            else:
                 print("Please enter given Option")

             
            
            
