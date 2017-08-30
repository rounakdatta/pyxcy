import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

root = Tk(className = "PyXCy")
pyxcy = ScrolledText(root, width = 100, height = 80)

def open_command():
	file = tkFileDialog.askopenfile(parent = root, mode = 'rb', title = 'Select a file')
	if file != None:
		contents = file.read()
		pyxcy.insert('1.0', contents)
		file.close()

def save_command(self):
	file = tkFileDialog.asksaveasfile(mode = 'w')
	if file != None:
		data = self.pyxcy.get('1.0', END+'-lc')
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
	tkMessageBox.showinfo("Docu", "blah blah blah")

def clear_command():
	pyxcy.delete('1.0', END)

def dummy():
	print "Hello world"

menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Clear", command = clear_command)
filemenu.add_command(label = "Open", command = open_command)
filemenu.add_command(label = "Save", command = save_command)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "For", command = for_command)
helpmenu.add_command(label = "By", command = by_command)
helpmenu.add_command(label = "Documentation", command = documentation_command)

pyxcy.pack()
root.mainloop()