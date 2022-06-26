#atmoperation.py ------>File Name Acts As Module Name
from atmexception import WithDrawError,DipositError,InsuffiFoundError
bal=500
def deposit():
    damt=float(input("Enter Amount How Want To Deposit :"))
    if(damt<=0):
        raise DipositError
    else:
        global bal
        bal=bal+damt
        print("Your Ac xxxxxxx123 Balanace INR={}".format(damt))
        print("Your Current Balance :{}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enter Amount How Much You Want WithDraw :"))
    if(wamt<=0):
        raise WithDrawError
    elif(wamt + 500)>bal:
        raise InsuffiFoundError
    else:
        bal=bal-wamt
        print("Your Ac xxxxxxxx123 Debited With INR:{}".format(wamt))
        print("Your Current Ac Balance :{}".format(bal))

def balance():
    print("Your Ac xxxxxxxxxxx123 Current Balance INR:{}".format(bal))