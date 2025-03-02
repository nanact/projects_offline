def is_odd(number):
    return number % 2 != 0

def is_even(number):
    return number % 2 == 0

def main():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if start > end:
            raise ValueError("Start of the range should be less than or equal to the end of the range.")

        squares = [x**2 for x in range(start, end + 1)]
        odd_squares = [x for x in squares if is_odd(x)]
        even_squares = [x for x in squares if is_even(x)]

        print(f"Square values: {squares}")
        print(f"Odd square values: {odd_squares}")
        print(f"Even square values: {even_squares}")

    except ValueError as e:
        print(f"Error: {e}")

main()
