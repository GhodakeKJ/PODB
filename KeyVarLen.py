#Program For Keyword Variable Length Arguments
try:
    def display(sname,*details,crs="Python",**kvr):
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
        for k,v in kvr.items():
            print("\t{}\t{}".format(k,v))
    #Main Program
    display("Karan",10,20,30,40,50,60,crs="Java",hobby1="Cricket",hobby2="Kho-Kho",hobby3="Reading")
    display("Scott","Python","Java","Django","Android",marathi=56,hindi=99,eng=87)
except :
    print("OOP's Something Went Wrong")