#atmdemo.py ----->file Name Acts module Name
import sys

from atmmenu import atmmenu
from atmexception import WithDrawError,DipositError,InsuffiFoundError
from atmoperation import deposit,withdraw,balance
while(True):

    try:
        atmmenu()
        ch=int(input("Enter Your Choice :"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("Dont try To Deposite strs,special and alpha-nums")
                except DipositError:
                    print("Don't Try To Deposit Zero And -Ve Amount")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("Don't Try WithDraw strs,aplha-Numerics And Special Symbols")
                except WithDrawError:
                    print("Dont Try To Withdraw Zero And -Ve Amount")
                except InsuffiFoundError:
                    print("In Your AC Does Not Sufficiant Found")

            case 3:
                balance()
            case 4:
                print("Thank You For Visiting Our ATM")
                sys.exit()

            case _:
                print("Your Choice Is Invalid Try-Again")

    except:
        print("OOPs Some Thing Went Wrong")
