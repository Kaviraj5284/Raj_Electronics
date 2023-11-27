import pyfiglet
from error_handling import error_handler
from modules import Booking,Payment,Record,Accessories

def main():
    print(pyfiglet.figlet_format("           Raj  Electronics"))
    print("\t\t\t1 Booking\n\t\t\t2 Accessories\n\t\t\t3 Payment\n\t\t\t4 Record\n\t\t\t0 Exit\n")
    choose = int(input("Press value b/w (0 to 4)\n-> "))
    response = error_handler.errorHandling2(choose,0,4)
    if response == True:
        try:
            match choose:
                case 0:
                    print("Exiting the program ...\n")
                    exit()
                case 1:
                    # Booking()
                    print("Booking...")
                case 2:
                    # Accessories()
                    print("Accessory")
                case 3:
                    # Payment()
                    print("Payment")
                case 4:
                    # Record()
                    print("Record")
        except Exception as e:
            print("Exception: {}".format(e))


if __name__ == "__main__":
    main()