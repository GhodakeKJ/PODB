#Import Out aop Module
#aopoperation.py
from aopmenu import aopmenu
def aopoperations(kvr):
    a=float(input("Enter Your First Value :"))
    b=float(input("Enter Your Second Value :"))
    return a,b
def addition():
    a,b=aopoperations("Addition")
    print("Addition Of ({} and {}) = {}".format(a,b,a+b))

def subtraction():
    a,b=aopoperations("Subtraction")
    print("Subtraction Of ({} and {}) = {}".format(a,b,a-b))

def multiplication():
    a,b=aopoperations("Multiplication")
    print("Multiplication Of ({} and {}) = {}".format(a,b,a*b))
def Division():
    a,b=aopoperations("Division")
    print("Division Of ({} and {}) = {}".format(a,b,a/b))

def Modulodiv():
    a,b=aopoperations("Modulo Division")
    print(" Modulo Division Of ({} and {}) = {}".format(a,b,a//b))

def remainder():
    a,b=aopoperations("Remainder")
    print(" Remainder Of ({} and {}) = {}".format(a,b,a%b))

def exponational():
    a=float(input("Enter Base :"))
    b=float(input("Enter Power :"))
    print(" Remainder Of ({} and {}) = {}".format(a,b,a**b))





