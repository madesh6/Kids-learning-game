#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:58:51 2018

@author: madeshturaka
"""
'''from tkinter import *
root = Tk()

f = Frame(root)

var1 = StringVar()
#var1 =  var2 = var3 =var4 =StringVar()
var2 =  StringVar()
var3 =  StringVar()
var4 =  StringVar()

def mget(val):
    entered_list = [var1.get(), var2.get(), var3.get(), var4.get()]
    answer_list = ['chicken','sheep']
    li =[]
    if len(entered_list) > len(answer_list):
        f.destroy()
    score = IntVar()
    jk =0
    for x in range(4):
        for y in range(4):
            if entered_list[x] == answer_list[y]:
                jk+=1
                li.append(entered_list[x])
        if entered_list[x] == answer_list[x]:
            jk += 1
            li.append(entered_list[x])
    print(li, jk)
    score.set(jk) 
    #score.set(y)
    sl = Label(f, textvariable = score)
    sl.grid(row=6, column =2)
cb1 = Checkbutton(f, text = 'Lion', variable = var1, onvalue='lion', offvalue='hi')
cb1.grid(row=0, column=1)
cb2 = Checkbutton(f, text = 'Rabbit', variable = var2, onvalue='rabbit', offvalue='hi')
cb2.grid(row=1, column=1)
cb3 = Checkbutton(f, text = 'Chicken', variable = var3, onvalue='chicken', offvalue='hi')
cb3.grid(row=0, column=2)
cb4 = Checkbutton(f, text = 'Sheep',variable = var4, onvalue='sheep', offvalue='emp')
cb4.grid(row=1, column=2)
b = Button(f, text='GET VALUES', command = lambda:mget(6))
b.grid(row=5, column=3)


f.pack()
root.mainloop() '''

## Animation gif

from tkinter import *
import time
import os
root = Tk()

frames = [PhotoImage(file='winner.gif',format = 'gif -index %i' %(i)) for i in range(100)]

def update(ind):

    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()