from cProfile import label
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import random
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
import string, random
import secrets
import uuid
import time


# this is a function to get the selected list box value
def getListboxValue():
	itemSelected = listPassword.curselection()
	return itemSelected

# this is the function called when the button is clicked
def generierenFunktion():
    selection = listPassword.curselection()
    if selection == (0,):
        alphabet = string.digits
        pie = ''.join(secrets.choice(alphabet) for i in range(int(spinBox.get())))
        for i in range(1):
            root.update_idletasks()
            pb1['value'] += 100
            time.sleep(0.4)
        Label(root, text = pie, bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=100, y=218)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{pie}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
        Button(root, text='Speichern', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=20, y=252)

    if selection == (1,):
        alphabet = string.ascii_letters
        password = ''.join(secrets.choice(alphabet) for i in range(int(spinBox.get())))
        for i in range(1):
            root.update_idletasks()
            pb1['value'] += 100
            time.sleep(0.4)
        Label(root, text = password, bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=100, y=218)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{password}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
        Button(root, text='Speichern', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=20, y=252)

    if selection == (2,):
        alphabet = string.ascii_letters + string.digits
        passwordMixed = ''.join(secrets.choice(alphabet) for i in range(int(spinBox.get())))
        for i in range(1):
            root.update_idletasks()
            pb1['value'] += 100
            time.sleep(0.4)
        Label(root, text = passwordMixed, bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=100, y=218)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{passwordMixed}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
        Button(root, text='Speichern', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=20, y=252)

    if selection == (3,):
        alphabet = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        passwordMixedS = ''.join(secrets.choice(alphabet) for i in range(int(spinBox.get())))
        for i in range(1):
            root.update_idletasks()
            pb1['value'] += 100
            time.sleep(0.4)
        Label(root, text = passwordMixedS, bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=100, y=218)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{passwordMixedS}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
        Button(root, text='Speichern', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=20, y=252)

    if selection == (4,):
        zeichenkette = uuid.uuid4()
        for i in range(1):
            root.update_idletasks()
            pb1['value'] += 100
            time.sleep(0.4)
        Label(root, text = zeichenkette, bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=100, y=218)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{zeichenkette}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
        Button(root, text='Speichern', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=20, y=252)



# This is a function which increases the progress bar value by the given increment amount
def makeProgress():
	pb1['value']=pb1['value'] + 1
	root.update_idletasks()


def getSelectedSpinBoxValue():
	return spinBox.get()



root = Tk()

# This is the section of code which creates a spin box
spinBox= Spinbox(root, from_=1, to=50, font=('arial', 12, 'normal'), bg = '#F0F8FF', width=10)
spinBox.place(x=150, y=130)

#Creates a Label for the Spinbox
Label(root, text='Passwortlänge: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=17, y=130)

# This is the section of code which creates the main window
root.geometry('700x390')
root.configure(background='#F0F8FF')
root.title('PW-Generator')


# This is the section of code which creates a listbox
listPassword=Listbox(root, bg='#F0F8FF', font=('arial', 12, 'normal'), width=0, height=0)
listPassword.insert(1, 'Zahlenpasswort')
listPassword.insert(2, 'Buchstabenpasswort')
listPassword.insert(3, 'Zahlen- und Buchstabenpasswort')
listPassword.insert(4, 'Zahlen- und Buchstabenpasswort inkl. Sonderzeichen')
listPassword.insert(5, 'Zufällige Zeichenkette')
listPassword.place(x=18, y=16)



# This is the section of code which creates the a label
Label(root, text='PW-Generator', bg='#F0F8FF', font=('arial', 15, 'normal')).place(x=486, y=19)


# This is the section of code which creates a button
generierenButton = Button(root, text='Generieren', bg='#F0F8FF', font=('arial', 12, 'normal'), command=generierenFunktion).place(x=298, y=167)


# This is the section of code which creates the a label
Label(root, text='Passwort: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=17, y=219)



# This is the section of code which creates a color style to be used with the progress bar
progessBarGen_style = ttk.Style()
progessBarGen_style.theme_use('clam')
progessBarGen_style.configure('progessBarGen.Horizontal.TProgressbar', foreground='#F0F8FF', background='#F0F8FF')


# This is the section of code which creates a progress bar
pb1=ttk.Progressbar(root, style='progessBarGen.Horizontal.TProgressbar', orient='horizontal', length=260, mode='determinate', maximum=100, value=1)
pb1.place(x=19, y=180)


# This is the section of code which creates the a label
Label(root, text='PW-Generator is created by zlElo', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=438, y=58)


# This is the section of code which creates the a label
Label(root, text='GitHub: github.com/zlElo', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=467, y=84)

root.mainloop()
