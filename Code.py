# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 14:37:21 2022

@author: 91781
"""


import pandas as pd
import matplotlib.pyplot as plt



def menu():
    print("HOTEL MANAGEMENT SYSTEM Project")
    print("1.  About the Project")
    print("2.  Show all customers details")
    print("3.  Show Types of Rooms in hotel")
    print("4.  Avaliable rooms for booking")
    print("5.  Room rent and bill according to stay")
    print("6.  Booking")
    print("7.  Sort customer Detail by Name")
    print("8.  Rent Increment")
    print("9.  Laundry")
    print("10. Laundry Bill")
    print("11. Delete Column")
    print("12. Show all Games Avaliable")
    print("13. Game Bill")
    print("14. Show Menu of Restaurant")
    print("15. Restaurant Bill") 
    print("16. Checkout")
    print("17. Line Plot")
    print("18. Bar Plot") 
    print("19. Barh Plot")
    print("20. Histogram")
    print()
    
menu()

def about():
    print("The Project is developed on HOTEL MANAGEMENT SYSTEM. It contains 20 options. In the Project CSV files are used- Customers, Room type, Laundry, Games, Restaurant")
    print()

def costumer_details():
    df=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\costumer.csv") 
    df=df.set_index('MOBILE NO')
    print(df)

def show_roomtype():
    print("Show Types of Rooms Available")
    df=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\typesofroom.csv",index_col=0)
    print()
    print(df)
    
def avaliable_rooms():
    df=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\roomstatus.csv")
    df = df.set_index('ROOMNO')
    df1=df.loc[(df['STATUS']=='unbooked')]
    print(df1)
      
def roomrent():
    print ("Room amenities include: 1 Double Bed, Television, Telephone, Double-Door Cupboard, 1 Coffee table with  sofa, Balcony and an attached washroom with hot/cold water.") 
    print("WE HAVE THE FOLLOWING ROOMS FOR YOU:-") 
    print()
    print ("1. Single/without ac Room Rs 1000 Per Night") 
    print ("2. Single/with ac Rs 1200 Per Night")
    print ("3. Double/without ac Rs 1900 Per Night")
    print ("4. Double/with ac Rs 2350  Per Night")
    print ("5. Silver Rs 4000  Per Night")
    print ("6. Gold Room Rs 5000  Per Night")
    x=int(input("ENTER YOUR CHOICE PLEASE->"))
    n=int(input("FOR HOW MANY NIGHTS YOU WANTED TO STAY:"))
    if(x==1): 
        print ("YOU HAVE CHOSEN- Single/without ac Room")
        S=1000*n
    elif (x==2): 
        print ("YOU HAVE CHOSEN- Single/with ac  Room")
        S=1200*n
    elif (x==3): 
        print ("YOU HAVE CHOSEN- Double/without ac")
        S=1900*n
    elif (x==4):
        print ("YOU HAVE CHOSEN- Double/with ac")
        S=2350*n
    elif (x==5) ("YOU HAVE CHOSEN- silver"):
        S=4000*n
        print()
    elif (x==6) ("YOU HAVE CHOSEN- gold"):
        S=5000*n
        print()
    else:
        print ("PLEASE CHOOSE A ROOM") 
    print ("your room rent is =",S,"\n Thank You Visit Again")
   
    
   
def booking():
    df=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\roomstatus.csv")
    df = df.set_index('ROOMNO')
    roomno=int(input("Enter your room number you want to book:"))
    if roomno== 101:
        df.loc[101,'STATUS']='booked'
    elif roomno== 102:
        df.loc[102,'STATUS']='booked'
    elif roomno== 103:
        df.loc[103,'STATUS']='booked'
    elif roomno== 104:
        df.loc[104,'STATUS']='booked'
    elif roomno== 105:
        df.loc[105,'STATUS']='booked'
    elif roomno== 106:
        df.loc[106,'STATUS']='booked'
    elif roomno== 201:
        df.loc[201,'STATUS']='booked'
    elif roomno== 202:
        df.loc[202,'STATUS']='booked'
    elif roomno== 203:
        df.loc[203,'STATUS']='booked'
    elif roomno== 204:
        df.loc[204,'STATUS']='booked'
    elif roomno== 205:
        df.loc[205,'STATUS']='booked'
    elif roomno== 206:
        df.loc[206,'STATUS']='booked'
    elif roomno== 301:
        df.loc[301,'STATUS']='booked'
    elif roomno== 302:
        df.loc[302,'STATUS']='booked'
    elif roomno== 303:
        df.loc[303,'STATUS']='booked'
    elif roomno== 304:
        df.loc[304,'STATUS']='booked'
    elif roomno== 305:
        df.loc[305,'STATUS']='booked'
    elif roomno== 306:
        df.loc[306,'STATUS']='booked'
        print()
    df.to_csv(r"C:\Users\user\Desktop\Hotel Management system\roomstatus.csv")
    df1=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\costumer.csv") 
    df1.set_index('MOBILE NO',inplace=True)
    name=input("Enter your name: ")
    address= input("Enter your address: ")
    phno= int(input("Enter your phone number: "))
    checkin=input("Enter the check in date: ")
    checkout=''
    df1.loc[phno]=[name, address, checkin,checkout,roomno]
    print(df1)
    df1.to_csv(r"C:\Users\user\Desktop\Hotel Management system\costumer.csv")


def sort_customer():
    print("sorting Customers names and details in Ascending order")
    df=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\costumer.csv", index_col=0) 
    df=df.sort_values("NAME")
    print (df)

def rent_increment() :
    print("Previous Rent of Rooms")
    df= pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\availrooms.csv", index_col=0)
    print (df)
    print("increase rent by Rs. 500") 
    df['CHARGES']+=500
    print (df)

def laundry():
    df=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\laundarydetails.csv", index_col=0) 
    print (df)

def lbill():
    print ("WE Charge THE FOLLOWING rate for Laundry:-")
    print ("1. kids wear RS 30 1 Piece")
    print ("2. Trouser RS 20 1 Piece")
    print ("3. shirts/tshirts RS 150 1 Piece")
    print ("4. shorts/skin RS 30 1 Piece")
    print ("5. sweater RS 100 1 Piece")
    print ("6. coat RS 200 1 Piece")
    print ("7. footwear RS 150 1 Piece")
    print ("8. others RS 180 1 Piece ")
    x=int(input("ENTER YOUR CHOICE OF CLOTH PLEASE->")) 
    n=int(input("How many Pieces you want to get washed: ")) 
    if(x==1):
        print ("You want to get kids wear washed")
        S=30*n 
    elif (x==2): 
        print ("YOU want to get Shirt/tshirt washed") 
        S=20*n
    elif(x==3):
        print ("YOU want to get jeans/pants washed") 
        S= 50*n
    elif (x==4):
        print ("YOU want to get shorts/skirts washed")
        S=30*n
    elif (x==5):
        print ("You want to get sweater Cloth washed")
        S=100*n
    elif (x==6): 
        print ("YOU want to get coat washed") 
        S=200*n
    elif (x==7): 
        print ("YOU want to get footwear washed") 
        S=150*n
    elif (x==8): 
        print ("YOU want to get others washed") 
        S=180*n
    else:
        print ("PLEASE CHOOSE A Piece of cloth") 
    print ("your Laundry Charges are Rs. =",S,"\n")


def delete_col():
    print('Delete column address from customers')
    df=pd.read_csv (r"C:\Users\user\Desktop\Hotel Management system\costumer.csv")
    print(df)
    print()
    del df [ 'ADDRESS'] 
    print (df)


def show_game(): 
    print("ALL Games available") 
    df=pd.read_csv (r"C:\Users\user\Desktop\Hotel Management system\gamedetails.csv",index_col=0) 
    print(df)

def gamebill():
    print("________GAME MENU_______")
    df=pd.read_csv (r"C:\Users\user\Desktop\Hotel Management system\gamedetails.csv",index_col=0)
    print(df)
    g= int(input ("Enter your choice of Game :"))
    if (g == 1):
        h = int(input("No. of hours:"))
        S = 100* h
    elif (g == 2):
        h= int(input("No. of hours"))
        S= 90 * h
    elif (g == 3):
        h = int(input("No. of hours:"))
        S= 120 *h
    elif (g == 4):
        h = int(input("No. of hours:"))
        S= 150 * h
    elif (g == 5):
        h = int(input("No. of hours:"))
        S = 200 * h
    elif (g == 6):
        h = int(input("No. of hours:"))
        S = 400 * h
    else:
        print("Invalid option") 
    print("Total Game BiLL=Rs",S,"\n")


def show_restaurant():
    print("_____MENU_____")
    df=pd.read_csv (r"C:\Users\user\Desktop\Hotel Management system\menu.csv",index_col=0) 
    print(df)


def restaurantbill():
    print("ALL Food Items available") 
    df=pd.read_csv (r"C:\Users\user\Desktop\Hotel Management system\menu.csv",index_col=0) 
    print (df)
    print()
    c = int(input("Order your ITEM No. :")) 
    d = int(input("Enter the quantity:"))
    if (c == 1):
       S = 120*d
    elif (c == 2):
       S = 200*d
    elif (c == 3):
       S = 150*d
    elif (c == 4):
       S = 80*d
    elif (c == 5):
       S = 40*d
    elif (c == 6):
       S = 15*d
    elif (c == 7):
       S = 20*d
    elif (c == 8):
       S=25*d
    elif (c == 9):
       S=30*d
    else:
        print("Invalid option")
    print("Total food Bill is Rs",S,"\n")
    

def checkout():
    df=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\roomstatus.csv")
    df = df.set_index('ROOMNO')
    print(df)
    roomno=int(input("Enter your room number:"))
    if roomno== 101:
        df.loc[101,'STATUS']='unbooked'
    elif roomno== 102:
        df.loc[102,'STATUS']='unbooked'
    elif roomno== 103:
        df.loc[103,'STATUS']='unbooked'
    elif roomno== 104:
        df.loc[104,'STATUS']='unbooked'
    elif roomno== 105:
        df.loc[105,'STATUS']='unbooked'
    elif roomno== 106:
        df.loc[106,'STATUS']='unbooked'
    elif roomno== 201:
        df.loc[201,'STATUS']='unbooked'
    elif roomno== 202:
        df.loc[202,'STATUS']='unbooked'
    elif roomno== 203:
        df.loc[203,'STATUS']='unbooked'
    elif roomno== 204:
        df.loc[204,'STATUS']='unbooked'
    elif roomno== 205:
        df.loc[205,'STATUS']='unbooked'
    elif roomno== 206:
        df.loc[206,'STATUS']='unbooked'
    elif roomno== 301:
        df.loc[301,'STATUS']='unbooked'
    elif roomno== 302:
        df.loc[302,'STATUS']='unbooked'
    elif roomno== 303:
        df.loc[303,'STATUS']='unbooked'
    elif roomno== 304:
        df.loc[304,'STATUS']='unbooked'
    elif roomno== 305:
        df.loc[305,'STATUS']='unbooked'
    elif roomno== 306:
        df.loc[306,'STATUS']='unbooked'
        print()
    df.to_csv(r"C:\Users\user\Desktop\Hotel Management system\roomstatus.csv")
    df1=pd.read_csv(r"C:\Users\91781\OneDrive\Desktop\new\costumer.csv")
    df1.set_index('MOBILE NO',inplace=True)
    mobile=int(input("Enter mobile number you enter earlier:"))
    checkout=input("Enter your check out date:")
    df1.loc[[mobile],['CHECKOUT']]=checkout    
    df1.to_csv(r"C:\Users\91781\OneDrive\Desktop\new\costumer.csv")
    print(df1)

def line_plot():
    print("Line plot")
    df=pd.read_csv (r"C:\Users\user\Desktop\Hotel Management system\typesofroom.csv") 
    print(df)
    x1=df["TYPE"]
    y1=df["CHARGES"]
    plt.xlabel("Types of Rooms",fontsize=10)
    plt.ylabel("Rent of Rooms", fontsize=10) 
    plt.xticks(rotation=30)
    plt.yticks(rotation=30)
    plt.plot(x1, y1,linewidth=5, color='orange', linestyle='--')
    plt.grid()
    plt.title('TYPE OF ROOMS AND THEIR RENT PER NIGHT', fontsize=14, color="r") 
    plt.show()

def bar_plot():
    print('bar plot')
    df=pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\gamedetails.csv") 
    print(df)
    x1=df["GAME NAME"]
    y1=df["CHARGES"]
    plt.xlabel("Types of GAMES", fontsize=14, color='r')
    plt.ylabel("Charges", fontsize=14, color='r')
    plt.xticks(rotation=30)
    plt.yticks(rotation=30)
    plt.title("Type of games and their Rate/hour",fontsize=14, color="r")
    plt.bar(x1, y1, facecolor="purple", edgecolor="yellow")
    plt.show()

def barh_plot():
    print("Horizontal bar plot")
    df=pd.read_csv (r"C:\Users\user\Desktop\Hotel Management system\menu.csv") 
    print (df)
    x=df[ 'ITEM']
    y=df['CHARGES']
    plt.title("ITEM Names and Rates", fontsize=14, color="r")
    plt.xlabel('ITEMS Names', fontsize=14,color='k')
    plt.ylabel('RATE', fontsize=14, color='k')
    plt.barh(x,y,color= 'm',edgecolor='black')
    plt.show()

def histogram():
    print("Histogram")
    df= pd.read_csv(r"C:\Users\user\Desktop\Hotel Management system\laundarydetails.csv")
    print(df)
    x=df['ITEM NAME']
    plt.xticks(rotation=30)
    plt.yticks(rotation=30)
    plt.title("Laundry Items and its charges")
    plt.hist(x,bins=6, color='cyan',edgecolor='black', hatch='o')
    plt.show()
    

opt=""
opt=int(input("enter your choice: "))

if opt==1:
    about()
elif opt==2:
    costumer_details()
elif opt==3:
    show_roomtype()
elif opt==4:
    avaliable_rooms()
elif opt==5:
    roomrent()    
elif opt==6:
    booking()
elif opt==7:
    sort_customer()
elif opt==8:
    rent_increment()
elif opt==9:
    laundry()
elif opt ==10:
    lbill()
elif opt==11:
    delete_col()   
elif opt==12:
    show_game()
elif opt==13:
    gamebill()
elif opt==14:
    show_restaurant()
elif opt==15:
    restaurantbill()
elif opt==16:
    checkout()
elif opt==17:
    line_plot()
elif opt==18:
    bar_plot()
elif opt==19: 
    barh_plot()
elif opt==20:
    histogram()
else:
    print("invalid option")
import winsound 
winsound.Beep(1000, 300)


