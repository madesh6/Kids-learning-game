#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 22:14:50 2018

@author: madeshturaka
"""

from tkinter import *



root = Tk()
root.title('Kids Learning Game')
root.geometry("800x880")
frame0= Frame(root)

def menu():
    l0.grid_forget()
    play.grid_forget()
    b1.grid()
    b2.grid()
    b3.grid()
    l1.grid(row=0, column=4)
    l2.grid(row=1, column=4)
    l3.grid(row=2, column=4)
    
    
    
def colors():
    b1.grid_forget()
    b2.grid_forget()
    b3.grid_forget()
    l1.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    
    
    answer=[]
    color_text = ['red', 'green', 'blue', 'black', 'orange']
    
    C1 = Label( frame0, image= imgC1, height = 100, width = 150)
    C1.grid(row=0, column=10)
    E1.grid()
    
    
    C2 = Label( frame0, image= imgC2, height = 100, width = 150)
    C2.grid(row=3, column=4)
    E2.grid()
    
    C3 = Label( frame0, image= imgC3, height = 100, width = 150)
    C3.grid(row=6, column=10)
    E3.grid()
    
    C4 = Label( frame0, image= imgC4, height = 100, width = 150)
    C4.grid(row=8, column=4)
    E4.grid()
    
    C5 = Label( frame0, image= imgC5, height = 100, width = 150)
    C5.grid(row=10, column=10)
    E5.grid()
    
    Sub = Button( frame0, text='SUBMIT' , command = checkC )
    Sub.grid(row=14, column =6)
    

def checkC():
     answers = [E1.get(),E2.get(),E3.get(),E4.get(),E5.get()]
     color_text = ['red', 'green', 'blue', 'black', 'orange']
     animal_text = ['lion','rabbit','monkey','chicken','sheep']
     shape_text = ['star','circle','triangle','rectangle','pentagon']
     if answers == color_text:
         
         Win = Label( frame0, image = imgWIN)
         Win.grid(row = 15, column=20)
     elif answers == animal_text:
         Win = Label( frame0, image = imgWIN)
         Win.grid(row = 15, column=20)
     elif answers == shape_text:
         Win = Label( frame0, image = imgWIN)
         Win.grid(row = 15, column=20)
     else:    
         Lose = Label( frame0, image = imgLOSE)
         Lose.grid(row = 15, column = 20)
     
     
        
    
 
    
    
def shapes():
    b1.grid_forget()
    b2.grid_forget()
    b3.grid_forget()
    l1.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    
    S1 = Label( frame0, image= imgS1, height = 100, width = 150)
    S1.grid(row=0, column=10)
    E1.grid()
    
    
    S2 = Label( frame0, image= imgS2, height = 100, width = 150)
    S2.grid(row=3, column=4)
    E2.grid()
    
    S3 = Label( frame0, image= imgS3, height = 100, width = 150)
    S3.grid(row=6, column=10)
    E3.grid()
    
    S4 = Label( frame0, image= imgS4, height = 100, width = 150)
    S4.grid(row=8, column=4)
    E4.grid()
    
    S5 = Label( frame0, image= imgS5, height = 100, width = 150)
    S5.grid(row=10, column=10)
    E5.grid()
    
    Sub = Button( frame0, text='SUBMIT' , command = checkC )
    Sub.grid(row=14, column =6)
    
    
    


def animals():
    b1.grid_forget()
    b2.grid_forget()
    b3.grid_forget()
    l1.grid_forget()
    l2.grid_forget()
    l3.grid_forget()
    
    A1 = Label( frame0, image= imgA1, height = 100, width = 150)
    A1.grid(row=0, column=10)
    E1.grid()
    
    
    A2 = Label( frame0, image= imgA2, height = 100, width = 150)
    A2.grid(row=3, column=4)
    E2.grid()
    
    A3 = Label( frame0, image= imgA3, height = 100, width = 150)
    A3.grid(row=6, column=10)
    E3.grid()
    
    A4 = Label( frame0, image= imgA4, height = 100, width = 150)
    A4.grid(row=8, column=4)
    E4.grid()
    
    A5 = Label( frame0, image= imgA5, height = 100, width = 150)
    A5.grid(row=10, column=10)
    E5.grid()
    
    Sub = Button( frame0, text='SUBMIT' , command = checkC )
    Sub.grid(row=14, column =6)
    
    
  

    
img = PhotoImage(file='Welcome_700x500.png')
imgC = PhotoImage(file='Rainbow_200x100.png')
imgS = PhotoImage(file='shapes_200x100.png')
imgA = PhotoImage( file='animals_200x100.png')

imgWIN = PhotoImage(file="winner_250x200.png")
imgLOSE = PhotoImage(file="lose_250x200.png")
imgC1 = PhotoImage(file='red.png')
imgC2 = PhotoImage(file='green.png')
imgC3 = PhotoImage(file='blue.png')
imgC4 = PhotoImage(file='black.png')
imgC5 = PhotoImage(file='orange.png')

imgA1 = PhotoImage(file='lion_150x100.png')
imgA2 = PhotoImage(file='rabbit_150x100.png')
imgA3 = PhotoImage(file='monke_150x100.png')
imgA4 = PhotoImage(file='chicken_150x100.png')
imgA5 = PhotoImage(file='sheep_150x100.png')

imgS1 = PhotoImage(file='star_150x100.png')
imgS2 = PhotoImage(file='circle_150x100.png')
imgS3 = PhotoImage(file='triangle_150x100.png')
imgS4 = PhotoImage(file='rectangle_150x100.png')
imgS5 = PhotoImage(file='pentagon_150x100.png')

l0 = Label( frame0, image = img)
play = Button( frame0, text = 'PLAY', command = menu )
l1 = Label( frame0, image = imgC,  height=100, width = 150)
l2 = Label( frame0, image = imgS,  height=100, width = 150)
l3 = Label( frame0, image = imgA,  height=100, width = 150) 

b1 = Button( frame0, text='Colors', command = colors, height=8, width = 15)
b2 = Button( frame0, text='Shapes', command = shapes, height=8, width = 15)
b3 = Button( frame0, text='Animals', command = animals, height=8, width = 15)


E1 = Entry( frame0, bd=5)
E1.grid(row=0, column =6 )
E1.grid_remove()

E2 = Entry( frame0, bd=5)
E2.grid(row=3, column =6 )
E2.grid_remove()

E3 = Entry( frame0, bd=5)
E3.grid(row=6, column =6 )
E3.grid_remove()

E4 = Entry( frame0, bd=5)
E4.grid(row=8, column =6 )
E4.grid_remove()

E5 = Entry( frame0, bd=5)
E5.grid(row=10, column =6 )
E5.grid_remove()

b1.grid(row=0, column =7)
b2.grid(row=1, column =7)
b3.grid(row=2, column =7)
b1.grid_forget()
b2.grid_forget()
b3.grid_forget()        
l0.grid()
play.grid()
frame0.grid()
root.mainloop()
