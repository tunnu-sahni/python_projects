from tkinter import *
import time

def update_time():
    current_time = time.strftime("%H:%M:%S%P")
    label.config(text=current_time)
    label.after(1000, update_time)
    #update every second

root = Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="black")

label = Label(root, font=("ds-digital",50), bg="black", fg="cyan")
label.pack(anchor="center")

update_time
root.mainloop()              