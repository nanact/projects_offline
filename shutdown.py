import os

shutdown = input("do you want you shutdown")

if shutdown == "no":
    print("Okay")
    
else:
    os.system("shutdown -s")