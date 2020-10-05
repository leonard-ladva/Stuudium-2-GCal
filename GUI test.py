# importing tkinter
from tkinter import *

# initializing root
root = Tk()

# setting geometry
root.geometry("400x300")


# defining function to print username and password on call
def showinfo():
    print("User Name is", user_name.get())
    print("Password is", password.get())


# defining function to clear entry widgets using .set() method
def clear():
    user_name.set("")
    password.set("")

user_name = StringVar()  # User name variable
password = StringVar()  # Password variable

# creating an entry widget to take username
user_name_Entry = Entry(root, textvariable=user_name).pack(pady=3)
# creating an entry widget to take userpassword
passEntry = Entry(root, textvariable=password, show='*').pack(pady=3)

# creating a button to call "showinfo" function which will print
# username and password in console
Button(root, text='Show Info', command=showinfo).pack(pady=3)

# creating a button to call "clear" function which will clear the entry 
# widgets value of username and userpassword 
Button(root, text='Clear Info', command=clear).pack(pady=3)

# .mainloop() is used when our program is ready to run
root.mainloop()
