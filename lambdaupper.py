#Program For Demonstrating Given List Names Are Finding Upper,Lower Or Mixed
uppercase=lambda n:n.isupper()
lowercase=lambda n:n.islower()
mixedcase=lambda n:not(n.isupper() or n.islower())

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