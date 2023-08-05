import mysql.connector  #FOR CONNECTING MYSQL WITH PYTHON
import datetime          #FOR SHOWING DATE & TIME ON TOP
import sys                 #FOR SHOWING ERRORS
import string              #FOR USING UPPER FUNCTION & CENTER
import emojis             #FOR INSERTING EMOJIS
import pywhatkit   #FOR GETTING WHATSAPP MESSAGE FOR OTP VERIFICATION
import random            #FOR GETTING RANDOM PNR NUMBER
from plyer import notification as railway_notifier #FOR GETTING DESKTOP NOTIFICATIONS
from prettytable import PrettyTable
import pandas as pd

def main_program():
     date=datetime.datetime.now()
     print(date)
     
     heading = 'Hi User !'
     body = 'Welcome to Railway Reservation Sytem Made by Mohd. Ayan & Praful Nigam'
     railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=10,toast=False)

     heading='CBSE COMPUTER SCIENCE PROJECT'
     print(heading.center(170))

     session='SESSION 2020-21'
     print(session.center(175))

     welcome='WELCOME TO THE RAILWAY RESERVATION SYSTEM'
     print(welcome.center(170))

     madeby='DEVELOPED BY PRAFUL NIGAM'
     print(madeby.center(170))

     teacher_name='SUBMITTED TO : MR. PANKAJ AGARWAL'
     print(teacher_name.center(170))

     print("YOUR CONNECTION ID OF MYSQL IS :",mydb.connection_id)
     print('\n')
     
     dataBase()

#CONNECTING WITH MYSQL
mydb=mysql.connector.connect(host="localhost",user="root",passwd="osmosis1080");
mycursor=mydb.cursor()

#MAKING DATABASE
def dataBase():
     pasw = input('ENTER THE PASSWORD : ')
     if pasw == 'user123':
          print('\n')     
          sys.stdout.write("THE ENTERED PASSWORD IS CORRECT !")
          mycursor.execute("create database if not exists Railways_DPS")
          mycursor.execute("use Railways_DPS")
          Tables()
          railresmenu()
           
     else:
          print('\n')
          sys.stderr.write('WRONG PASSWORD')
          print()
          password=input("Press The Enter Key To Try Again : ")
          dataBase()
'''----------------------------------------------------------------------------------------------------------------------------------'''

#TWO TABLES CREATED : 1 of Train Details, 2 of Passenger Details
def Tables():
     sql = "CREATE TABLE if not exists traindetail (\
               tname varchar(30) ,\
               tnum int PRIMARY KEY,\
               ac1 int,\
               ac2 int ,\
               ac3 int ,\
               slp int ,\
               tstartpt varchar(30) ,\
               tdestpt varchar(30) );"
     mycursor.execute(sql)

     sql = "CREATE TABLE if not exists Passengers (\
               pname char(25) ,\
               age char(10) ,\
               ph_no varchar(15),\
               Board_pt varchar(30) ,\
               Dest_pt varchar(30) ,\
               trainno char(15) NOT NULL ,\
               cls char(5) ,\
               amt int ,\
               status varchar(10) ,\
               pnr int PRIMARY KEY);"
     mycursor.execute(sql)
     print()
     railresmenu()

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
                                                                                     #MAIN MENU

def railresmenu():
     heading = 'Hey !'
     body = 'YOU ARE IN THE MAIN MENU'
     railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=5,toast=False)
     print()
     menu="--------------------RAILWAY RESERVATION--------------------"
     print(menu.center(150))
     print()
     print("1. TRAIN DETAIL")
     print("2 .RESERVATION OF TICKET")
     print("3. CANCELLATION OF TICKET")
     print("4. DISPLAY TCKET DEATILS")
     print("5. TRAIN RECORDS")
     print("6. QUIT")
     
     print()         
     n=int(input("KINDLY SELECT A VALID OPTION : "))
     print()
     
     if(n==1):
          traindetail()
     elif(n==2):
          reservation()
     elif(n==3):
          cancel()
     elif(n==4):
          displayticket()
     elif(n==5):
          printtraindetails()
     elif(n==6):
          exit()
     else:
          sys.stderr.write("PLEASE SELECT A VALID OPTION : ")
          railresmenu()
          
          
'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#FUNCTION MADE OF TRAIN DETAILS

def traindetail():
     heading = 'Hey !'
     body = 'YOU ARE INSIDE THE TRAIN DETAILS WINDOW !!'
     railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=5,toast=False)
     
     train_details=("--------------------TRAIN DETAILS--------------------")
     print(train_details.center(150))
     while True:
          l=[]
          name=input("ENTER TRAIN NAME : ")
          print()
          l.append(name)
          print()
          
          try:
               tnum=int(input("ENTER TRAIN NUMBER : "))
               print()
          except ValueError:
               print('\n')
               sys.stderr.write("Please enter Integer value only !!")
               print('\n')
               enter=input("Press the Enter key to Try Again : ")
               print('\n')
               traindetail()
               print('\n')
          l.append(tnum)
          print()
         
          try:
               ac1=int(input("ENTER THE NUMBER OF AC 1 CLASS SEATS : "))
               print('\n')
          except ValueError:
               print('\n')
               sys.stderr.write("Please Enter Integer Value Only !!")
               print('\n')
               enter=input("Press the Enter Key to Try Again : ")
               print('\n')
               traindetail()
               print('\n')
          l.append(ac1)
          print()
          
          try:
               ac2=int(input("ENTER THE NUMBER OF AC 2 CLASS SEATS : "))
               print('\n')
          except ValueError:
               print('\n')
               sys.stderr.write("Please Enter Integer Value only !!")
               print('\n')
               enter=input("Press the Enter Key to Try Again : ")
               print('\n')
               traindetail()
               print('\n')
          l.append(ac2)
          print('\n')
          
          try:
               ac3=int(input("ENTER THE NUMBER OF AC 3 CLASS SEATS : "))
               print('\n')
          except ValueError:
               print('\n')
               sys.stderr.write("Please enter Integer value only !!")
               print('\n')
               enter=input("Press the Enter Key to Try Again : ")
               print('\n')
               traindetail()
               print('\n')
          l.append(ac3)
          print('\n')
          
          
          try:
               slp=int(input("ENTER THE NUMBER OF SLEEPER CLASS SEATS : "))
               print('\n')
          except ValueError:
               print('\n')
               sys.stderr.write("Please Enter Integer Value Only !!")
               print('\n')
               enter=input("Press the Enter Key to Try Again : ")
               print('\n')
               traindetail()
               print('\n')
          l.append(slp)
          print('\n')

          tstartpt= input("Enter the starting Point of the Train : ")
          l.append(tstartpt)
          print('\n')

          tdestpt= input("Enter the Stopping Station of the Train : ")
          l.append(tdestpt)
          print('\n')
          
          train=(l)
          sql="insert into traindetail(tname,tnum,ac1,ac2,ac3,slp,tstartpt,tdestpt)values(%s,%s,%s,%s,%s,%s,%s,%s)"
          mycursor.execute(sql,train)
          mydb.commit()
          print('\n')
          
          heading = 'Yayyyyy !'
          body = 'YOUR DATA IS SUCCESSFULLY INSERTED'
          railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=10,toast=False)

          ch=input("ENTER Yes/Y TO CONTINUE ENTERING DETAIL OR No/N FOR EXITING TO MAIN MENU : ")
          print('\n' *3)
          print("===================================================================")
          if ch.upper() == 'Y':
               traindetail()
               print('\n')
          else :
               railresmenu()
               print('\n')
        
'''---------------------------------------------------------------------------------------------------------------------------------'''
                                                                                  #RESERVATION FUNCTION

def reservation():
          heading = 'Hey !'
          body = 'YOU ARE INSIDE THE RESERVATION WINDOW !!'
          railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=5,toast=False)
          global pnr
          l1=[]
          
          reserve="--------------------RESERVATION WINDOW--------------------"
          print(reserve.center(150))
          print('\n')
          
          pname=input("ENTER THE NAME OF PASSENGER : ")
          l1.append(pname)
          print('\n')
          
          try:
               age=int(input("ENTER THE AGE OF PASSENGER : "))
          except ValueError:
               print('\n')
               sys.stderr.write("Please Enter Integer Value Only !!")
               print('\n')
               enter=input("Press the Enter Key to Try Again : ")
               print('\n')
               reservation()
               print('\n')
          l1.append(age)
          print('\n')

          ph_no = input('ENTER YOUR PHONE NUMBER WITH + SIGN & COUNTRY CODE : ')
          print('\n')
          l1.append(ph_no)
          print('\n')

          Board_pt= input('Enter the Boarding Station : ')
          l1.append(Board_pt)
          print('\n')

          Dest_pt= input('Enter the Destination Station : ')
          l1.append(Dest_pt)
          print('\n')
          
          
          try:
               
               trainno=int(input("ENTER TRAIN NUMBER : "))
               print('\n')
          except ValueError:
               print('\n')
               sys.stderr.write("Please Enter Integer Value Only !!")
               print('\n')
               enter=input("Press the Enter Key to Try Again : ")
               print('\n')
               reservation()
               print('\n')
          l1.append(trainno)
          print('\n')
          
          print("SELECT A CLASS FOR PASSENGER")
          print()
          print("1. AC FIRST CLASS")
          print("2. AC SECOND CLASS")
          print("3. AC THIRD CLASS")
          print("4. SLEEPER CLASS")
          print('\n')
          
          cp=int(input("ENTER THE CLASS NUMBER : "))
          if(cp==1):
               amount=1000
               cls='ac1'
          elif(cp==2):
               amount=800
               cls='ac2'
          elif(cp==3):
               amount=500
               cls='ac3'
          else:
               amount=350
               cls='slp'
          l1.append(cls)
          print('\n')
                                                                                #WHATSAPP MESSAGE FUNCTION
          pywhatkit.sendwhatmsg(ph_no,'Your Unique OTP of Railway Reservation is : 5430',hr,mim)
          print('\n')
          
                                                                                     #OTP SYSTEM
          otp=input("Enter The OTP : ")
          if otp=='5430':
               print("STATUS : CONFIRMED")
               print('\n')
               print("TOTAL AMOUNT TO BE PAID : ",amount)
               l1.append(amount)
               print('\n')

                                                                           #RANDOM PNR GENERATING OF 4 NUMBERS
               
               pnr=random.randint(1000,9999)
               print("PNR NUMBER : ",pnr)
               print('\n')
               heading = 'Thank You For Booking Your Ticket !!'
               body = 'Have a Safe Journey !'
               railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=5,toast=False)
          else:
               print("The Entered OTP is Wrong !!")
               print('\n')
               trying=input("Press the Enter Key to again Book the Ticket : ")
               print('\n')
               reservation()
               print('\n')
          
          status='conf'
          l1.append(status)
          l1.append(pnr)
          train1=(l1)         
          sql="insert into passengers(pname,age,ph_no,Board_pt,Dest_pt,trainno,cls,amt,status,pnr)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
          mycursor.execute(sql,train1)
          mydb.commit()
          print('\n')
          
          print("WISHING TO GO BACK TO MENU ?? ")
          d=input("Press Yes/Y for going OR NO/N to exit : ")
     
          if d.upper()=='Y' or d=='Yes' or d=='YES':
               print('\n' *3)
          else:
               exit()

          print("====================================================================================================================")
          railresmenu()

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def cancel():
          heading = 'Hey !'
          body = 'YOU ARE INSIDE THE TICKET CANCELLATION WINDOW !!'
          railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=5,toast=False)
          global pnr
          cancelation=("--------------------TICKET CANCELLATION WINDOW--------------------")
          print(cancelation.center(150))
          print()
          try:
               pnr=int(input("ENTER PNR NUMBER : "))
          except ValueError:
               print('\n')
               sys.stderr.write("Please Enter PNR NO. In Integer Value Only !!")
               print('\n')
               enter=input("Press the Enter Key to Try Again : ")
               print('\n')
               cancel()
               print('\n')
          print()
          sql="select * from passengers where pnr = %s"
          pn=(pnr,)
          sql="update passengers set status='Deleted' where pnr=%s"
          mycursor.execute(sql,pn)
          mydb.commit()
          print("DELETION COMPLETED")
          print()
          
          print("GO BACK TO MENU")
          print('\n' *2)

          print("===================================================================")
          railresmenu()


'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def displayticket():
          heading = 'Hey !'
          body = 'YOU ARE INSIDE THE PNR STATUS WINDOW !!'
          railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=5,toast=False)
          global pnr
          print('\n')
          pnr_status=("--------------------PNR STATUS WINDOW--------------------")
          print(pnr_status.center(150))
          print('\n')
          
          try:
               pnr=int(input("ENTER PNR NUMBER : "))
          except ValueError:
               print('\n')
               sys.stderr.write("Please Enter PNR NO. In Integer Value Only !!")
               print('\n')
               enter=input("Press the Enter Key to Try Again : ")
               print('\n')
               displayPNR()
               print('\n')
          pn= (pnr,)
          sql="select * from passengers where pnr=%s"
          mycursor.execute(sql,pn)
          res = mycursor.fetchall() 
          print("PNR STATUS ARE AS FOLLOWS : ")
          print('\n')
          
          print("( NAME , AGE , PH_NO,BOARDING POINT,DESTINATION POINT, TRAIN NO , NO_of_PASSENGERS, CLASS , AMT , STATUS , PNR)")
          
          for x in res:
               print(x)
          print('\n')    
          print("DO YOU WISH TO GO BACK TO MENU ??")
          print('\n')
          d=input("Press Yes/Y for going OR NO/N to exit : ")
     
          if d.upper()=='Y' or d=='Yes' or d=='YES':
               print('\n' *3)

               print("===================================================================")
               railresmenu()
          else:
               exit()

'''------------------------------------------------------------------------------------------------------------------'''
def printtraindetails():
     heading = 'Hey !'
     body = 'YOU ARE INSIDE THE DISPLAY TRAIN DETAILS WINDOW !!'
     railway_notifier.notify(title=heading,message=body,app_name='Python',app_icon=None,timeout=5,toast=False)
     
     print('\n')
     trains=("--------------------TRAIN DETAILS WINDOW--------------------")
     print(trains.center(150))
     print('\n')
     sql = 'select * from traindetail'
     mycursor.execute(sql,)
     res = mycursor.fetchall()
     '''mytable = PrettyTable([' Train Name ' ,' Train Num ', '  AC 1  ' , '  AC 2 ',  '  AC 3 ' , ' SLP CLASS ',  ' Boarding Pt ', ' Dest Pt'])
      mytable.add_row([x])'''
     for x in res:
          print(x)
     df = pd.DataFrame([res])
     print('\n')    
     print("DO YOU WISH TO GO BACK TO MENU ??")
     print('\n')
     d=input("Press Yes/Y for going OR NO/N to exit : ")
     
     if d.upper()=='Y' or d=='Yes' or d=='YES':
          print('\n' *3)

          print("===================================================================")
          railresmenu()
     else:
          exit()
