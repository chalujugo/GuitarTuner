from tkinter import *
import sys
from playsound import playsound

import tkinter as tk

root = tk.Tk(className=" Guitar Tuner")
frame = tk.Frame(root)
frame.pack()

tunes = [["E1.mp3", "A.mp3", "D.mp3"], ["G.mp3", "B.mp3", "E2.mp3"]]
note = [["E1", "A", "D"], ["G", "B", "E2"]]
buttons = [[None] * 3 for _ in range(3)]
for i in range(3):
    for j in range(2):
        but = buttons[i][j]
        f = playsound("E2.mp3"); play = lambda: f.play()
        but = tk.Button(frame, text = note[j][i], relief=GROOVE, command = play)
        but.grid(row=i, column=j)


root.mainloop()

"""
gui = Tk(className=' Guitar Tuner')
gui.geometry("500x500")
frame = Frame(gui)
frame.pack(gui)

buttons = [[None] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        but = buttons[i][j]
        but = gui.Button(frame)
        but.grid(row=i, column=j)


# create button
E1 = Button(gui, text='My Button', width=15, height=15, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
E1.grid(column = 0, row = 0)

A = Button(gui, text='My Button', width=15, height=15, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
A.grid(column = 0, row = 1)


D = Button(gui, text='My Button', width=15, height=15, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
D.grid(column = 0, row = 2)

G = Button(gui, text='My Button', width=15, height=15, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
G.grid(column = 1, row = 0)

B = Button(gui, text='My Button', width=15, height=15, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
B.grid(column = 2, row = 0)

E2 = Button(gui, text='My Button', width=15, height=15, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
E2.grid(column = 2, row = 0)

# add button to gui window
E1.pack()
A.pack()
D.pack()
G.pack()
B.pack()
E2.pack()

gui.mainloop() 
"""