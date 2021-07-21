from tkinter import *
import sys
from playsound import playsound

import tkinter as tk
from tkinter.ttk import *

root = tk.Tk(className=" Guitar Tuner")
root.geometry("500x500")
frame = tk.Frame(root)
frame.pack()


tunes = [["E1.mp3", "A.mp3", "D.mp3"], ["G.mp3", "B.mp3", "E2.mp3"]]
note = [["E1", "A", "D"], ["G", "B", "E2"]]


def playE1(): return playsound("Tune/E1.mp3")


E1 = tk.Button(frame, text="E1", width=10, height=10,
               relief=GROOVE, command=playE1)
E1.grid(row=2, column=0)


def playA(): return playsound("Tune/A.mp3")


A = tk.Button(frame, text="A", width=10, height=10,
              relief=GROOVE, command=playA)
A.grid(row=1, column=0)


def playD(): return playsound("Tune/D.mp3")


D = tk.Button(frame, text="D", width=10, height=10,
              relief=GROOVE, command=playD)
D.grid(row=0, column=0)


def playG(): return playsound("Tune/G.mp3")


G = tk.Button(frame, text="G", width=10, height=10,
              relief=GROOVE, command=playG)
G.grid(row=0, column=2)


def playB(): return playsound("Tune/B.mp3")


B = tk.Button(frame, text="B", width=10, height=10,
              relief=GROOVE, command=playB)
B.grid(row=1, column=2)


def playE2(): return playsound("Tune/E2.mp3")


E2 = tk.Button(frame, text="E2", width=10, height=10,
               relief=GROOVE, command=playE2)
E2.grid(row=2, column=2)

root.mainloop()
