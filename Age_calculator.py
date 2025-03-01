import tkinter as t



def submit_():
    Month_of_DOB = month_of_DOB.get()
    Month_of_DOB=int(Month_of_DOB)
    Year_of_DOB= year_of_DOB.get()
    Year_of_DOB = int(Year_of_DOB)
    Month_of_date = month_of_date.get()
    Month_of_date = int(Month_of_date)
    Year_of_date = year_of_date.get()
    Year_of_date = int(Year_of_date)
    
    age = 0
    if Month_of_date < 13:
        if Month_of_DOB < 13:
          if Month_of_DOB > Month_of_date:
            age = Year_of_date - Year_of_DOB - 1
          else:
              age = Year_of_date - Year_of_DOB
    
    answer.config(text = age)

room=t.Tk()

room.geometry("500x300")

room.title("Age")

label18 = t.Label(text = "birth")
label18.grid(row = 0,column = 0)

label = t.Label(text="month of birth(number format)")
label.grid(row = 1, column = 0)

month_of_DOB = t.Entry()
month_of_DOB.grid(row = 2, column=0)

label1 = t.Label(text = "year of birth")
label1.grid(row = 3, column=0)

year_of_DOB = t.Entry()
year_of_DOB.grid(row = 4, column = 0)

label2 = t.Label(text = "date entered")
label2.grid(row = 0, column=2)

label3 = t.Label(text = "month of date(number format)")
label3.grid(row = 1, column=2)

month_of_date = t.Entry()
month_of_date.grid(row = 2, column = 2)

label4 = t.Label(text = "year of birth")
label4.grid(row = 3, column=2)

year_of_date = t.Entry()
year_of_date.grid(row = 4, column = 2)

submit = t.Button(text = "submit", command = submit_)
submit.grid(row = 5, column=1)

answer = t.Label(text = "no input reviced")
answer.grid(row=6, column = 1)

room.mainloop()