from cProfile import label
from logging import root
from tkinter import * 
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
import string
import secrets
import uuid
import customtkinter


# this is the function called when the button is clicked
def generierenFunktion():
    selection = comboOneTwoPunch.get()
    if selection == ('Zahlenpasswort'):
        app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        app.title("PW-Generator_Passwort")
        app.geometry("300x180")
        alphabet = string.digits
        pie = ''.join(secrets.choice(alphabet) for i in range(int(tInput.get())))
        customtkinter.CTkLabel(master=app, text = pie, bg='#F0F8FF').place(x=50, y=50)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{pie}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
            app.destroy()
        customtkinter.CTkButton(master=app, text='Speichern', bg='#F0F8FF', command=btnClickFunction).place(x=50, y=80)
        app.mainloop()

    if selection == ('Buchstabenpasswort'):
        app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        app.title("PW-Generator_Passwort")
        app.geometry("300x180")
        alphabet = string.ascii_letters
        password = ''.join(secrets.choice(alphabet) for i in range(int(tInput.get())))
        customtkinter.CTkLabel(master=app, text = password, bg='#F0F8FF').place(x=50, y=50)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{password}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
            app.destroy()
        customtkinter.CTkButton(master=app, text='Speichern', bg='#F0F8FF', command=btnClickFunction).place(x=50, y=80)
        app.mainloop()

    if selection == ('Zahlen-und Buchstabenpasswort'):
        app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        app.title("PW-Generator_Passwort")
        app.geometry("300x180")
        alphabet = string.ascii_letters + string.digits
        passwordMixed = ''.join(secrets.choice(alphabet) for i in range(int(tInput.get())))
        customtkinter.CTkLabel(master=app, text = passwordMixed, bg='#F0F8FF').place(x=50, y=50)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{passwordMixed}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
            app.destroy()
        customtkinter.CTkButton(master=app, text='Speichern', bg='#F0F8FF', command=btnClickFunction).place(x=50, y=80)
        app.mainloop()

    if selection == ('Zahlen- und Buchstabenpasswort inkl. Sonderzeichen'):
        app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        app.title("PW-Generator_Passwort")
        app.geometry("300x180")
        alphabet = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        passwordMixedS = ''.join(secrets.choice(alphabet) for i in range(int(tInput.get())))
        customtkinter.CTkLabel(master=app, text = passwordMixedS, bg='#F0F8FF').place(x=50, y=50)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{passwordMixedS}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
            app.destroy()
        customtkinter.CTkButton(master=app, text='Speichern', bg='#F0F8FF', command=btnClickFunction).place(x=50, y=80)
        app.mainloop()

    if selection == ('Zufällige Zeichenkette'):
        app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        app.title("PW-Generator_Passwort")
        app.geometry("300x180")
        zeichenkette = uuid.uuid4()
        customtkinter.CTkLabel(master=app, text = zeichenkette, bg='#F0F8FF').place(x=50, y=50)
        def btnClickFunction():
            file = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")],
            defaultextension=".txt")
            fob=open(file,'w')
            fob.write(f'{zeichenkette}\n\nCreated with PW-Generator by zlElo\nGithub: https://github.com/zlElo')
            fob.close()
            app.destroy()
        customtkinter.CTkButton(master=app, text='Speichern', bg='#F0F8FF', command=btnClickFunction).place(x=50, y=80)
        app.mainloop()


# this is a function which returns the selected combo box item
def getSelectedComboItem():
	return comboOneTwoPunch.get()



def getSelectedSpinBoxValue():
	return tInput.get()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x170")
app.title("PW-Generator")


# This is the section of code which creates a text input box
tInput=customtkinter.CTkEntry(app)
tInput.place(x=140, y=73)

#Creates a Label for the Spinbox
customtkinter.CTkLabel(master=app, text='Passwortlänge: ', bg='#F0F8FF').place(x=0, y=70)



# This is the section of code which creates a combo box
comboOneTwoPunch= customtkinter.CTkComboBox(master=app, values=['Zahlenpasswort', 'Buchstabenpasswort', 'Zahlen-und Buchstabenpasswort', 'Zahlen- und Buchstabenpasswort inkl. Sonderzeichen', 'Zufällige Zeichenkette'], width=655)
comboOneTwoPunch.place(x=18, y=16)
comboOneTwoPunch.grab_current


# This is the section of code which creates a button
generierenButton = customtkinter.CTkButton(master=app, text='Generieren', command=generierenFunktion).place(x=20, y=120)

# This is the section of code which creates a icon for the window
app.iconbitmap('iconpw.ico')

app.mainloop()