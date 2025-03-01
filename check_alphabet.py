def is_alphabet(char):
    if char.isalpha():
        return f"'{char}' is an alphabet."
    else:
        return f"'{char}' is not an alphabet."

char = input("Enter a character: ")

if len(char) == 1:
    result = is_alphabet(char)
    print(result)
else:
    print("Please enter a single character.")
