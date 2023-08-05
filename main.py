                                                            #IMPORTING ALL THE FUNCTIONS
import mysql.connector
from railway_function import dataBase, Tables, railresmenu, traindetail, reservation, cancel, displayticket, printtraindetails,main_program
                                                                            

'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
                                                            #CONNECTING MYSQL WITH PYTHON
mydb=mysql.connector.connect(host="localhost",user="root",password="osmosis1080");
mycursor=mydb.cursor()

pnr=0                                               #MADE GLOBAL FOR USING IN FUNCTIONS

                                                                    #CALLING FUNCTIONS
main_program()








#MODULES TO BE IMPORTED ON A NEW DESKTOP :
#1) datetime
#2) plyer
#3) string
#4) sys
#5) pywhatkit
#6)random
