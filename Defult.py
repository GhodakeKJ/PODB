#Program For Default Arguments
def show(sno,sname,marks,crs="Python"):
    print("\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs))

#Main Program
print("="*50)
print("\tSt No\tSt Name  \tSt Marks\tCourse")
print("=" * 50)
show(100,"Rossum",78.80)
show(200,"Karan",33.33)
show(300,"Scott",22.22)
print("=" * 50)