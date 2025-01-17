import roman as r

class int_to_roman():
  def __init__(self):
      self.number = int(input("Enter your number"))
      self.roman = r.toRoman(self.number)
      print(self.roman)
      
int_to_roman()
      
