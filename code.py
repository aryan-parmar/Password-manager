import json
from tkinter import Button, Entry, PhotoImage, StringVar, Tk, Label

def addUser(password, email, window):
    data["email"] = email
    data["password"] = password
    with open("code.json", "w") as f:
        json.dump(data, f)
    window.destroy()

def signup():
    window = Tk()
    window.title("Signup - password manager")
    window.geometry("400x150")
    window.resizable(False, False)
    photo = PhotoImage(file=".//assets//icons1.png")
    window.iconphoto(False, photo)
    
    Label(window, text="Welcome to password manager", font="12").pack()
    
    Label(window,text="Email").place(x=100,y=50)
    email = StringVar()
    inputtxt = Entry(window, width = 20, textvariable = email)
    inputtxt.place(x=160,y=50)

    Label(window,text="Password").place(x=100,y=90)
    password = StringVar()
    inputp = Entry(window, width = 20, show="*", textvariable=password)
    inputp.place(x=160,y=90)

    Button(window, text="Signup", command=lambda: addUser(
        password.get(), email.get(), window)).place(x=170, y=115)
    window.mainloop()
try:
    with open("code.json", "r") as f:
        data = json.load(f)
except:
    data = {}
    with open("code.json", "w") as f:
        json.dump(data, f)
if len(data) == 0:
    signup()
