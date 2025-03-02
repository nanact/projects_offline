def check_age():
    try:
        age = int(input("Please enter your age: "))
        
        if age < 0 or age > 120:  
            print("Error: The age entered is not valid. Please enter an age between 0 and 120.")
        else:
            if age % 2 == 0:
                print("The age entered is even.")
            else:
                print("The age entered is odd.")
    
    except ValueError:
        print("Error: The value entered is not a valid integer. Please enter a numerical value.")

check_age()
