import random
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
import pygame

pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load("midnight-quirk-255361.mp3")
    pygame.mixer.music.play(loops=-1)


AIpoints = 0

player = 0
choos = ["rock","paper","scissor"]

def start(choose):
    global player
    global AIpoints
    command = ""
    computer = random.choice(choos)
    
    if computer == choose:
        command = "it is a tie"
    elif choose == "paper" and computer == "rock"or choose == "rock" and computer == "scissor" or choose == "scissor" and computer == "paper":
        command = "you win"
        player = player + 1
        
    else:
        command = "you lose"
        AIpoints = AIpoints + 1
        
    if computer == "paper":
        computery.config(text = "Computer:",image= paper_,compound='top', font=("Arial", 14))
        
        
    elif computer == "rock":
        computery.config(text = "Computer:",image= rock_,compound='top', font=("Arial", 14))
    
    elif computer == "scissor":
        computery.config(text = "Computer:",image= scissor_,compound='top', font=("Arial", 14))
        
    else:
        pass
    
    if choose == "rock":
        your.config(text = "My: ",image = rock_ ,compound='top', font=("Arial", 14))
        
    elif choose == "paper":
        your.config(text = "My: ",image = paper_,compound='top', font=("Arial", 14))
    
    elif choose == "scissor":
        your.config(text = "My: ",image = scissor_ ,compound='top', font=("Arial", 14))
    
    else:
        pass
         
        
    to.config(text=f"{command} You pick {choose} the computer pick {computer}")
    
    answer.config(text = "PLAYER: " + str(player) + " COMPUTER: "+str(AIpoints))


ro = tk.Tk()

ro.geometry("700x500")

ro.title("GAME")

ro.configure(bg="lightblue")

ro.update_idletasks()

scissor_ = PhotoImage(file = "Untitled design (1).png").subsample(3, 3)

paper_= PhotoImage(file = "Untitled design (3).png").subsample(3, 3)

rock_ = PhotoImage( file = "Untitled design (2).png").subsample(3, 3)

ro.iconphoto(False, PhotoImage(file = "rock.png"))

style = ttk.Style() 
style.configure("TLabel", background="lightblue")
style.configure("TButton", font=("Arial", 14), padding=10)

top_frame = tk.Frame(ro, bg="lightblue")
top_frame.pack(pady = 10, fill = tk.X,expand=True)
middle_frame = tk.Frame(ro, bg="lightblue")
middle_frame.pack(pady = 10, fill = tk.X,expand=True)
bottom_frame = tk.Frame(ro, bg="lightblue")
bottom_frame.pack(pady = 10, fill = tk.X,expand=True)
dow = tk.Frame(ro, bg="lightblue")
dow.pack(pady = 10, fill = tk.X,expand=True)

rock = ttk.Button(bottom_frame,text = "rock",command = lambda: start("rock"))
rock.pack()

paper = ttk.Button(bottom_frame,text = "paper", command = lambda: start("paper"))
paper.pack()

scissor = ttk.Button(bottom_frame,text="scissor", command = lambda: start("scissor"))
scissor.pack()

answer = ttk.Label(top_frame,text = "PLAYER: " + str(player) + " COMPUTER: "+str(AIpoints),font = 100)
answer.pack()

to = ttk.Label(dow,text = "")
to.pack()

your = tk.Label(middle_frame)
your.pack(side=tk.LEFT)

computery = tk.Label(middle_frame)
computery.pack(side=tk.RIGHT)

play_sound()

ro.mainloop()