#Program For Variable Length Keyword Arguments
try:
    def display(sname,*details,crs="Python"):
        print("="*50)
        sno = int(input("Enter Student Number :"))
        print("\t{}".format(sno))
        print("\t{}".format(sname))
        print("\t{}".format(crs))
        print("=" * 50)
        print("Student Details :")
        for val in details:
            print("\t{}".format(val))
        print("="*50)
    #Main Program
    display("Karan",10,20,30,40,50,60,crs="Java")
    display("Scott","Python","Java","Django","Android")
except ValueError:
    print("Dont Enter str For sno")

def num(*obj):
    print("="*50)
    for val in obj:
        print("\t{}".format(val))

#Main Program
num(10,20,30,40,50,60,70)