#program to create a listbox
from tkinter import*
top = Tk()
top.geometry("200x250")
#code to create a labe;
lbl = Label(top, text = "list of languages", activeforeground = "green", activebackground = "red")
#code to create a listbox
listbox = Listbox(top)
listbox.insert(1, "Java")
listbox.insert(2, "python")
listbox.insert(3, "C++")
listbox.insert(4, "C-sharp")
listbox.index(2)
listbox.size()
listbox.pack()
lbl.pack()
top.mainloop()
