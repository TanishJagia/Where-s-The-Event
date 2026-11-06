from tkinter import *
from tkinter import messagebox 

root = Tk()
root.geometry("200x200")
root.title("Popup Example")

def msg():
    messagebox.showerror("Error", "This is an error message!")
button = Button(root, text="Show Error", command=msg)
button.pack()

root.mainloop()
