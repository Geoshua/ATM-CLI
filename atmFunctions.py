    #library for all the functions used in the main program
def printoptions(userID):
    print("\nHello "+ userID + "! How are you today?")
    print("\nWhat can I help you with?")
    print("1. Withdraw money")
    print("2. Deposit money")
    print("3. Transfer money")
    print("4. Check balance")
    print("5. Change pin")
    print("0. Logout")

def withdraw(userID,atw,mode):   
    savingfile = open("savingData.txt",'r')
    #loops through whole file
    for line in savingfile:
        fileID, fileBalance = line.strip().split("#")
        if userID == fileID:
            if atw <= float(fileBalance) and atw > 0:
                foundline = line
                newBalance = float(fileBalance) - atw
                newData = userID + "#" + str(newBalance) + "\n"
                if mode == 1:
                    print("Amount dispensed: $ ", + atw)
                    print("     Please take the cash before leaving!")
                print("New balance: $ ",str(newBalance))
            else:
                print("The amount input either exceeds bank balance or is not valid")
                savingfile.close()
                return 0

    savingfile.close()

    # creates a new variable that temporarily stores the new replacement file
    with open("savingData.txt",'r') as file:
        fileData = file.read()
        fileData = fileData.replace(foundline,newData)

    # overwrites the file with the replacement
    with open("savingData.txt",'w') as file:
        file.write(fileData)

def deposit(userID,atd,mode):
    savingfile = open("savingData.txt",'r')
    #loops through whole file
    for line in savingfile:
        fileID, fileBalance = line.strip().split("#")
        if userID == fileID:
            if atd > 0:
                foundline = line
                newBalance = float(fileBalance) + atd
                newData = userID + "#" + str(newBalance) + "\n"
                if mode == 1:
                    print("Amount deposited: $ ", + atd)
                    print("New balance: $ " + str(newBalance))
            else:
                print("The amount input is not valid")
                savingfile.close()
                return
    savingfile.close()

    with open("savingData.txt",'r') as file:
        fileData = file.read()
        fileData = fileData.replace(foundline,newData)
    with open("savingData.txt",'w') as file:
        file.write(fileData)

def transfer(userID,transferID,att):
    #calls the function withdraw to take money out of account
    process = withdraw(userID,att,0)
    if process != 0:
        print("$ " + str(att) + " successfully transferred to " + transferID)
        # calls function deposit to put money in given account
        deposit(transferID,att,0) 
    else:
        print("$ " + str(att) + " was not transferred to " + transferID)

    

def check(userID):
    savingfile = open("savingData.txt",'r')
    #loops through whole file
    for line in savingfile:
        fileID, fileBalance = line.strip().split("#")
        if userID == fileID:
            print("Account balance: $ " + fileBalance)
    savingfile.close()

def changePIN(userID,newPIN):
    savingfile = open("userData.txt",'r')
    #loops through whole file
    for line in savingfile:
        fileID, filePIN = line.strip().split("#")
        if userID == fileID:
            foundline = line
            newData = userID + "#" + newPIN + "\n"
    savingfile.close()

    with open("userData.txt",'r') as file:
        fileData = file.read()
        fileData = fileData.replace(foundline,newData)
    
    with open("userData.txt",'w') as file:
        file.write(fileData)
    print("PIN is changed!")

#verifications for input data
def verifyID(userID):
    userfile = open("userData.txt",'r')
    #loops through whole file
    for line in userfile:
        fileID, filePIN = line.strip().split("#")  
        if userID == fileID:
            return 1     
    return 0             

def verifyUser(userID,pin):
    userfile = open("userData.txt",'r')
    #loops through whole file
    for line in userfile:
        fileID, filePIN = line.strip().split("#")  
        if userID == fileID and pin == filePIN:
            return 1
        fileID, filePIN = line.strip().split("#")
    userfile.close()
    return 0



def verifyPIN(newPIN):
    if len(newPIN) == 4:
        return 1
    else:
        return 0

def pgbreak():
        print("-----------------------------------------------")