#divisiondemo.py
from userdefineexc import KaranDivisionError
from  karanex import division
try:
    a=float(input("Enter First Value For Division  :"))
    b=float(input("Enter Second Value For Division :"))
    result=division(a,b)

except KaranDivisionError:
    print("Don't Enter Zero For Denominator !")
except ValueError:
    print("Don't Enter strs,Special Symbols And Alpha-Numerics")
except:
    print("OOP's SomeThing Went Wrong")
else:
    print("Result :",result)
finally:
    print("I AM From Finally Block")