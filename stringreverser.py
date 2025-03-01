class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string

input_string = "Hello world this is a test"
reverser = StringReverser(input_string)
reversed_string = reverser.reverse_words()
print("Original String:", input_string)
print("Reversed String:", reversed_string)
