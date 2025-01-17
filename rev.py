s = input("Your string")

stack = list(s)

rev = ""

while stack:
  
    rev += stack.pop()

print(rev)