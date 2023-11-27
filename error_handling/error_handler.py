#global errorhandling program
def errorHandling(param1, param2):
    while True:
        try:
            valid_inp = int(input("\nOut of this which option would you like to choose ? : "))
            if valid_inp >= param1 and valid_inp <= param2:
                return valid_inp
        except ValueError:
            print("Error! Enter an integer value!! ")
        except KeyboardInterrupt:
            print("OOPs feelin' like very strong keyboard stroke ")
            raise Exception("Thanks for coming!! ")

def errorHandling2(param1, range1, range2):
    while True:
        try:
            if range1 <= param1 <= range2:
                return True
            else:
                print("Error: Enter values in the range of {} to {}".format(range1, range2))
                param1 = int(input('Try again: '))
        except ValueError:
            print("Error! Enter an integer value!! ")
        except KeyboardInterrupt:
            print("OOPs feelin' like very strong keyboard stroke ")
            raise Exception("Thanks for coming!! ")