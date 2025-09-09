import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H: %M: %S: %P")
    # hour : Minute:second +  AM/PM
    label.config(text=current_time)
    label.after(1000, update_time)   #har 1 second baad time update karega

    #tkinter window
root = tk.TK()
root .title("digital clock")
root . geometry("400x200")
root . configure(bg="black")

#label for clock
label = tk . Label(root , font=("ds-digital",50),
background = "black",
foreground= "cyan")
label.pack(anchor="cetre")

root.mainloop()
    