from tkinter import *
import tkinter as tk 
import datetime as dt 

main_window = tk.Tk()# the main window where the options are represented 
main_window.geometry("600x300")
main_window.title("Main Menu")

label1 = Label(main_window,text="Hello this is the main menu.")

mainWindow_icon = PhotoImage(file='Screenshot 2024-01-10 130335.png')
main_window.iconphoto(True,mainWindow_icon)
main_window.config(background="#EDCDFF")

main_window.mainloop()