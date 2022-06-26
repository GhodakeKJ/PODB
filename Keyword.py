#Program For KeyWord  Arguments
def show(sno,sname,marks,crs="Python"):
    print("\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs))

#Main Program
print("="*50)
print("\tSt No\tSt Name  \tSt Marks\tCourse")
print("=" * 50)
show(sno=100,sname="Rossum",marks=78.80)
show(200,"Karan",33.33)
show(300,"Scott",22.22)
show(marks=56.44,sname="Sanjay",crs="Java",sno=400)
show(500,"Gosling",33.22)
print("=" * 50)