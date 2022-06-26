#Program For Storing Our Source File Data Copied In Destinatrion File
try:

    sfile=input("Enter Your Source File Name  :")
    with open(sfile,"r") as fp1:
        dfile=input("Enter Location/Destination Of File :")
        with open(dfile,"a") as fp2:
            filedata=fp1.read()
            print(filedata)
            fp2.write(filedata)
except FileNotFoundError:
    print("File Does Not Exists")