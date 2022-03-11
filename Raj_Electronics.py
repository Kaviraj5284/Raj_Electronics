import qrcode
import random
import pyfiglet
import datetime
import time

# Global List Declaration
name = []
phno = []
date = []
price = []
Id = []
add = []
billing_date = []
day = []
rc = []
p = []
# Global Variable Declaration
i = 0
# Home Function
def home():
    result = pyfiglet.figlet_format("           Raj  Electronics")
    print(result)
    print("\t\t\t1 Booking\n")
    print("\t\t\t2 Accessories\n")
    print("\t\t\t3 Payment\n")
    print("\t\t\t4 Record\n")
    print("\t\t\t0 Exit\n")
    choose = int(input("Press value b/w (0 to 4)\n->"))
    if choose == 1:
        Booking()
    elif choose == 2:
        Accessories()
    elif choose == 3:
        Payment()
    elif choose == 4:
        Record()
    else:
        exit()


def Booking():
    # used global keyword to
    # use global variable 'i'
    global i
    print(" BOOKING ")
    while 1:
        n = str(input("Name: "))
        p1 = str(input("Phone No.: "))
        a = str(input("Address: "))

        # checks if any field is not empty
        if n != "" and p1 != "" and a != "":
            name.append(n)
            add.append(a)
            break

        else:
            print("\tName, Phone no. & Address cannot be empty..!!")

            # id for customer
    Cid = random.randrange(40) + 10

    # checks if alloted room no. & customer
    # id already not alloted
    while Cid in Id:
        Cid = random.randrange(60) + 10
    rc.append(0)
    p.append(0)
    if p1 not in phno:
        phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 1:
                    phno.append(p1)
    elif p1 in phno:
        for n in range(0, i):
            if p1 == phno[n]:
                if p[n] == 0:
                    print("\tPhone no. already exists and payment yet not done..!!")
                    name.pop(i)
                    add.pop(i)
                    billing_date.pop(i)
                    Booking()
    print("")
    print("\t\t\t***REGISTRATION SUCCESSFULLY***\n")
    print("Id - ", Cid)
    Id.append(Cid)
    i = i + 1
    print("Select Electronics Items")
    print("1. Mobile Phones")
    print("2. Television")
    print("3. Refrigirator")
    print("\t\tPress 0 for ALL Electronics Items ")
    choose = int(input("->"))
    if choose == 0:
        print("--------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\tRaj Electronics")
        print("--------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\t  Mobile Phones")
        print("--------------------------------------------------------------------------------------------")
        print("\n MI Mobile Info\t\t\t\t\t\t\t\t\t\t\tVivo Mobile Info")
        print("-------------------------------------\t\t----------------------------------------")
        print(" 1 Xiaomi 11T pro 5G\t\t\t\t\t\t 16 Vivo Y75 5G\n\tDisplay : 6.58 inches\t\t\t\t\t\tDisplay : 6.67 inches\n\tProcessor : Octa core Dimensity 700\t\t\tProcessor : Qualcomm Snapdragon 888\n\tRam : 8 GB\t\t\t\t\t\t\t\t\tRam : 8 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 20MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 50MP + 2MP + 2MP\t\t\t\tBack Camera : 108MP + 8MP + 5MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 5000mAh\n\tPrice : 21,990.00\t\t\t\t\t\t\tPrice : 43,999.00\n-------------------------------------------------------------------------------------")
        print(" 2 Xiaomi Redmi Mi 10T\t\t\t\t\t\t 17 Vivo Y72 5G\n\tDisplay : 6.67 inches\t\t\t\t\t\tDisplay : 6.58 inches\n\tProcessor : Qualcomm Snapdragon 865 OC\t\tProcessor : Mediatek MT6833 Dimensity 700\n\tRam : 6 GB\t\t\t\t\t\t\t\t\tRam : 6 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 20MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 64MP + 13MP + 5MP\t\t\t\tBack Camera : 64MP + 8MP + 2MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 5000mAh\n\tPrice : 21,694.00\t\t\t\t\t\t\tPrice : 19,999\n-------------------------------------------------------------------------------------")
        print(" 3 Redmi Note 11t 5G\t\t\t\t\t\t 18 vivo V20 SE\n\tDisplay : 6.6 inches\t\t\t\t\t\tDisplay : 6.44 inches\n\tProcessor : Mediatek Dimensity 810 OC\t\tProcessor : Qualcomm Snapdragon 665\n\tRam : 8 GB\t\t\t\t\t\t\t\t\tRam : 6 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 16MP\t\t\t\t\t\t\tFront Camera : 32MP\n\tBack Camera : 108MP + 8MP\t\t\t\t\tBack Camera : 48MP + 8MP + 2MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 4100mAh\n\tPrice : 19,999.00\t\t\t\t\t\t\tPrice : 19,990\n-------------------------------------------------------------------------------------")
        print(" 4 Xiaomi Mi 11X\t\t\t\t\t\t\t 19 Vivo Y33T\n\tDisplay : 6.67 inches\t\t\t\t\t\tDisplay : 6.58 inches\n\tProcessor : Qualcomm Snapdragon 870\t\t\tProcessor : Snapdragon 680 OC\n\tRam : 8 GB\t\t\t\t\t\t\t\t\tRam : 8 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 20MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 48MP + 8MP + 5MP\t\t\t\tBack Camera : 50MP + 2MP + 2MP\n\tBattery : 4520mAh\t\t\t\t\t\t\tBattery : 5000mAh\n\tPrice : 27,159.00\t\t\t\t\t\t\tPrice : 18,990.00\n\n-------------------------------------------------------------------------------------")
        print(" 5 Redmi Note 10T 5G\t\t\t\t\t\t 20 Vivo V23 5G\n\tDisplay : 6.5 inches\t\t\t\t\t\tDisplay : 6.56 inches\n\tProcessor : Mediatek Dimensity 700 OC\t\tProcessor : Mediatek Dimensity 1200\n\tRam : 4 GB\t\t\t\t\t\t\t\t\tRam : 8 GB\n\tStorage : 64 GB\t\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 8MP\t\t\t\t\t\t\tFront Camera : 50MP + 8MP\n\tBack Camera : 48MP + 2MP\t\t\t\t\tBack Camera : 108MP + 8MP + 2MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 4300mAh\n\tPrice : 14,999.00\t\t\t\t\t\t\tPrice : 21,999.00\t\t")
        print("\n Realme Mobile Info\t\t\t\t\t\t\t\t\t\tOppo Mobile Info")
        print("-------------------------------------\t\t----------------------------------------")
        print(" 6 Realme 8 5G\t\t\t\t\t\t\t\t 21 Oppo F19\n\tDisplay : 6.5 inches\t\t\t\t\t\tDisplay : 6.4 inches\n\tProcessor : Mediatek Dimensity 700\t\t\tProcessor : Mediatek Helio P95 OC\n\tRam : 4 GB\t\t\t\t\t\t\t\t\tRam : 8 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 16MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 48MP + 2MP + 2MP\t\t\t\tBack Camera : 48MP + 8MP + 2MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 4310mAh\n\tPrice : 16,499.00\t\t\t\t\t\t\tPrice : 18,990.00\n-------------------------------------------------------------------------------------")
        print(" 7 Realme X Series X7\t\t\t\t\t\t 22 Oppo Reno2 F\n\tDisplay : 6.43 inches\t\t\t\t\t\tDisplay : 6.4 inches\n\tProcessor : Mediatek Dimensity 800U\t\t\tProcessor : Qualcomm Snapdragon 710 OC\n\tRam : 6 GB\t\t\t\t\t\t\t\t\tRam : 6 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 16MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 64MP + 8MP + 2MP\t\t\t\tBack Camera : 48MP + 5MP\n\tBattery : 4310mAh\t\t\t\t\t\t\tBattery : 3765mAh\n\tPrice : 21,999.00\t\t\t\t\t\t\tPrice : 21,990\n-------------------------------------------------------------------------------------")
        print(" 8 Realme GT Master Edition\t\t\t\t\t\t 23 Oppo A74 5G\n\tDisplay : 6.43 inches\t\t\t\t\t\tDisplay : 6.49 inches\n\tProcessor : Qualcomm Snapdragon 778G\t\tProcessor : Qualcomm Snapdragon 480\n\tRam : 8 GB\t\t\t\t\t\t\t\t\tRam : 6 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 32MP\t\t\t\t\t\t\tFront Camera : 8MP\n\tBack Camera : 108MP + 8MP\t\t\t\t\tBack Camera : 48MP + 2MP + 2MP\n\tBattery : 4300mAh\t\t\t\t\t\t\tBattery : 5000mAh\n\tPrice : 26,999.00\t\t\t\t\t\t\tPrice : 16,990\n-------------------------------------------------------------------------------------")
        print(" 9 Realme 8s 5G\t\t\t\t\t\t\t\t 24 Oppo F19s\n\tDisplay : 6.5 inches\t\t\t\t\t\tDisplay : 6.43 inches\n\tProcessor : Mediatek Dimensity 700\t\t\tProcessor : Qualcomm Snapdragon 662\n\tRam : 4 GB\t\t\t\t\t\t\t\t\tRam : 6 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 16MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 48MP + 2MP + 2MP\t\t\t\tBack Camera : 48MP + 2MP + 2MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 5000mAh\n\tPrice : 17,999.00\t\t\t\t\t\t\tPrice : 19,990.00\n\n-------------------------------------------------------------------------------------")
        print(" 10 Realme 9i\t\t\t\t\t\t\t\t 25 Oppo F19 pro\n\tDisplay : 6.6 inches\t\t\t\t\t\tDisplay : 6.43 inches\n\tProcessor : Qualcomm Snapdragon 680\t\t\tProcessor : Mediatek Dimensity 800U\n\tRam : 4 GB\t\t\t\t\t\t\t\t\tRam : 8 GB\n\tStorage : 64 GB\t\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 16MP\t\t\t\t\t\t\tFront Camera : 50MP + 8MP\n\tBack Camera : 48MP + 8MP + 2MP\t\t\t\tBack Camera : 108MP + 8MP + 2MP\n\tBattery : 4310mAh\t\t\t\t\t\t\tBattery : 4300mAh\n\tPrice : 15,999.00\t\t\t\t\t\t\tPrice : 21,990.00\t\t")
        print("\n Samsung Mobile Info\t\t\t\t\t\t\t\t\t\tGaming Mobile Info")
        print("-------------------------------------\t\t----------------------------------------")
        print(" 11 Samsung Galaxy M32 5G\t\t\t\t\t 26 iQOO Z5 5G\n\tDisplay : 6.58 inches\t\t\t\t\t\tDisplay : 6.67 inches\n\tProcessor : Octa core Dimensity 700\t\t\tProcessor : Qualcomm Snapdragon 888\n\tRam : 8 GB\t\t\t\t\t\t\t\t\tRam : 8 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 20MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 50MP + 2MP + 2MP\t\t\t\tBack Camera : 108MP + 8MP + 5MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 5000mAh\n\tPrice : 20,999.00\t\t\t\t\t\t\tPrice : 26,990.00\n-------------------------------------------------------------------------------------")
        print(" 12 Samsung Galaxy F12\t\t\t\t\t\t 27 Samsung Galaxy\n\tDisplay : 6.67 inches\t\t\t\t\t\tDisplay : 6.58 inches\n\tProcessor : Qualcomm Snapdragon 865 OC\t\tProcessor : Mediatek MT6833 Dimensity 700\n\tRam : 6 GB\t\t\t\t\t\t\t\t\tRam : 6 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 20MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 64MP + 13MP + 5MP\t\t\t\tBack Camera : 64MP + 8MP + 2MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 5000mAh\n\tPrice : 10,499.00\t\t\t\t\t\t\tPrice : 93,300\n-------------------------------------------------------------------------------------")
        print(" 13 Samsung Galaxy F22\t\t\t\t\t\t 28 Oppo Reno7 Pro\n\tDisplay : 6.6 inches\t\t\t\t\t\tDisplay : 6.44 inches\n\tProcessor : Mediatek Dimensity 810 OC\t\tProcessor : Qualcomm Snapdragon 665\n\tRam : 8 GB\t\t\t\t\t\t\t\t\tRam : 6 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 16MP\t\t\t\t\t\t\tFront Camera : 32MP\n\tBack Camera : 108MP + 8MP\t\t\t\t\tBack Camera : 48MP + 8MP + 2MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 4100mAh\n\tPrice : 14,999.00\t\t\t\t\t\t\tPrice : 39,999\n-------------------------------------------------------------------------------------")
        print(" 14 Samsung Galaxt S20 FE 5G\t\t\t\t 29 Oneplus 9 RT\n\tDisplay : 6.67 inches\t\t\t\t\t\tDisplay : 6.58 inches\n\tProcessor : Qualcomm Snapdragon 870\t\t\tProcessor : Snapdragon 680 OC\n\tRam : 8 GB\t\t\t\t\t\t\t\t\tRam : 8 GB\n\tStorage : 128 GB\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 20MP\t\t\t\t\t\t\tFront Camera : 16MP\n\tBack Camera : 48MP + 8MP + 5MP\t\t\t\tBack Camera : 50MP + 2MP + 2MP\n\tBattery : 4520mAh\t\t\t\t\t\t\tBattery : 5000mAh\n\tPrice : 39,999.00\t\t\t\t\t\t\tPrice : 42,999.00\n\n-------------------------------------------------------------------------------------")
        print(" 15 Samsung Galaxy A03s\t\t\t\t\t\t 30 Realme 8 Pro\n\tDisplay : 6.5 inches\t\t\t\t\t\tDisplay : 6.56 inches\n\tProcessor : Mediatek Dimensity 700 OC\t\tProcessor : Mediatek Dimensity 1200\n\tRam : 4 GB\t\t\t\t\t\t\t\t\tRam : 8 GB\n\tStorage : 64 GB\t\t\t\t\t\t\t\tStorage : 128 GB\n\tFront Camera : 8MP\t\t\t\t\t\t\tFront Camera : 50MP + 8MP\n\tBack Camera : 48MP + 2MP\t\t\t\t\tBack Camera : 108MP + 8MP + 2MP\n\tBattery : 5000mAh\t\t\t\t\t\t\tBattery : 4300mAh\n\tPrice : 12,499.00\t\t\t\t\t\t\tPrice : 18,099.00\t\t")
        print("--------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\t  Television")
        print("--------------------------------------------------------------------------------------------")
        print(" 1.One plus Y Series\t\t\t\t\t\t\t6.Redmi\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice : 14,998\t\t\t\t\t\t\t\t\tPrice : 15,999\n----------------------------------------\t\t---------------------------------------------\n 2.Sony Bravia\t\t\t\t\t\t\t\t\t7.Toshiba\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice : 24,990\t\t\t\t\t\t\t\t\tPrice : 12,990\n-----------------------------------------\t\t---------------------------------------------\n 3.Samsung\t\t\t\t\t\t\t\t\t\t8.Xiaomi Mi 4K Horizon Edition\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice :16,499\t\t\t\t\t\t\t\t\tPrice : 16,290\n-----------------------------------------\t\t---------------------------------------------\n 4.Mi\t\t\t\t\t\t\t\t\t\t\t9.Beston\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice : 11,999\t\t\t\t\t\t\t\t\tPrice : 15,999\n-----------------------------------------\t\t---------------------------------------------\n 5.Sansui HD Ready Smart\t\t\t\t\t\t10.Realme NEO\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice : 13,990\t\t\t\t\t\t\t\t\tPrice : 9,800")
        print("--------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\t  Refrigirator")
        print("------------------------------------------------------------------------------------------------------")
        print(" 1. Godrej 185L Direct Cool\t\t\t\t\t\t\t\t5. LG 190L Direct Cool\n\t\tCapacity : 185L\t\t\t\t\t\t\t\t\t\tCapacity : 190L\n\t\tStar Rating : 4 Star\t\t\t\t\t\t\t\tStar Rating : 5 Star\n\t\tWeight : 35Kg\t\t\t\t\t\t\t\t\t\tWeight : 35.6Kg\n\t\tBuilt in Stabilizer : Yes\t\t\t\t\t\t\tBuilt in Stabilizer : Yes\n\t\tPrice : 14,390\t\t\t\t\t\t\t\t\t\tPrice : 17,990\n 2. Godrej 265L Frost Free DD\t\t\t\t\t\t\t6. LG 260L Frost DD\n\t\tCapacity : 265L\t\t\t\t\t\t\t\t\t\tCapacity : 260L\n\t\tStar Rating : 3 Star\t\t\t\t\t\t\t\tStar Rating : 3 Star\n\t\tWeight : 50.8Kg\t\t\t\t\t\t\t\t\t\tWeight : 50Kg\n\t\tBuilt in Stabilizer : Yes\t\t\t\t\t\t\tBuilt in Stabilizer : Yes\n\t\tPrice : 25,990\t\t\t\t\t\t\t\t\t\tPrice : 25,790\n 3. Whirlpool 190L Direct Cool\t\t\t\t\t\t\t7. Samsung 192L Direct Cool SD\n\t\tCapacity : 190L\t\t\t\t\t\t\t\t\t\tCapacity : 192L\n\t\tStar Rating : 2 Star\t\t\t\t\t\t\t\tStar Rating : 2 Star\n\t\tWieght : 32.4Kg\t\t\t\t\t\t\t\t\t\tWeight : 30Kg\n\t\tBuilt in Stabilizer : Yes\t\t\t\t\t\t\tBuilt in Stabilizer : Yes\n\t\tPrice : 12,990\t\t\t\t\t\t\t\t\t\tPrice : 12,790\n 4. Whirlpool 240L Frost TD\t\t\t\t\t\t\t\t8. Samsung 253L Frost Free DD\n\t\tCapacity : 240L\t\t\t\t\t\t\t\t\t\tCapacity : 253L\n\t\tStar Rating : 5 Star\t\t\t\t\t\t\t\tStar Rating : 3 Star\n\t\tWeight : 50Kg\t\t\t\t\t\t\t\t\t\tWeight : 46Kg\n\t\tBuilt in stabilizer : Yes\t\t\t\t\t\t\tBuilt in stabilizer : Yes\n\t\tPrice : 25,490\t\t\t\t\t\t\t\t\t\tPrice : 24,490\n")

        n = int(input("0-BACK\n ->"))
        if n == 0:
            home()
        else:
            pass

    elif choose == 1:
        Mobile_Phones()
    elif choose==2:
        Television()
    elif choose==3:
        Refrigirator()
    else:
        pass

    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()

def Mobile_Phones():
    ch=int(input("Id : "))
    global i
    f=0
    r=0
    for n in range (0,i):
        if Id[n]==ch:
            f=1
            print("--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t\t\tRaj Electronics")
            print("--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t\t\t\tCompany")
            print("--------------------------------------------------------------------------------------------")
            print("\n MI\t\t\t\t\t\t\t\t\t\t\tVivo")
            print("-------------------------------------\t\t----------------------------------------")
            print(" 1 Xiaomi 11T pro 5G.........43,999.00\t\t 16 Vivo Y75 5G..............21,990.00")
            print(" 2 Xiaomi Redmi Mi 10T.......21,694.00\t\t 17 Vivo Y72 5G..............19,999.00")
            print(" 3 Redmi Note 11t 5G.........16,999.00\t\t 18 vivo V20 SE..............19,990.00")
            print(" 4 Xiaomi Mi 11X.............27,159.00\t\t 19 Vivo Y33T................18,990.00")
            print(" 5 Redmi Note 10T 5G.........14,999.00\t\t 20 Vivo V23 5G..............21,999.00")

            print("\n Realme\t\t\t\t\t\t\t\t\t\tOPPO")
            print("-------------------------------------\t\t----------------------------------------")
            print(" 6 Realme 8 5G...............16,499.00\t\t 21 Oppo F19..................18,990.00")
            print(" 7 Realme X Series X7........21,999.00\t\t 22 Oppo Reno2 F..............21,990.00")
            print(" 8 Realme GT Master Edition..26,999.00\t\t 23 Oppo A74 5G...............16,990.00")
            print(" 9 Realme 8s 5G..............17,999.00\t\t 24 Oppo F19s.................19,990.00")
            print(" 10 Realme 9i................15,999.00\t\t 25 Oppo F19 Pro..............21,990.00")

            print("\n Samsung\t\t\t\t\t\t\t\t\tGaming Phone")
            print("-------------------------------------\t\t----------------------------------------")
            print(" 11 Samsung Galaxy M32 5G.....20,999.00\t\t 26 iQOO Z5 5G...............26,990.00")
            print(" 12 Samsung Galaxy F12........10,499.00\t\t 27 Samsung Galaxy...........93,300.00")
            print(" 13 Samsung Galaxy F22........14,999.00\t\t 28 Oppo Reno7 Pro...........39,999.00")
            print(" 14 Samsung Galaxy S20 FE 5G..39,999.00\t\t 29 OnePlus 9 RT.............42,999.00")
            print(" 15 Samsung Galaxy A03s.......12,499.00\t\t 30 Realme 8 Pro.............18,099.00")
            print("Press 0 to end")
            ch=1
            while(ch!=0):
                ch = int(input(" ->"))
                if ch == 1:
                    rs = 49999
                    r=r+rs
                elif ch == 2:
                    rs = 21694
                    r=r+rs
                elif ch == 3:
                    rs=16999
                    r=r+rs
                elif ch == 4:
                    rs = 27159
                    r=r+rs
                elif ch == 5:
                    rs = 14999
                    r=r+rs
                elif ch == 6:
                    rs = 16499
                    r=r+rs
                elif ch == 7:
                    rs = 21999
                    r=r+rs
                elif ch == 8:
                    rs = 26999
                    r=r+rs
                elif ch == 9:
                    rs = 17999
                    r=r+rs
                elif ch == 10:
                    rs = 15999
                    r=r+rs
                elif ch == 11:
                    rs = 20999
                    r=r+rs
                elif ch == 12:
                    rs = 10499
                    r=r+rs
                elif ch == 13:
                    rs = 14399
                    r=r+rs
                elif ch == 14:
                    rs = 39999
                    r=r+rs
                elif ch == 15:
                    rs = 12499
                    r=r+rs
                elif ch == 16:
                    rs = 21990
                    r=r+rs
                elif ch == 17:
                    rs = 19999
                    r=r+rs
                elif ch == 18 or ch == 24:
                    rs = 19990
                    r=r+rs
                elif ch == 19 or ch == 21:
                    rs = 18990
                    r=r+rs
                elif ch == 20:
                    rs = 21999
                    r=r+rs
                elif ch == 22 or ch == 25:
                    rs = 21990
                    r=r+rs
                elif ch == 23:
                    rs = 19990
                    r=r+rs
                elif ch == 26:
                    rs = 26990
                    r=r+rs
                elif ch == 27:
                    rs = 93300
                    r=r+rs
                elif ch == 28:
                    rs = 39999
                    r = r + rs
                elif ch == 29:
                    rs = 42999
                    r = r + rs
                elif ch == 30:
                    rs = 18099
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice.....!!!!!")
            print("Total Bill: ",r)
            print("Item is added in Cart Successfully")
            r = r + rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Id")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()

def Television():
    ch=int(input("Id : "))
    global i
    f=0
    r=0
    for n in range (0,i):
        if Id[n]==ch:
            f=1
            print("--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t\t\tRaj Electronics")
            print("--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t\t\t  Television")
            print("--------------------------------------------------------------------------------------------")
            print(" 1.One plus Y Series\t\t\t\t\t\t\t6.Redmi\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice : 14,998\t\t\t\t\t\t\t\t\tPrice : 15,999\n----------------------------------------\t\t---------------------------------------------\n 2.Sony Bravia\t\t\t\t\t\t\t\t\t7.Toshiba\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice : 24,990\t\t\t\t\t\t\t\t\tPrice : 12,990\n-----------------------------------------\t\t---------------------------------------------\n 3.Samsung\t\t\t\t\t\t\t\t\t\t8.Xiaomi Mi 4K Horizon Edition\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice :16,499\t\t\t\t\t\t\t\t\tPrice : 16,290\n-----------------------------------------\t\t---------------------------------------------\n 4.Mi\t\t\t\t\t\t\t\t\t\t\t9.Beston\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice : 11,999\t\t\t\t\t\t\t\t\tPrice : 15,999\n-----------------------------------------\t\t---------------------------------------------\n 5.Sansui HD Ready Smart\t\t\t\t\t\t10.Realme NEO\n\tDisplay : 32 inch\t\t\t\t\t\t\t\tDisplay : 32 inch\n\tOS : Android\t\t\t\t\t\t\t\t\tOS : Android\n\tPrice : 13,990\t\t\t\t\t\t\t\t\tPrice : 9,800")
            print("Press 0 to end")
            ch=1
            while (ch!=0):
                ch = int(input(" ->"))
                if ch==1:
                    rs = 15999
                    r=r+rs
                elif ch==2:
                    rs = 24990
                    r=r=rs
                elif ch==3:
                    rs = 16290
                    r=r+rs
                elif ch==4:
                    rs = 15999
                    r=r+rs
                elif ch==5:
                    rs = 13990
                    r=r+rs
                elif ch==6:
                    rs = 14998
                    r=r+rs
                elif ch==7:
                    rs = 12990
                    r=r+rs
                elif ch==8:
                    rs = 16499
                    r=r+rs
                elif ch==9:
                    rs = 15999
                    r=r+rs
                elif ch==10:
                    rs = 9800
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("WRONG CHOICE.....!!!!!")
            print("Total Bill: ",r)
            print("Item is added in Cart Successfully")
            r = r + rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Id")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()

def Refrigirator():
    ch=int(input("Id : "))
    global i
    f=0
    r=0
    for n in range (0,i):
        if Id[n]==ch:
            f=1
            print("--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t\t\tRaj Electronics")
            print("--------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t\t\t\t\t  Refrigirator")
            print("------------------------------------------------------------------------------------------------------")
            print(" 1. Godrej 185L Direct Cool\t\t\t\t\t\t\t\t5. LG 190L Direct Cool\n\t\tCapacity : 185L\t\t\t\t\t\t\t\t\t\tCapacity : 190L\n\t\tStar Rating : 4 Star\t\t\t\t\t\t\t\tStar Rating : 5 Star\n\t\tWeight : 35Kg\t\t\t\t\t\t\t\t\t\tWeight : 35.6Kg\n\t\tBuilt in Stabilizer : Yes\t\t\t\t\t\t\tBuilt in Stabilizer : Yes\n\t\tPrice : 14,390\t\t\t\t\t\t\t\t\t\tPrice : 17,990\n 2. Godrej 265L Frost Free DD\t\t\t\t\t\t\t6. LG 260L Frost DD\n\t\tCapacity : 265L\t\t\t\t\t\t\t\t\t\tCapacity : 260L\n\t\tStar Rating : 3 Star\t\t\t\t\t\t\t\tStar Rating : 3 Star\n\t\tWeight : 50.8Kg\t\t\t\t\t\t\t\t\t\tWeight : 50Kg\n\t\tBuilt in Stabilizer : Yes\t\t\t\t\t\t\tBuilt in Stabilizer : Yes\n\t\tPrice : 25,990\t\t\t\t\t\t\t\t\t\tPrice : 25,790\n 3. Whirlpool 190L Direct Cool\t\t\t\t\t\t\t7. Samsung 192L Direct Cool SD\n\t\tCapacity : 190L\t\t\t\t\t\t\t\t\t\tCapacity : 192L\n\t\tStar Rating : 2 Star\t\t\t\t\t\t\t\tStar Rating : 2 Star\n\t\tWieght : 32.4Kg\t\t\t\t\t\t\t\t\t\tWeight : 30Kg\n\t\tBuilt in Stabilizer : Yes\t\t\t\t\t\t\tBuilt in Stabilizer : Yes\n\t\tPrice : 12,990\t\t\t\t\t\t\t\t\t\tPrice : 12,790\n 4. Whirlpool 240L Frost TD\t\t\t\t\t\t\t\t8. Samsung 253L Frost Free DD\n\t\tCapacity : 240L\t\t\t\t\t\t\t\t\t\tCapacity : 253L\n\t\tStar Rating : 5 Star\t\t\t\t\t\t\t\tStar Rating : 3 Star\n\t\tWeight : 50Kg\t\t\t\t\t\t\t\t\t\tWeight : 46Kg\n\t\tBuilt in stabilizer : Yes\t\t\t\t\t\t\tBuilt in stabilizer : Yes\n\t\tPrice : 25,490\t\t\t\t\t\t\t\t\t\tPrice : 24,490\n")
            print("Press 0 to end")
            ch=1
            while(ch!=0):
                ch = int(input(" ->"))
                if ch == 1:
                    rs = 14390
                    r=r+rs
                elif ch == 2:
                    rs = 25990
                    r=r+rs
                elif ch == 3:
                    rs = 12990
                    r=r+rs
                elif ch == 4:
                    rs = 25490
                    r=r+rs
                elif ch == 5:
                    rs = 17990
                    r=r+rs
                elif ch == 6:
                    rs = 25790
                    r=r+rs
                elif ch == 7:
                    rs = 12790
                    r=r+rs
                elif ch == 8:
                    rs = 24490
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("WRONG CHOICE")
            print("Total Bill :",r)
            print("Item is added in Cart Successfully")
            r = r + rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Id")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()

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

# PAYMENT FUNCTION
def Payment():
    ph = int(input("Id.: "))
    global i
    f = 0
    for n in range(0, i):
        if ph == Id[n]:

            # checks if payment is
            # not already done
            if p[n] == 0:
                f = 1
                print("\n\n --------------------------------")
                print("		 Raj Electronics")
                print(" --------------------------------")
                print("			 Bill")
                print(" --------------------------------")
                print(" MODE OF PAYMENT")
                print(" 1- Credit/Debit Card")
                print(" 2- Paytm/PhonePe")
                print(" 3- Using UPI")
                print(" 4- Cash")
                print(" ")
                print("Amount : ", rc[n])
                print(" ")
                am = rc[n]
                if am > 50000:
                    print("You Are Eligible for 10% Discount\nAfter Discount Amount will be")
                    a = (am * 10) / 100
                    print("\n Total Amount : Rs", am - a)
                elif am < 50000:
                    print("You Are Eligible for 5% Discount\nAfter Discount Amount will be")
                    a = (am * 5) / 100
                    print("\n Total Amount: Rs", am - a)
                else:
                    print("Not Eligible For Any Discount")
                print(" ")
                x = int(input("Select Mode Of Payment -> "))
                if x == 1:
                    print("Enter your Card details")

                    def validate(cardNumber):
                        validCardNumber = ""
                        for number in cardNumber:
                            if (ord(number) >= 48 and ord(number) <= 57): validCardNumber += str(number)
                        if not cardNumber or not validCardNumber: validCardNumber = "00"
                        return validCardNumber

                    # Calculate sum of digits for validation
                    def calculateSum(cardNumber):
                        sum=0
                        for each in ((cardNumber)): sum += int(each)
                        return sum

                    # Check the Card Numbers Length and Composition
                    def checkFormat(cardNumber):
                        if (calculateSum(cardNumber) == 0 or len(cardNumber) < 4 or not cardNumber):
                            return False
                        else:
                            return True

                    # Check the Card Numbers Check Sum and Calculate Check Bit
                    def checkNumber(cardNumber):
                        def calculateSum(cardNumber):
                            sum1 = sum3 = 0
                            sum2 = ""
                            for each in ((cardNumber[-1::-2])): sum1 += int(each)
                            for each in ((cardNumber[-2::-2])): sum2 += str((int(each) * 2))
                            for each in (sum2): sum3 += int(each)
                            return str(sum1 + sum3)

                        cd = int(calculateSum(str(int(str(cardNumber)[:-1]) * 10))) % 10
                        global checkDigit
                        checkDigit = cd if cd == 0 else 10 - cd
                        return True if checkFormat(cardNumber) == True and calculateSum(cardNumber)[
                            -1] == '0' else False

                    # Determine why the card number is not correct
                    def getReason(cardNumber):
                        reason = ""
                        if (calculateSum(cardNumber) == 0 or not cardNumber):
                            reason = "a blank Card Number %s was Inputed" % cardNumber
                        elif (len(cardNumber) < 4):
                            reason = "the card number is too short (%s digits)" % len(cardNumber)
                        elif (cardNumber[-1] != checkDigit):
                            reason = "The last digit, or check digit should have been %s" % checkDigit
                        return reason

                    # Declare Variables
                    cardNumber = validate(input("Enter a Card Number\t"))
                    valid = False
                    reason = ""

                    # Determine Whether Number is Correct and get a Reason
                    valid = checkNumber(cardNumber)
                    if valid == False: reason = getReason(cardNumber)

                    # Output Result to User
                    outputStatement = "The card number %s is %s"
                    outputStatement += "%s" if reason == "" else " because %s"
                    print(outputStatement % (cardNumber, "Valid" if valid == True else "Invalid", reason))

                    e = input("Expiry date : ")
                    z = int(input("CVV : "))
                    c = input("Name On Card : ")
                    o = int(input("OTP : "))
                    time.sleep(5)
                    print("Payment Done Successfully!!!!!!\nThanks for Shopping!!!")
                elif x == 2:
                    img = qrcode.make("Paytm/PhonePe 9717569027")
                    img.show("payment.jpg")
                    time.sleep(5)
                    print("Payment Done Successfully!!!!!!\nThanks for Shopping!!!")
                elif x == 3:
                    print("UPI ID : kavirajkishore984@hdfcbank")
                    time.sleep(5)
                    print("Payment Done Successfully!!!!!!\nThanks for Shopping!!!")
                elif x == 4:
                    time.sleep(5)
                    print("Payment Done Successfully!!!!!!\nThanks for Shopping!!!")
                else:
                    print("invalid input")
                print("Print Bill (Y/N)")
                ch = str(input("->"))

                if ch == 'y' or ch == 'Y':
                    print("\n\n -----------------------------------------")
                    print("		 Raj Electronics India Pvt. Ltd.")
                    print(" -----------------------------------------")
                    print("\tADD - Raj electronics, GF,Road no. 4,\n\t\tGreenfield,Faridabad,Haryana,121009")
                    print(" -----------------------------------------")
                    print("			 Retail Invoice")
                    print(" -----------------------------------------")
                    iv = random.randrange(5000)
                    print("Invoice No. :", iv)
                    e = datetime.datetime.now()
                    print("\t\t\t\t\tBilling Date: %s/%s/%s" % (e.day, e.month, e.year))
                    print("\t\t\t\t\tBilling Time: = %s:%s:%s" % (e.hour, e.minute, e.second))
                    print(" Name: ", name[n], "\t\n Phone No.: ", phno[n], "\t")
                    print(" -----------------------------------------")
                    print("\n Total Amount: ", (am-a), "\t")
                    print(" -----------------------------------------")
                    print("		 \tThank You")
                    print("		 \tVisit Again :)")
                    print(" -----------------------------------------\n")
                    p.pop(n)
                    p.insert(n, 1)

                    # pops room no. and customer id from list and
                    # later assigns zero at same position
                    Id.pop(n)
                    Id.insert(n, 0)

            else:

                for j in range(n + 1, i):
                    if ph == Id[j]:
                        if p[j] == 0:
                            pass

                        else:
                            f = 1
                            print("\n\tPayment has been Made :)\n\n")
    if f == 0:
        print("Invalid  Id")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()


# RECORD FUNCTION
def Record():
    # checks if any record exists or not
    if phno != []:
        print("	 *** HOTEL RECORD ***\n")
        print("| Name	 | Phone No. | Price	 |")
        print(
            "----------------------------------------------------------------------------------------------------------------------")

        for n in range(0, i):
            print("|", name[n], "\t |", phno[n], "\t",
                  "\t|", rc[n])

        print(
            "----------------------------------------------------------------------------------------------------------------------")

    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()

#Driver Code
home()
