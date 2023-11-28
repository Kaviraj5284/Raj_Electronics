import mysql.connector

# connection = mysql.connector.connect(
#     host="localhost",
#     user="your_username",
#     password="your_password",
#     database="your_database"
# )

def Accessories():
    ch=int(input("Id : "))
    global i
    f=0
    r=0
    for n in range(0,i):
        if Id[n]==ch:
            f=1
            print("--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t\t\tRaj Electronics")
            print("--------------------------------------------------------------------------------------------")
            print("Headphones\t\t\t\t\t\t\t\t\t\tEarbuds")
            print("--------------------------------------\t\t\t------------------------------------------")
            print("1. Boat Rockerz 450 Pro............1999\t\t\t11. Boat Airdopes 131.................1299\n2. Sony WH-CH510...................2990\t\t\t12. Boult Audio Airbass Combuds.......1299\n3. JBL T500BT......................3149\t\t\t13. Noise Buds VS202..................1599\n4. MOTOROLA Escape 210.............1499\t\t\t14. Wecool Moonwalk M3-V2..............999\n5. MI Super Bass...................1799\t\t\t15. Realme Buds Q2 Neo................1599")
            print("------------------------------------------------------------------------------------------")
            print("Refrigirator Accessories\t\t\t\t\t\tTelevision Accessories")
            print("--------------------------------------\t\t\t------------------------------------------")
            print("6. Fridge Storage Container.........259\t\t\t16. TV Cover..........................149\n7. Fridge Storage Basket............150\t\t\t17. Remote Cover......................298\n8. Fridge Bottle Shelf..............490\n9. Food Organizer Tray..............219\n10. Ice Cube Tray...................245")
            print("Press 0 to end")
            ch=1
            while(ch!=0):
                ch = int(input(" ->"))
                if ch==1:
                    rs=1999
                    r=r+rs
                elif ch==2:
                    rs=1299
                    r=r+rs
                elif ch==3:
                    rs=1599
                    r=r+rs
                elif ch==4:
                    rs=999
                    r=r+rs
                elif ch==5:
                    rs=1599
                    r=r+rs
                elif ch==6:
                    rs=259
                    r=r+rs
                elif ch==7:
                    rs=150
                    r=r+rs
                elif ch==8:
                    rs=490
                    r=r+rs
                elif ch==9:
                    rs=219
                    r=r+rs
                elif ch==10:
                    rs=245
                    r=r+rs
                elif ch==11:
                    rs=599
                    r=r+rs
                elif ch==12:
                    rs=549
                    r=r+rs
                elif ch==13:
                    rs=1999
                    r=r+rs
                elif ch==14:
                    rs=649
                    r=r+rs
                elif ch==15:
                    rs=999
                    r=r+rs
                elif ch==16:
                    rs=149
                    r=r+rs
                elif ch==17:
                    rs=298
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("WRONG CHOICE....!!!")
            print("Total Bill :",r)
            print("Item is added in Cart Successfully")
            r = r + rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Id not Valid")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()