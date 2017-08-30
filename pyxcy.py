import Tkinter
import ScrolledText

root = Tkinter.Tk(className = "PyXCy")
textpad = ScrolledText.ScrolledText(root, width = 100, height = 80)
textpad.pack()
root.mainloop()