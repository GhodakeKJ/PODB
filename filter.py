#Main Program
print("Enter List Of Values Seperated By Space :")
lst=[int (val) for val in input().split()]
positive=list(filter(lambda n:n>0,lst))
negative=list(filter(lambda n:n<0,lst))
zeros=list(filter(lambda n:n==0,lst))
print("="*50)
print("Given List Of Elements :",lst)
print("Positive Elements In List :",positive)
print("Negative Elements In List :",negative)
print("Zeros Elements In List :",zeros)
print("="*50)
