import Tkinter as tk
from Tkinter import *
from ScrolledText import *
import tkFileDialog
from tkFileDialog import *
import tkMessageBox

root = Tk(className = "PyXCy")
pyxcy = ScrolledText(root, width = 100, height = 80)
done = 0;

def open_command():
	file = tkFileDialog.askopenfile(parent = root, mode = 'rb', title = 'Select a file')
	if file != None:
		contents = file.read()
		pyxcy.insert('1.0', contents)
		file.close()

def save_command():
    file = tkFileDialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    if file != None:
        data = pyxcy.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def saveas_command():
	file = asksaveasfile(mode = 'w', defaultextension = '.txt')
	data = pyxcy.get('1.0', END+'-1c')
	file.write(data)
	file.close()

def exit_command():
	if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
		root.destroy()

def for_command():
	tkMessageBox.showinfo("For", "People who code in C++")

def by_command():
	tkMessageBox.showinfo("By", "People who code in Python")

def documentation_command():
	tkMessageBox.showinfo("Documentation", "Made as a weekend Python project. For features refer github.")

def clear_command():
	pyxcy.delete('1.0', END)
	done = 0

def colorme(*args):
	print "hello"

menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Clear", command = clear_command)
filemenu.add_command(label = "Open", command = open_command)
filemenu.add_command(label = "Save", command = save_command)
filemenu.add_command(label = "Save As", command = saveas_command)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "For", command = for_command)
helpmenu.add_command(label = "By", command = by_command)
helpmenu.add_command(label = "Documentation", command = documentation_command)

#root.bind("hello", colorme)
pyxcy.tag_configure('color', foreground='blue')
pyxcy.insert(END, "This is blue\n", 'color')

pyxcy.pack()
root.mainloop()