def uppercase(n):
    if n.isupper():
        return True
    else:
        return False
def lowercase(n):
    if n.islower():
        return True
    else:
        return False
def mixedcase(n):
    if not (n.isupper() or n.islower()):
        return True
    else:
        return False

#Main Program
print("Enter List Of Elements Seperated By Space :")
lst=[str(val) for val in input().split()]
upper=list(filter(uppercase,lst))
lower=list(filter(lowercase,lst))
mixed=list(filter(mixedcase,lst))
print("="*50)
print("Given List Names :",lst)
print("Upper Case Names :",upper)
print("Lower Case Name  :",lower)
print("Mixed Case Names :",mixed)
print("="*50)