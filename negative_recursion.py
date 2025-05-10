def get_input():
    number = int(input("Enter a number: "))
    if number < 0:  
        print("Negative number entered")
        return
    else:
        get_input()  

get_input()