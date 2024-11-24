from atmFunctions import *
import time

while(True):
    while(True):
        for i in range(30):
            print("\n")
        print("WELCOME TO THE REAL BANKING SYSTEM")
        userID = input("Enter user ID: ").upper()
        #validate user input information
        try:
            if verifyID(userID) == 0:
                raise Exception
            else:
                pin = input("Enter 4-digit PIN: ")
                try:
                    if verifyUser(userID,pin) == 0:
                        raise Exception
                    else:
                        break
                except:
                    pgbreak()
                    print("Please enter the correct PIN")
                    pgbreak()
                    time.sleep(2)
        except:
            pgbreak()
            print("User is not found")
            pgbreak()
            time.sleep(2)



    decision = None
    
    while(decision != "0"):
        decision = None
        printoptions(userID)
        decision = input("> ")

        # withdraw
        if decision == "1":     
            # amount to withdraw
            try:
                atw = float(input("Enter the amount to be withdrawn: "))
                pgbreak()
                withdraw(userID,atw,1)   
                pgbreak()
            except:
                print("Amount input is invalid")

        # deposit
        elif decision == "2":   
            # amount to deposit
            try:
                atw = float(input("Enter the amount to be deposited: "))
                pgbreak()
                deposit(userID,atw,1)
                pgbreak()
            except:
                print("Amount input is invalid")           

        # transfer
        elif decision == "3":
            while(True):
                transferID = input("Enter ID of account to receive transfer: ").upper()
                #verifies if the user input
                try:
                    if verifyID(transferID) == 0:
                        raise Exception
                    else:
                        break
                except:
                    print("User is not found\n")  
            #amount to transfer
            try:
                att = float(input("Enter the amount to be transferred: "))
                pgbreak()
                transfer(userID,transferID,att)
                pgbreak()
            except:
                print("Amount input is invalid")

        # check balance
        elif decision == "4": 
            pgbreak()  
            check(userID)
            pgbreak()
        
        # change PIN
        elif decision == "5":   
            while(True):
                newPIN = input("Enter a new 4-digit PIN: ")
                try:
                    if verifyPIN(newPIN) == 0:
                        raise Exception
                    else:
                        break
                except:
                    print("Please input a valid PIN")
                    pgbreak()
            pgbreak()
            changePIN(userID,newPIN)
            pgbreak()

        time.sleep(3)
        
    print("Goodbye " + userID + "  ~~")
    print("Don't forget to take your card!")
    time.sleep(3)
    pgbreak()
