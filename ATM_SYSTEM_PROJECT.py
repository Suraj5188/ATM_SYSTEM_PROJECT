#ATM_SYSTEM_PROJECT

#importing require module
import random
import time
import csv


#decalre
amount=30000
print("\n------------------------------------Welcome-------------------------------\n")

print("\n")


import csv
f=open("file.csv","r")
csvr1=csv.reader(f)
found=0
ml=[]
cardnumber=input("Enter card number:")
for r in csvr1:
    if (r[0]==cardnumber):
        print("you can continue")
        atm_pin=input("Enter pin number:")
        
        if (r[5]==atm_pin):
            print("you can continue")
            break
        else:
            print("Wrong")
        exit()
else:
    print("Wrong")
    exit()


#--user choice---
def get_input2(): 
    amount_withdraw=int(input("Enter amount to withdraw:"))
    return amount_withdraw

#--------if user selected saving account----------

#1:saving
def saving():

    x=get_input2()
    f=open("file.csv","r")
    csvr=csv.reader(f)
    found=0
    ml=[]
    
    for r in csvr:
        if (r[0]==cardnumber):
            r[3]=int(r[3])-int(x)
            #r[3]=int(input("Enter amount:"))
            found=1
            print(f"\n----------Your Reamaining Balance is:  {r[3]}Rs --------------")
    
        ml.append(r)
    f.close()
    if found==0:
        time.sleep(2)
        print("Data not found")
    else:
        f=open("file.csv","w",newline='')
        csvr=csv.writer(f)
        csvr.writerows(ml)
        f.close()
        time.sleep(2)
        return "\n\t-------------Thank you!---------------------\n"

#--------if user selected current account--------

# 2:current
def current():
    y=get_input2()
    f=open("file.csv","r")
    csvr=csv.reader(f)
    found=0
    ml=[]
    
    for r in csvr:
        if (r[0]==cardnumber):
            r[3]=int(r[3])-int(y)
            #r[3]=int(input("Enter amount:"))
            found=1
            print(f"\n----------Your Reamaining Balance is: {r[3]}")
    
        ml.append(r)
    f.close()
    if found==0:
        time.sleep(2)
        print("Data not found")
    else:
        f=open("file.csv","w",newline='')
        csvr=csv.writer(f)
        csvr.writerows(ml)
        f.close()
        time.sleep(2)
        return "\n\t-------------Thank you!-------------------"


#------if user slected for other operations------------

# 3:other
def other():
    
    #------------------other-------------------
    print("\n-----------------------------select choice--------------------------\n\n\t1.pinchange\n\t2.Block card\n")

    oprations2={
        1:Pin_change,
        2:Block_card    
    }


    choice2=int(input("Enter Your choice: "))
    output2=oprations2.get(choice2,errorhandler_2)()
    print(output2)

#function for if user selected ---"other"---1.pinchange---2.block card--
#1:Pin_change,
#2:Block_card

def get_input():
    cardnumber=input("Enter cardn number:")  
    return cardnumber
    
#-------------------if user have to change the pin-----------------

#1.Pinchange
def Pin_change():

    c1=get_input()
    f=open("file.csv","r")
    csvr=csv.reader(f)
    found=0
    ml=[]

    for r in csvr:
        if (r[0]==c1):
            print("Now verify the otp\n")
            otp=random.randrange(100000,1000000)
            time.sleep(4)#sleep methood
            print(f"---You Generated otp is:    {otp}")

            user=int(input("\t\nVerify By Entering otp:"))
            if(user==otp):
                r[5]=int(input("Enter new pin:"))
                print("\nPin changed successfully")
                #print(r)
                found=1
            else:
                print("Invalid OTP")
        ml.append(r)
    f.close()
    if found==0:
        print("Data not found")
    else:
        f=open("file.csv","w",newline='')
        csvr=csv.writer(f)
        csvr.writerows(ml)
        f.close()

    return "\n------Thank you!!-------------"

#----------------if user want to the block the card----------------------
#2.Block card
def Block_card():
    c2=get_input()
    f=open("file.csv","r")
    csvr=csv.reader(f)
    found=0
    ml=[]

    for r in csvr:
        if (r[0]==c2):
            print("Now verify the otp\n")
            otp=random.randrange(100000,1000000)
            time.sleep(4)#sleep methood
            print(f"---You Generated otp is:    {otp}")

            user=int(input("\t\nVerify By Entering otp:"))
            if(user==otp):
                r[6]="BLOCK"
                print("\nAccess Blocked successfully")
                #print(r)
                found=1
            else:
                print("Invalid OTP")
        ml.append(r)
    f.close()
    if found==0:
        print("Data not found")
    else:
        f=open("file.csv","w",newline='')
        csvr=csv.writer(f)
        csvr.writerows(ml)
        f.close()

    return "\n------Thank you!!-------------"
    

#------------------if user enter differnt number-----------
def errorhandler_2():
   return "Invalid soRRy!"

#------------------if user enter differnt number------------
def errorhandler():
    return "Invalid soRRy!"
    
#sleep methood
time.sleep(2)

print("\n------------------------------Select Choice---------------------------\n")

#user can select at least one out of three
print("\t1.saving \n\t2.current \n\t3.other\n")

oprations={
    1:saving,
    2:current,
    3:other
    }

#use choice
choice=int(input("Enter Your choice: "))
output=oprations.get(choice,errorhandler)()
print(output)
