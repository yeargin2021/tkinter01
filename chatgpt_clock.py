import tkinter as tk
import time

class Clock:
    def __init__(self, master):
        self.master = master
        master.title("Clock")

        self.time_label = tk.Label(master, font=("Arial", 80))
        self.time_label.pack()

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_clock)

root = tk.Tk()
clock = Clock(root)
root.mainloop()
