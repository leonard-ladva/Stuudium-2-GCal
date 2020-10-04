from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#def faili():
    


#def googlelogin():


raam = Tk()
raam.title("Log In")
#tahvel = Canvas(raam, height=300, width=300, background="White")
#tahvel.grid()
raam.geometry("400x400")

def show():
    Password_text = password.get()
    print(Password_text)

usernamepilt=Label(raam, text="Username")
usernamepilt.place (x=5, y=50)

passwordpilt=Label(raam, text="Password")
passwordpilt.place(x=5, y=80)

Stulogin=Label(raam, text="Stuudiumi login")
Stulogin.place(x=5, y=5)

Outputpilt=Label(raam, text="Output")
Outputpilt.place(x=5, y=110)

#Username Textbox
user_text=Entry(raam)
user_text.place(x=70, y=50, width=150)

#Password textbox
password = StringVar()
Password_text=Entry(raam, textvariable=password, show="*")
Password_text.place(x=70, y=80, width=150)

show_nupp=Button(raam, text="Show", bg="White", command=show)
show_nupp.place(x=225, y=80, width=70)

#show password button
show_nupp=Button(raam, text="Show", bg="White")
show_nupp.place(x=225, y=80, width=70)

Failinupp=Button(raam, text="File", bg="white")
Failinupp.place(x=70, y=110, width=70)

googlenupp=Button(raam, text="Google Calendar", bg="white")
googlenupp.place(x=150, y=110)


raam.mainloop()