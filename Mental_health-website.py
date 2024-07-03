from tkinter import *
import tkinter as tk 
import datetime as dt 
import sys 

main_window = tk.Tk()# the main window where the options are represented 
main_window.geometry("800x400")
main_window.title("Main Menu")

#---------------------------------------------------------------------------------------------------------------

#Below is anger
def Ahide_widget():
    anger.grid_forget()
    Ab1.configure(text="Show", command=Ashow_widget)
def Ashow_widget():
    anger.grid(row=1,column=3)
    Ab1.configure(text="Hide", command=Ahide_widget)

#Below is depression
def Dhide_widget():
    depression.grid_forget()
    Db1.configure(text="Show", command=Dshow_widget)
def Dshow_widget():
    depression.grid(row=2,column=3)
    Db1.configure(text="Hide", command=Dhide_widget)

#Below is stress
def Shide_widget():
    stress.grid_forget()
    Sb1.configure(text="Show", command=Sshow_widget)
def Sshow_widget():
    stress.grid(row=3,column=3)
    Sb1.configure(text="Hide", command=Shide_widget)
#---------------------------------------------------------------------------------------------------------------

#Below is anger
angerCho = tk.Label(main_window, 
                    text="Anger \nManagement", 
                    font='Aerial 12 bold', 
                    borderwidth=2, 
                    relief="solid", 
                    bg='#D61D1D')
angerCho.grid(row=1,column=1)

anger = tk.Label(main_window, 
                 text="""To manage anger effectively, 
                 start by pausing and taking deep breaths to calm 
                 \nyourself before reacting, which helps prevent 
                 impulsive actions. \nReflect on the specific triggers 
                 that caused your anger to understand the root of 
                 \nthe issue and develop better strategies for handling 
                 similar situations in the future.\nWhen expressing 
                 your feelings, use 'I' statements like 'I feel upset when...' 
                 \nto communicate your emotions constructively without blaming 
                 others, promoting a more \npeaceful and productive dialogue.""", 
                 font=('Aerial 8'), 
                 borderwidth=2, 
                 relief="groove", 
                 bg='#DB6565')

Ab1 = tk.Button(main_window, text="Show", command=Ashow_widget)
Ab1.grid(row=1,column=2,padx=1,pady=40)


#Below is depression
depressionCho = tk.Label(main_window, text="Depression", 
                         font='Aerial 12 bold', 
                         borderwidth=2, 
                         relief="solid", 
                         bg='#338CB7')

depressionCho.grid(row=2,column=1)

depression = tk.Label(main_window, 
                      text="""Managing depression effectively involves several steps. 
                      First, seek professional help \nfrom a therapist or doctor who can 
                      provide counseling and, if needed, medication.\nTake care of 
                      yourself by exercising regularly, eating healthy foods, 
                      and getting enough\nsleep,as these can all improve your mood. 
                      Surround yourself with supportive friends\nand family toreduce 
                      feelings of loneliness. Practice mindfulness or meditation, set 
                      small\nand achievable goals, and engage in activities you enjoy 
                      to help lift your spirits.""", 
                      font=('Aerial 8'), 
                      borderwidth=2, 
                      relief="groove",
                      bg='#8CCEED')

Db1 = tk.Button(main_window, text="Show", command=Dshow_widget)
Db1.grid(row=2,column=2,padx=1,pady=40)


#Below is stress
stressCho = tk.Label(main_window, 
                     text="Stress", 
                     font='Aerial 12 bold', 
                     borderwidth=2, 
                     relief="solid", 
                     bg='#FF6B1F')
stressCho.grid(row=3,column=1)

stress = tk.Label(main_window, text="""Managing stress involves several simple steps. First, identify what causes your stress so you can address it directly.\nPractice relaxation techniques like deep breathing, meditation, or yoga to calm yourself. Stay organized with a schedule or to-do list to manage tasks better. Exercise regularly to reduce stress hormones and boost your mood. Take breaks to relax and recharge. Talk to friends, family, or support groups to share your feelings and get support. Maintain a healthy lifestyle by eating well, sleeping enough, and avoiding too much caffeine or alcohol. Set boundaries and learn to say no to avoid taking on too much. If stress becomes overwhelming, seek help from a therapist or counselor. """, font=('Aerial 8'), 
                  borderwidth=2, 
                  relief="groove", 
                  bg='#E8A785')

Sb1 = tk.Button(main_window, text="Show", command=Sshow_widget)
Sb1.grid(row=3,column=2,padx=1,pady=40)

#---------------------------------------------------------------------------------------------------------------

mainWindow_icon = PhotoImage(file='Screenshot 2024-01-10 130335.png')
main_window.iconphoto(True,mainWindow_icon)
# main_window.config(background="#EDCDFF")

main_window.mainloop()