import json
import random 
import string
from pathlib import Path




class Bank:

    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("There is no suchh file exists")
    except Exception as err:
        print(f'an exception occuredd as {err}')

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%&*^", k=1)
        id  = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)



    def createAccount(self):
        info= {
            "name" : input("Enter your name : "),
            "age" : int(input("Enter your age : ")),
            "email": input("Enter your Email : "),
            "pin" : int(input("Enter your pin : ")),
            "accountNo"  : self.__accountGenerate(),
            "balance" : 0
        }
        if info['age'] <18:
            print("Sorry! You are not eligible for creating an account")
        elif len(str(info['pin'])) != 4:
            print("Pin should  4 digits only")
        else:
            print("Your Account created Succesfully!")
            for i in info:
                print(f"{i} : {info[i]}")

            print("Please Remember your Account Number.")

            Bank.data.append(info)

            Bank.__update()

    def deposit(self):
        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter your PIN : ")) 

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin ]

        if userdata == False:
            print("Sorry! No data Found")
        else:
            amount = int(input("Enter the Deposit Amount: "))
            if amount > 10000 or amount <0 :
                print("Sorry! The amount is too much.You can deposit above 0 and below 10000 ")
            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"Amount {amount} Deposited Succesfully in {userdata[0]['accountNo']}")
                print(f"Balance : {userdata[0]['balance']}")



    def withdraw(self):
             accnumber = input("Enter Your Account Number :")
             pin = int(input("Enter your PIN : ")) 

             userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin ]

             if userdata == False:
                print("Sorry! No data Found")
             else:
                amount = int(input("Enter the Withdrawl Amount: "))
                if userdata[0]['balance'] < amount:
                     print("Sorry!You Dont have that much money ")
                else:
                    print(userdata)
                    userdata[0]['balance'] -= amount
                    Bank.__update()
                    print(f"Amount {amount} Withdrew Succesfully from {userdata[0]['accountNo']}")
                    print(f"Balance : {userdata[0]['balance']}")

    def showDetails(self):
        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter your PIN : ")) 

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        print(userdata)
        if userdata == False:
            print("Enter the Correct details")
        else:
            print("\nUser Details : \n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")


    def updateDetails(self):

        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter your PIN : ")) 
        
        userdata = [i for i in Bank.data if i['accountNo']==accnumber and i['pin'] == pin ]

        if userdata == False:
            print("No such User Found!")
        else:
            print("You  cant change the age, accountNo ,balance")
            print("Fill the deatils for change or leave it empty if no change")

            newdata = {
                "name" : input("Enter your name here or press enter to skip : "),
                "email" : input("Enter your new Email or press enter to skip : "),
                "pin" : input("Enter your new pin   here or press enter to skip : ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']

            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']
            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin'] )== str:
                newdata['pin'] == int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            
            Bank.__update()
            print("Your Details Updated succesfully")
    
    def deleteAccount(self):
        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter your PIN : ")) 

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such Data exists!")
        else:
            check = input("Press Y if you want to delete your account or press N : ")
            if check == 'n' or check == 'N':
                print("NO changes made in your account!")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Your Account Deleted Successfully")
                Bank.__update()        


# user is a object created using the Bank class 

user = Bank()

# options for the user to to 

print("Press 1 for create an account")
print("Press 2 for Deposit Money in the Bank")
print("Press 3 for withdrawing money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting your account")


check = int(input("Tell your Response :"))

if check ==1:
    user.createAccount()

if check ==2:
    user.deposit()

if check == 3:
    user.withdraw()

if check ==4:
    user.showDetails()

if check == 5:
    user.updateDetails()

if check == 6:
    user.deleteAccount()