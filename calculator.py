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
	global joinnum
	global afterdone
	global initial
	pressed = True
	global last
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
	if len(joinerlist) >= 1:
		strings = [str(integer) for integer in joinerlist]
		a_string = "".join(strings)
		an_integer = int(a_string)
		list1.append(an_integer)
 
root = Tk()
root.geometry("300x600")
btn1 = Button(root, text = "1", bd = "5", command=lambda : appender(1))
btn2 = Button(root, text = "2", bd = "5", command=lambda : appender(2))
btn3 = Button(root, text = "3", bd = "5", command=lambda : appender(3))
btn4 = Button(root, text = "4", bd = "5", command=lambda : appender(4))
btn5 = Button(root, text = "5", bd = "5", command=lambda : appender(5))
btn6 = Button(root, text = "6", bd = "5", command=lambda : appender(6))
btn7 = Button(root, text = "7", bd = "5", command=lambda : appender(7))
btn8 = Button(root, text = "8", bd = "5", command=lambda : appender(8))
btn9 = Button(root, text = "9", bd = "5", command=lambda : appender(9))
btn10 = Button(root, text = "x", bd = "5", command=lambda : multiply())
btn11 = Button(root, text = "+", bd = "5", command=lambda : add())
btn12 = Button(root, text = "-", bd = "5", command=lambda : subtract())
btn13 = Button(root, text = "/", bd = "5", command=lambda : divide())

btn1.pack(side="top")
btn2.pack(side="top")
btn3.pack(side="top")
btn4.pack(side="top")
btn5.pack(side="top")
btn6.pack(side="top")
btn7.pack(side="top")
btn8.pack(side="top")
btn9.pack(side="top")
btn10.pack(side="top")
btn11.pack(side="top")
btn12.pack(side="top")
btn13.pack(side="top")


root.mainloop()

	
print(list1)
