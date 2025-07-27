import tkinter as tk
from time import strftime

def time():
    
    clock.config(text=strftime('%H:%M:%S'))
    clock.after(1000,time)
    
root=tk.Tk()
root.title('Digital Clock')

clock=tk.Label(root,font=('calibri', 40), background='black', foreground='cyan')
clock.pack(anchor='center')

time()
root.mainloop()    