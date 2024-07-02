from tkinter import *
import tkinter as tk 
import datetime as dt 
import sys 

main_window = tk.Tk()# the main window where the options are represented 
main_window.geometry("600x300")
main_window.title("Main Menu")

#---------------------------------------------------------------------------------------------------------------

def Ahide_widget():
    anger.grid_forget()
    Ab1.configure(text="Show", command=Ashow_widget)
def Ashow_widget():
    anger.grid(row=1,column=3)
    Ab1.configure(text="Hide", command=Ahide_widget)

def Dhide_widget():
    depression.grid_forget()
    Db1.configure(text="Show", command=Dshow_widget)
def Dshow_widget():
    depression.grid(row=2,column=3)
    Db1.configure(text="Hide", command=Dhide_widget)

#---------------------------------------------------------------------------------------------------------------

#Below is anger
angerCho = tk.Label(main_window, text="Anger \nManagement", font='Aerial')
angerCho.grid(row=1,column=1)

anger = tk.Label(main_window, text="To manage anger effectively, start by pausing and taking deep breaths to calm \nyourself before reacting, which helps prevent impulsive actions. \nReflect on the specific triggers that caused your anger to understand the root of \nthe issue and develop better strategies for handling similar situations in the future.\nWhen expressing your feelings, use 'I' statements like 'I feel upset when...' \nto communicate your emotions constructively without blaming others, promoting a more \npeaceful and productive dialogue.", font=('Aerial 8'))

Ab1 = tk.Button(main_window, text="Show", command=Dshow_widget)
Ab1.grid(row=1,column=2,padx=1,pady=40)

#Below is depression
depressionCho = tk.Label(main_window, text="Anger \nManagement", font='Aerial')
depressionCho.grid(row=2,column=1)


depression = tk.Label(main_window, text="To manage anger effectively, start by pausing and taking deep breaths to calm \nyourself before reacting, which helps prevent impulsive actions. \nReflect on the specific triggers that caused your anger to understand the root of \nthe issue and develop better strategies for handling similar situations in the future.\nWhen expressing your feelings, use 'I' statements like 'I feel upset when...' \nto communicate your emotions constructively without blaming others, promoting a more \npeaceful and productive dialogue.", font=('Aerial 8'))

# Add a Button widget
Db1 = tk.Button(main_window, text="Show", command=Dshow_widget)
Db1.grid(row=2,column=2,padx=1,pady=40)

#---------------------------------------------------------------------------------------------------------------

mainWindow_icon = PhotoImage(file='Screenshot 2024-01-10 130335.png')
main_window.iconphoto(True,mainWindow_icon)
main_window.config(background="#EDCDFF")

main_window.mainloop()