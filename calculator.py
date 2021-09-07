from tkinter import *

list1 = []
joinerlist = []
pressed = False
multiplication = False
addition = False
subtraction = False
division = False
afterdone = False
equals = False
decimal = False
justdone = False
justdecimal = False
initial = True
last = 5
count = 0

def appender(num):
	global multiplication
	global addition
	global decimal
	global subtraction
	global division
	global pressed
	global afterdone
	global equals
	global justdone
	global initial
	global justdecimal
	global last
	global count
	pressed = True
	list1.append(num)
	if multiplication == True:
		count = 0
		decimal = False
		justdecimal = False
		equals = False
		show_answer()
		initial = False
		list1.append(list1[-1]*list1[-2])
		multiplication = False
		afterdone = True
		justdone = True
		last = 0
	elif addition == True:
		count = 0
		decimal = False
		justdecimal = False
		equals = False
		show_answer()
		initial = False
		list1.append(list1[-1]+list1[-2])
		addition = False
		afterdone = True
		justdone = True
		last = 1
	elif subtraction == True:
		count = 0
		decimal = False
		justdecimal = False
		equals = False
		show_answer()
		initial = False
		list1.append(list1[-2]-list1[-1])
		subtraction = False
		afterdone = True
		justdone = True
		last = 2
	elif division == True:
		count = 0
		decimal = False
		justdecimal = False
		equals = False
		show_answer()
		initial = False
		list1.append(list1[-2]/list1[-1])
		division = False
		afterdone = True
		justdone = True
		last = 3
	elif equals == True:
		count = 0
		justdone = False
		decimal = False
		last = 5
		list1.clear()
		list1.append(num)
		show_answer()
		initial = True
		equals = False		
	elif initial == True:
		count = 0
		decimal = False
		justdecimal = False
		if len(list1) >= 2:
			joinerlist.append(list1[-2])
			joinerlist.append(list1[-1])
			list1.pop(-1)
			list1.pop(-1)
			joiner(joinerlist)
			joinerlist.clear()
			show_answer()
		else:
			show_answer()
	elif afterdone == True:
		count = 0
		decimal = False
		justdecimal = False
		joinerlist.append(list1[-3])
		joinerlist.append(list1[-1])
		list1.pop(-1)
		list1.pop(-1)
		list1.pop(-1)
		joiner(joinerlist)
		joinerlist.clear()
		show_answer()
		if last == 0:
			list1.append(list1[-1]*list1[-2])
		elif last == 1:
			list1.append(list1[-1]+list1[-2])
		elif last == 2:
			list1.append(list1[-2]-list1[-1])
		elif last == 3:
			list1.append(list1[-2]/list1[-1])
	elif decimal == True:
		if justdone == False:
			if justdecimal == True:
				count += 1
				newitem = 0 + round(num * 0.1, 2)
				list1.pop(-1)
				list1.append(newitem)
				justdecimal = False
				if last != 5:
					justdone = True
			elif count == 0:
				count += 1
				newitem = list1[-2] + round(num * 0.1, 2)
				list1.pop(-1)
				list1.pop(-1)
				list1.append(newitem)
			elif count == 1:
				joinerlist.append(list1[-2])
				joinerlist.append(num)
				stringlist = [str(integer) for integer in joinerlist]
				floater = float("".join(stringlist))
				list1.pop(-1)
				list1.pop(-1)
				list1.append(floater)
				joinerlist.clear()
		elif justdone == True:
			if count == 0:
				count += 1
				if justdecimal == True:
					newitem = 0 + round(num * 0.1, 2)
					list1.pop(-1)
					list1.append(newitem)
					justdecimal = False
				else:
					newitem = list1[-3] + round(num * 0.1, 2)
					list1.pop(-1)
					list1.pop(-1)
					list1.pop(-1)
					list1.append(newitem)
			elif count == 1:
				joinerlist.append(list1[-3])
				joinerlist.append(num)
				stringlist = [str(integer) for integer in joinerlist]
				floater = float("".join(stringlist))
				list1.pop(-1)
				list1.pop(-1)
				list1.pop(-1)
				list1.append(floater)
				joinerlist.clear()
		show_answer()
		if last !=5:
			joinerlist.append(list1[-1])
			joinerlist.append(list1[-2])
			stringlist = [str(integer) for integer in joinerlist]
			if len(stringlist[-1]) >= len(stringlist[-2]):
				if last == 0:
					list1.append(round(list1[-1]*list1[-2], len(stringlist[-1])))
				elif last == 1:
					list1.append(round(list1[-1]+list1[-2], len(stringlist[-1])))
				elif last == 2:
					list1.append(round(list1[-2]-list1[-1], len(stringlist[-1])))
				elif last == 3:
					list1.append(round(list1[-2]/list1[-1], len(stringlist[-1])))
			elif len(stringlist[-1]) < len(stringlist[-2]):
				if last == 0:
					list1.append(round(list1[-1]*list1[-2], len(stringlist[-2])))
				elif last == 1:
					list1.append(round(list1[-1]+list1[-2], len(stringlist[-2])))
				elif last == 2:
					list1.append(round(list1[-2]-list1[-1], len(stringlist[-2])))
				elif last == 3:
					list1.append(round(list1[-2]/list1[-1], len(stringlist[-2])))
			joinerlist.clear()
			stringlist.clear()		
def multiply():
	if pressed == False:
		pass
	elif pressed == True:
		global multiplication
		global addition
		global subtraction
		global division
		global justdecimal
		global last
		global count
		multiplication = True
		addition = False
		subtraction = False
		division = False
		justdecimal = True
		last = 0
		count = 0
def add():
	if pressed == False:
		pass
	elif pressed == True:
		global multiplication
		global addition
		global subtraction
		global division
		global justdecimal
		global last
		global count
		multiplication = False
		addition = True
		subtraction = False
		division = False
		justdecimal = True
		last = 1
		count = 0
def subtract():
	if pressed == False:
		pass
	elif pressed == True:
		global multiplication
		global addition
		global subtraction
		global division
		global justdecimal
		global last
		global count
		multiplication = False
		addition = False
		subtraction = True
		division = False
		justdecimal = True
		last = 2
		count = 0
def divide():
	if pressed == False:
		pass
	elif pressed == True:
		global multiplication
		global addition
		global subtraction
		global division
		global justdecimal
		global last
		global count
		multiplication = False
		addition = False
		subtraction = False
		division = True
		justdecimal = True
		last = 3
		count = 0
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
def equalsign():
	global equals
	global justdone
	global justdecimal
	justdecimal = True
	justdone = False
	equals = True
	if len(list1) >= 1:
		label['text'] = list1[-1]
	else:
		label['text'] = "answer"
def clearer():
	global initial
	global justdone
	global pressed
	global last
	global justdecimal
	last = 5
	initial = True
	justdone = False
	pressed = False
	justdecimal = True
	list1.clear()
	show_answer()
def dec():
	global initial
	global pressed
	global decimal
	global afterdone
	global justdecimal
	global multiplication
	global addition
	global subtraction
	global division
	global equals
	multiplication = False
	addition = False
	subtraction = False
	division = False
	equals = False
	if pressed == False:
		justdecimal = True
		decimal = True
		initial = False
	if justdecimal == True:
		label['text'] = "0."
	elif afterdone == False:
		joinerlist.append(str(list1[-1]))
		joinerlist.append(".")
		label['text'] = "".join(joinerlist)
		joinerlist.clear()
	elif afterdone == True:
		joinerlist.append(str(list1[-2]))
		joinerlist.append(".")
		label['text'] = "".join(joinerlist)
		joinerlist.clear()
	if pressed == True:
		decimal = True
		initial = False
		afterdone = False


 
root = Tk()
root.geometry("240x95")
root.title("Calculator")
root.configure(background="black")
btn1 = Button(root, text = "1", width = "1", bd = "5", command=lambda : appender(1))
btn2 = Button(root, text = "2", width = "1", bd = "5", command=lambda : appender(2))
btn3 = Button(root, text = "3", width = "1", bd = "5", command=lambda : appender(3))
btn4 = Button(root, text = "4", width = "1", bd = "5", command=lambda : appender(4))
btn5 = Button(root, text = "5", width = "1", bd = "5", command=lambda : appender(5))
btn6 = Button(root, text = "6", width = "1", bd = "5", command=lambda : appender(6))
btn7 = Button(root, text = "7", width = "1", bd = "5", command=lambda : appender(7))
btn8 = Button(root, text = "8", width = "1", bd = "5", command=lambda : appender(8))
btn9 = Button(root, text = "9", width = "1", bd = "5", command=lambda : appender(9))
btn10 = Button(root, text = "0", width = "1", bd = "5", command=lambda : appender(0))
btn11 = Button(root, text = "x", width = "1", bd = "5", command=lambda : multiply())
btn12 = Button(root, text = "+", width = "1", bd = "5", command=lambda : add())
btn13 = Button(root, text = "-", width = "1", bd = "5", command=lambda : subtract())
btn14 = Button(root, text = "/", width = "1", bd = "5", command=lambda : divide())
btn15 = Button(root, text = "=", width = "1", bd = "5", command=equalsign)
btn16 = Button(root, text = "C", width = "1", bd = "5", command=lambda : clearer())
btn17 = Button(root, text = ".", width = "1", bd = "5", command=lambda: dec())
label = Label(root, text="answer", bg="black", fg="white", font="arial 12 bold")

btn1.grid(row = 0, column = 0)
btn2.grid(row = 0, column = 1)
btn3.grid(row= 0, column = 2)
btn4.grid(row=1, column = 0)
btn5.grid(row=1, column = 1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btn10.grid(row=2, column=6)
btn11.grid(row=0, column=6)
btn12.grid(row=0, column=7)
btn13.grid(row=1, column=7)
btn14.grid(row=1, column=6)
btn15.grid(row=1, column=8)
btn16.grid(row=0, column=8)
btn17.grid(row=3, column=3)
label.grid(row=1, column=9)

root.mainloop()

	
print(list1)
