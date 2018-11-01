#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:25:47 2018

@author: madeshturaka
"""
from tkinter import *
root = Tk()
root.title("KIDS LEARNING GAME")
root.geometry("500x500")
root.configure(background='gray')
def show(frame):
    frame.grid(row=0, column=0, sticky = 'news')
    frame.tkraise()
def show_bottom(frame):
    frame.tkraise()
def result(frame):
    for f in (f0, f1, f2, f00, f11, f22, fwin, fw, flose):
        f.grid_forget()
    frame.grid()
    frame.tkraise()
    
f0 = Frame(root, bg ='gray')
f1 = Frame(root, bg ='gray')
f2 = Frame(root, bg ='gray')

fw = Frame(root)
fwin = Frame(root)
flose = Frame(root)
f00 = Frame(root)
f11 = Frame(root)
f22 = Frame(root)

 # welcome
 
imgW = PhotoImage(file='Welk_350x300.png')
LW = Label(fw, image= imgW).grid(row=0, column=0, padx = 70)
Button(fw, text='PLAY', command = lambda:show(f0)).grid()
fw.grid(row=0,column=0) 
 # Zeroth Frame Design
 
imgf00 = PhotoImage(file='lion_150x100.png')
imgf01 = PhotoImage(file='star_150x100.png')
imgf02 = PhotoImage(file='triangle_150x100.png')
imgf03 = PhotoImage(file='rabbit_150x100.png')
imgf04 = PhotoImage(file='red.png')

Lf00 = Label(f0, image = imgf00)
Lf00.grid(row = 0, column = 2)

Lf01 = Label(f0, image = imgf01)
Lf01.grid(row = 0, column = 4)

Lf02 = Label(f0, image = imgf02)
Lf02.grid(row = 1, column = 2)

Lf03 = Label(f0, image = imgf03)
Lf03.grid(row = 1, column = 4)

Lf04 = Label(f0, image = imgf04, height = 100, width = 150)
Lf04.grid(row = 2, column = 3)

Rf0 = Button(f0, text ='Refresh', command = lambda: show(f1)).grid(row = 5, column =2)
Of0 = Button(f0, text ='OK', command = lambda:[show_bottom(f00), clear(), init_frame_bottom()]).grid(row = 5, column = 4)

 # First Frame Design
 
imgf10 = PhotoImage(file='pentagon_150x100.png')
imgf11 = PhotoImage(file='sheep_150x100.png')
imgf12 = PhotoImage(file='monke_150x100.png')
imgf13 = PhotoImage(file='green.png')
imgf14 = PhotoImage(file='circle_150x100.png')


Lf10 = Label(f1, image = imgf10)
Lf10.grid(row = 0, column = 2)

Lf11 = Label(f1, image = imgf11)
Lf11.grid(row = 0, column = 4)

Lf12 = Label(f1, image = imgf12)
Lf12.grid(row = 1, column = 2)

Lf13 = Label(f1, image = imgf13, height=100, width = 150)
Lf13.grid(row = 1, column = 4)

Lf14 = Label(f1, image = imgf14)
Lf14.grid(row = 2, column = 3)

Rf1 = Button(f1, text ='Refresh', command = lambda:show(f2)).grid(row = 5, column =2)
Of1 = Button(f1, text ='OK', command = lambda: [show_bottom(f11), clear(), init_frame_bottom()]).grid(row = 5, column = 4)

 # Second Frame Design

imgf20 = PhotoImage(file='chicken_150x100.png')
imgf21 = PhotoImage(file='monke_150x100.png')
imgf22 = PhotoImage(file='sheep_150x100.png')
imgf23 = PhotoImage(file='lion_150x100.png')
imgf24 = PhotoImage(file='rabbit_150x100.png')


Lf20 = Label(f2, image = imgf20 )
Lf20.grid(row = 0, column = 2)

Lf21 = Label(f2, image = imgf21)
Lf21.grid(row = 0, column = 4)

Lf22 = Label(f2, image = imgf22)
Lf22.grid(row = 1, column = 2)

Lf23 = Label(f2, image = imgf23, height=100, width = 150)
Lf23.grid(row = 1, column = 4)

Lf24 = Label(f2, image = imgf24)
Lf24.grid(row = 2, column = 3)

Rf2 = Button(f2, text ='Refresh', command = lambda: show(f0)).grid(row = 5, column =2)
Of2 = Button(f2, text ='OK', command = lambda: [show_bottom(f22),clear(), init_frame_bottom()]).grid(row = 5, column = 4)

 # Bottom Frames Design
score = IntVar()
Sla0 = Label(f00, text = 'SCORE : ')
Sla1 = Label(f11, text = 'SCORE : ')
Sla2 = Label(f22, text = 'SCORE : ')
SL0 = Label(f00, textvariable = score)
SL1 = Label(f11, textvariable = score)
SL2 = Label(f22, textvariable = score)

 # Win Frame
imgwin = PhotoImage(file='Fwin_400x300.png')
Lwin = Label(fwin, image = imgwin).grid(row=0, column=0)
Button(fwin, text='Play Again', command = lambda:show(f0)).grid()
Button(fwin, text='QUIT', command = quit).grid()
fwin.grid_forget()

# Lose frame
imgLose = PhotoImage(file='kid_lose_350x300.png')
Llose = Label(flose, image = imgLose).grid(row=0, column=0)
Button(flose, text='Play Again', command = lambda:show(f0)).grid()
Button(flose, text='QUIT', command = quit).grid()
flose.grid_forget()

def check(val):
    entered_list=[var0.get(),var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get()]
    answer_list=['lion','star','rabbit','triangle','red','pentagon','sheep','monkey','green','circle','chicken']
    #score = IntVar()
    count = 0
    if val == 0 :
        answers_list=['lion','star','triangle','rabbit','red']
        for x in entered_list:
            if x in answers_list:
                count+=1
        score.set(count)
        Sla0.grid(row = 6 , column = 7 )
        SL0.grid(row = 6 , column = 8 )
        
    if val == 1 :
        answers_list=['pentagon','sheep','monkey','green','circle']
        for x in entered_list:
            if x in answers_list:
                count+=1
        score.set(count)
        Sla1.grid(row =6 , column =3 )
        SL1.grid(row = 6, column = 4)
        
    if val == 2 :
        answers_list=['chicken','monkey','sheep','lion','rabbit']
        print(entered_list)
        for x in entered_list:
            if x in answers_list:
                count+=1
        score.set(count)
        Sla2.grid(row =6 , column =3 )
        SL2.grid(row = 6, column =4 )
    
    if score.get() is 5:
        print('working.....')
        result(fwin)
    elif score.get() < 3:
        result(flose)

def quit():
    root.quit()

def clear():
    score.set(0)
    SL0.grid_remove()
    SL1.grid_remove()
    SL2.grid_remove()
    Sla0.grid_remove()
    Sla1.grid_remove()
    Sla2.grid_remove()
    var0.set(0)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
def init_frame_bottom():
    for frame in (f00, f11, f22):
        frame.grid(row=1, column=0, sticky ='news')        
var0 = StringVar()
var1 = StringVar() 
var2 = StringVar() 
var3 = StringVar() 
var4 = StringVar() 
var5 = StringVar() 
var6 = StringVar() 
var7 = StringVar() 
var8 = StringVar() 
var9 = StringVar() 
var10 = StringVar() 
 # F00----------
Checkbutton(f00, text='Lion    ', variable = var0, onvalue='lion').grid(row= 6 , column=2 )
Checkbutton(f00, text = 'Star    ', variable = var1, onvalue='star').grid(row=6, column=5)
Checkbutton(f00, text='Rabbit  ', variable = var2, onvalue='rabbit').grid(row= 7, column=2 )
Checkbutton(f00, text = 'Red     ', variable = var3, onvalue='red').grid(row=7, column=5)
Checkbutton(f00, text='Pentagon', variable = var4, onvalue='pentagon').grid(row= 8, column= 2)
Checkbutton(f00, text = 'Sheep   ', variable = var5, onvalue='sheep').grid(row=8, column=5)
Checkbutton(f00, text = 'Monkey  ', variable = var6, onvalue='monkey').grid(row=9, column=2)
Checkbutton(f00, text='Green   ', variable = var7, onvalue='green').grid(row= 9, column=5 )
Checkbutton(f00, text = 'Circle  ', variable = var8, onvalue='circle').grid(row=10, column=2)
Checkbutton(f00, text='Chicken ', variable = var9, onvalue='chicken').grid(row=10 , column= 5)
Checkbutton(f00, text='Triangle', variable = var10, onvalue='triangle').grid(row=11 , column= 2)
Button(f00, text = 'SUBMIT', command= lambda: check(0)).grid(row=8, column=7)
Button(f00, text = 'QUIT', command = quit).grid(row =8, column=9)
 # F11----------
Checkbutton(f11, text='triangle', variable = var0, onvalue='triangle').grid(row= 6 , column=1 )
Checkbutton(f11, text = 'Star    ', variable = var1, onvalue='star').grid(row=6, column=2)
Checkbutton(f11, text='Green   ', variable = var2, onvalue='green').grid(row= 7, column=1 )
Checkbutton(f11, text = 'Red     ', variable = var3, onvalue='red').grid(row=7, column=2)
Checkbutton(f11, text='Chicken ', variable = var4, onvalue='chicken').grid(row= 8, column= 1)
Checkbutton(f11, text = 'Sheep   ', variable = var5, onvalue='sheep').grid(row=8, column=2)
Checkbutton(f11, text = 'Monkey  ', variable = var6, onvalue='monkey').grid(row=9, column=1)
Checkbutton(f11, text='Rabbit', variable = var7, onvalue='rabbit').grid(row= 9, column=2 )
Checkbutton(f11, text = 'Circle  ', variable = var8, onvalue='circle').grid(row=10, column=1)
Checkbutton(f11, text='Pentagon', variable = var9, onvalue='pentagon').grid(row=10 , column= 2)
Checkbutton(f11, text='Lion    ', variable = var10, onvalue='lion').grid(row=11 , column= 1)
Button(f11, text = 'SUBMIT', command= lambda: check(1)).grid(row=8, column=3)
Button(f11, text = 'QUIT', command = quit).grid(row =8, column=9)
 # F22-------------
Checkbutton(f22, text='Sheep   ', variable = var0, onvalue='sheep').grid(row= 6 , column=1 )
Checkbutton(f22, text = 'Circle  ', variable = var1, onvalue='circle').grid(row=6, column=2)
Checkbutton(f22, text='Rabbit  ', variable = var2, onvalue='rabbit').grid(row= 7, column=1 )
Checkbutton(f22, text = 'Triangle', variable = var3, onvalue='triangle').grid(row=7, column=2)
Checkbutton(f22, text='Pentagon', variable = var4, onvalue='pentagon').grid(row= 8, column= 1)
Checkbutton(f22, text = 'Lion    ', variable = var5, onvalue='lion').grid(row=8, column=2)
Checkbutton(f22, text = 'Monkey  ', variable = var6, onvalue='monkey').grid(row=9, column=1)
Checkbutton(f22, text='Green   ', variable = var7, onvalue='green').grid(row= 9, column=2 )
Checkbutton(f22, text = 'Star    ', variable = var8, onvalue='star').grid(row=10, column=1)
Checkbutton(f22, text='Chicken', variable = var9, onvalue='chicken').grid(row=10 , column= 2)
Checkbutton(f22, text='Red     ', variable = var10, onvalue='red').grid(row=11 , column= 1)
Button(f22, text = 'SUBMIT', command= lambda: check(2)).grid(row=8, column=3)
Button(f22, text = 'QUIT', command = quit).grid(row =8, column=9)

root.mainloop()