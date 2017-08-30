import Tkinter
from Tkinter import Menu
import ScrolledText

root = Tkinter.Tk(className = "PyXCy")
textpad = ScrolledText.ScrolledText(root, width = 100, height = 80)

def dummy():
	print "Hello world"

menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New", command = dummy)
filemenu.add_command(label = "Open", command = dummy)
filemenu.add_command(label = "Save", command = dummy)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = dummy)
helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "For", command = dummy)
helpmenu.add_command(label = "By", command = dummy)
helpmenu.add_command(label = "Documentation", command = dummy)

textpad.pack()
root.mainloop()