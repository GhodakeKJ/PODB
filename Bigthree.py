#Program For Big Number In Three Numbers
threevalue=lambda a,b,c:"All Values Are Same" if a==b==c else a if(b<=a>c) else b if(a<=b>c) else c


#Main Program
a=int(input("Enter First Value :"))
b=int(input("Enter Second Value :"))
c=int(input("Enter Third Value  :"))
allvalue=list(filter(threevalue))
print("")