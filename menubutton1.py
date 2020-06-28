from tkinter import Toplevel, Button, Tk, Menu
top = Tk()
top.geometry("300x400")
menubar = Menu(top)

file = Menu(menubar, tearoff = 0)
file.add_command(label = "New")
file.add_command(label = "Open")
file.add_command(label = "Save")
file.add_command(label = "Save As..")
file.add_command(label = "close")
#used to add a separator
file.add_separator()
file.add_command(label = "Exit", command = top.quit)

menubar.add_cascade(label = "File", menu = file)
edit = Menu(menubar, tearoff = 0)
edit.add_command(label = "Undo")

edit.add_separator()

edit.add_command(label = "Cut")
edit.add_command(label = "Copy")
edit.add_command(label = "Paste")
edit.add_command(label = "Delete")
edit.add_command(label = "Select All")

menubar.add_cascade(label = "Edit", menu = edit)
help = Menu(menubar, tearoff = 0)
help.add_command(label = "About")
menubar.add_cascade(label = "Help", menu = edit)
top.config(menu = menubar)

top.mainloop()

