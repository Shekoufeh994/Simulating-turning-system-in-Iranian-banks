
from tkinter import *
from pygame import mixer
import time

turn = Tk()
turn.title("Turning program")
turn.geometry("500x300")
turn.resizable(False,False)
turn.configure(bg="black") 

LblResult = Label(turn,width=50, height=2, text="",font=("arial",30,"bold"))
LblResult.pack()
'''
lbl = Label(turn, font=('calibri', 40, 'bold'),
            background='green',
            foreground='white')

lbl.pack(anchor='center')
'''
def Readme(name):
	
	# FileLocation = "wav/" + "user1.mp3"
	FileLocation = "wav/" + "shomare.mp3"
	mixer.init()
	mixer.music.load(FileLocation)
	mixer.music.play()
	time.sleep(1)

	FileLocation = "wav/" + name
	mixer.init()
	mixer.music.load(FileLocation)
	mixer.music.play()


counter = 1
def display(num):
	
	
	LblResult.configure(text= counter)

	if counter == 1:
		print("one")
		Readme("1.mp3")
	elif  counter == 2:
		print("2")
		Readme("2.mp3")
	elif  counter == 3:
		print("3")
		Readme("3.mp3")
	elif  counter == 4:
		print("4")
		Readme("4.mp3")
	elif  counter == 5:
		Readme("5.mp3")
		print("5")
	elif  counter == 6:
		Readme("6.mp3")
		print("6")
	elif  counter >= 7:
		LblResult.configure(text="error")
	

	
		



def Turn(val):
	global counter 
	
	counter += int(val)

	LblResult.configure(text= counter)
	
	if counter == 1:
		print("one")
		Readme("1.mp3")
	elif  counter == 2:
		print("2")
		Readme("2.mp3")
	elif  counter == 3:
		print("3")
		Readme("3.mp3")
	elif  counter == 4:
		print("4")
		Readme("4.mp3")
	elif  counter == 5:
		Readme("5.mp3")
		print("5")
	elif  counter == 6:
		Readme("6.mp3")
		print("6")
	elif  counter >= 7:
		LblResult.configure(text="error")

Button(turn,text="Dec Turn", width=8, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="purple",command=lambda:display("1")).place(x=30,y=150)
Button(turn,text="Next Turn", width=8, height=1, font=("arial",30,"bold"),bd=1,fg="white",bg="pink",command=lambda:Turn("1")).place(x=270,y=150)




turn.mainloop()	