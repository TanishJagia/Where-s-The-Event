from tkinter import *

window = Tk()
window.title("Event Handling")
window.geometry("100x100")

def on_click(event):
    print("Button was clicked!")
button = Button(window, text="Click Me!")
button.pack()
button.bind("<Button-1>", on_click)

def key_press(event):
    print(f"Key pressed: {event.char}")
window.bind("<Key>", key_press)
window.mainloop()