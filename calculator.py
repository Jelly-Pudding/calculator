from tkinter import *

list1 = []
joinerlist = []
pressed = False
multiplication = False
addition = False
subtraction = False
division = False
afterdone = False
initial = True
last = 0


def appender(num):
	global multiplication
	global addition
	global subtraction
	global division
	global pressed
	global afterdone
	global initial
	global last
	pressed = True
	list1.append(num)
	if multiplication == True:
		initial = False
		list1.append(list1[-1]*list1[-2])
		multiplication = False
		afterdone = True
		last = 0
	elif addition == True:
		initial = False
		list1.append(list1[-1]+list1[-2])
		addition = False
		afterdone = True
		last = 1
	elif subtraction == True:
		initial = False
		list1.append(list1[-2]-list1[-1])
		subtraction = False
		afterdone = True
		last = 2
	elif division == True:
		initial = False
		list1.append(list1[-2]/list1[-1])
		division = False
		afterdone = True
		last = 3
	elif initial == True:
		if len(list1) >= 2:
			joinerlist.append(list1[-2])
			joinerlist.append(list1[-1])
			list1.pop(-1)
			list1.pop(-1)
			joiner(joinerlist)
			joinerlist.clear()
	elif afterdone == True:
		joinerlist.append(list1[-3])
		joinerlist.append(list1[-1])
		list1.pop(-1)
		list1.pop(-1)
		list1.pop(-1)
		joiner(joinerlist)
		joinerlist.clear()
		if last == 0:
			list1.append(list1[-1]*list1[-2])
		elif last == 1:
			list1.append(list1[-1]+list1[-2])
		elif last == 2:
			list1.append(list1[-2]-list1[-1])
		elif last == 3:
			list1.append(list1[-2]/list1[-1])
def multiply():
	if pressed == False:
		pass
	elif pressed == True:
		global multiplication
		global addition
		global subtraction
		global division
		multiplication = True
		addition = False
		subtraction = False
		division = False
def add():
	if pressed == False:
		pass
	elif pressed == True:
		global multiplication
		global addition
		global subtraction
		global division
		multiplication = False
		addition = True
		subtraction = False
		division = False
def subtract():
	if pressed == False:
		pass
	elif pressed == True:
		global multiplication
		global addition
		global subtraction
		global division
		multiplication = False
		addition = False
		subtraction = True
		division = False
def divide():
	if pressed == False:
		pass
	elif pressed == True:
		global multiplication
		global addition
		global subtraction
		global division
		multiplication = False
		addition = False
		subtraction = False
		division = True
def joiner(joinerlist):
	strings = [str(integer) for integer in joinerlist]
	a_string = "".join(strings)
	an_integer = int(a_string)
	list1.append(an_integer)
def show_answer():
	if len(list1) >= 1:
		label['text'] = list1[-1]
	else:
		label['text'] = "answer"
def clearer():
	global initial
	global pressed
	initial = True
	pressed = False
	list1.clear()
 
root = Tk()
root.geometry("300x250")
btn1 = Button(root, text = "1", bd = "5", command=lambda : appender(1))
btn2 = Button(root, text = "2", bd = "5", command=lambda : appender(2))
btn3 = Button(root, text = "3", bd = "5", command=lambda : appender(3))
btn4 = Button(root, text = "4", bd = "5", command=lambda : appender(4))
btn5 = Button(root, text = "5", bd = "5", command=lambda : appender(5))
btn6 = Button(root, text = "6", bd = "5", command=lambda : appender(6))
btn7 = Button(root, text = "7", bd = "5", command=lambda : appender(7))
btn8 = Button(root, text = "8", bd = "5", command=lambda : appender(8))
btn9 = Button(root, text = "9", bd = "5", command=lambda : appender(9))
btn10 = Button(root, text = "0", bd = "5", command=lambda : appender(0))
btn11 = Button(root, text = "x", bd = "5", command=lambda : multiply())
btn12 = Button(root, text = "+", bd = "5", command=lambda : add())
btn13 = Button(root, text = "-", bd = "5", command=lambda : subtract())
btn14 = Button(root, text = "/", bd = "5", command=lambda : divide())
btn15 = Button(root, text = "=", bd = "7", command=show_answer)
btn16 = Button(root, text = "AC", bd = "7", command=lambda : clearer())
label = Label(root, text="answer")

btn1.grid(row = 0, column = 0)
btn2.grid(row = 0, column = 1)
btn3.grid(row= 0, column = 2)
btn4.grid(row=1, column = 0)
btn5.grid(row=1, column = 1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btn10.grid(row=3, column=1)
btn11.grid(row=0, column=6)
btn12.grid(row=0, column=7)
btn13.grid(row=0, column=8)
btn14.grid(row=1, column=7)
btn15.grid(row=1, column=9)
btn16.grid(row=0, column=9)
label.grid(row=0, column=10)

root.mainloop()

	
print(list1)
