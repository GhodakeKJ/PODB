#Program For Importing Shares Module And Displaying Values Of Shares
import importlib
import time
import shares
def dispshares(d):
    print("="*50)
    print("\tShare Name \tShare Value")
    print("=" * 50)
    for k,v in d.items():
        print("\t{}\t{}".format(k,v))

#Main Program
d=shares.sharesinfo()
dispshares(d)
print("I Am Going For Sleep 15 Sec")
time.sleep(15)
print("I Am Coming From Sleep")
importlib.reload(shares)
d=shares.sharesinfo()
dispshares(d)
print("I Am Going For Sleep 15 Sec")
time.sleep(15)
print("I Am Coming From Sleep")
importlib.reload(shares)

