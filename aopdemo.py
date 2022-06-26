#aopdemo.py ---> File Name Acts As Module Name
import sys

from aopmenu import aopmenu
from aopoperation import addition,subtraction,multiplication,Division,Modulodiv,exponational,remainder
try:
    while(True):
        aopmenu()
        ch=int(input("Enter Your Choice Option :"))
        match(ch):
            case 1:
                addition()
            case 2:
                subtraction()
            case 3:
                multiplication()
            case 4:
                Division()
            case 5:
                Modulodiv()
            case 6:
                remainder()
            case 7:
                exponational()

            case 8:
                sys.exit()

            case _:
                print("Your Choice Option Is Invalid/Wrong Plz Try-Again !")
except ValueError:
    print("Don't Enter strs,Special Symbols And Alpha-Numerics")
except :
    print("OOP's SomeThing Went Wrong !")
