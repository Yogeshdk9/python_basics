from tkinter import *

root_window = tk.Tk()
root_window.title("Masterclass in Python 47")
root_window.geometry("500x500")

msg = tk.Label(root_window, text="Hello GUI World-Yogesh")
msg.grid(row=0, column=0)

btn = tk.Button(root_window, text="Exit", command=exit)
btn.grid(row=1, column=0)

root_window.mainloop()
