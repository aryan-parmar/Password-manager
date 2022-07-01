from tkinter import BOTTOM, LEFT, RIGHT, X, Y, Button, Canvas, Entry, Frame, PhotoImage, Scrollbar, StringVar, Tk, Label, Toplevel, ttk
import json
import bcrypt
from functions import addUser, checkUser, showpas


def signup():
    window = Tk()
    window.title("Signup - password manager")
    window.geometry("400x150")
    window.resizable(False, False)
    photo = PhotoImage(file=".//assets//icons1.png")
    window.iconphoto(False, photo)

    Label(window, text="Welcome to password manager", font="12").pack()

    Label(window, text="Email").place(x=100, y=50)
    email = StringVar()
    inputtxt = Entry(window, width=20, textvariable=email)
    inputtxt.place(x=160, y=50)

    Label(window, text="Password").place(x=100, y=90)
    password = StringVar()
    inputp = Entry(window, width=20, show="*", textvariable=password)
    inputp.place(x=160, y=90)

    Button(window, text="Signup", command=lambda: addUser(
        data, password.get(), email.get(), window)).place(x=170, y=115)
    window.mainloop()


def login(ind):
    window = Tk()
    window.title("Login - password manager")
    window.geometry("400x150")
    window.resizable(False, False)
    photo = PhotoImage(file=".//assets//icons1.png")
    window.iconphoto(False, photo)

    Label(window, text="Login to view password", font="12").pack()

    Label(window, text="Email").place(x=100, y=50)
    email = StringVar()
    inputtxt = Entry(window, width=20, textvariable=email)
    inputtxt.place(x=160, y=50)

    Label(window, text="Password").place(x=100, y=90)
    password = StringVar()
    inputp = Entry(window, width=20, show="*", textvariable=password)
    inputp.place(x=160, y=90)

    Button(window, text="Login", command=lambda: showpass(store,a) if checkUser(
        data, email.get(), password.get(), window) else None ).place(x=170, y=115)

    window.mainloop()

def addPassword(store, password, app, window):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    hashed = hashed.decode("utf-8")
    store["password"].append(hashed)
    store["app"].append(app)
    with open("store.json", "w") as f:
        json.dump(store, f)
    window.destroy()
    main_window()

def addNewPasswordWindow(window):
    window.destroy()
    win = Tk()
    win.title("add password - password manager")
    win.geometry("400x150")
    win.resizable(False, False)

    Label(win, text="Add new password", font="12").pack()

    Label(win, text="App name").place(x=100, y=50)
    app = StringVar()
    inptxt = Entry(win, width=20, textvariable=app)
    inptxt.place(x=160, y=50)

    Label(win, text="Password").place(x=100, y=90)
    passwordA = StringVar()
    inpp = Entry(win, width=20, show="*", textvariable=passwordA)
    inpp.place(x=160, y=90)

    ttk.Button(win, text="Add", command=lambda: addPassword(
        store, passwordA.get(), app.get(), win)).place(x=170, y=115)
    win.mainloop()


def main_window():
    window = Tk()
    window.title("password manager")
    window.geometry("800x600")
    window.resizable(False, False)
    photo = PhotoImage(file=".//assets//icons1.png")
    window.iconphoto(False, photo)

    Label(window, text="Welcome to password manager",
          font="12").place(x=10, y=10)
    ttk.Button(window, text="Add new password",
               command=lambda: addNewPasswordWindow(window)).place(x=680, y=10)

    passwordList = store["password"]

    frame_container = Frame(window, width=800, height=500)
    canvas_container = Canvas(frame_container, height=500)
    canvas_container.bind_all('<MouseWheel>', lambda event: canvas_container.yview_scroll(
        int(-1*(event.delta/120)), "units"))
    frame2 = Frame(canvas_container, width=800, height=500)
    myscrollbar = Scrollbar(
        frame_container, orient="vertical", command=canvas_container.yview)
    canvas_container.create_window((0, 0), window=frame2, anchor='nw')

    edit = PhotoImage(file=".//assets//edit.png")
    delete = PhotoImage(file=".//assets//delete.png")
    eye = PhotoImage(file=".//assets//view.png")

    for i in range(len(passwordList)):
        ind = Label(frame2, text=str(i+1))
        ind.grid(row=i, column=3)
        app = Label(frame2, text=store["app"][i])
        app.grid(row=i, column=10)
        text = StringVar(value=passwordList[i])
        password = Entry(frame2, textvariable=text, show="*")
        password.grid(row=i, column=11)
        show = ttk.Button(frame2, image=eye, command=lambda a = i: login(a))
        show.grid(row=i, column=15)
        deleteB = ttk.Button(frame2, image=delete)
        deleteB.grid(row=i, column=17)
        editB = ttk.Button(frame2, image=edit)
        editB.grid(row=i, column=18)

    frame2.update()
    canvas_container.configure(
        yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height())
    canvas_container.pack(side=LEFT, fill=X, expand=True)
    myscrollbar.pack(side=RIGHT, fill=Y)
    frame_container.pack(side=BOTTOM, fill=X, expand=True)

    window.mainloop()



try:
    with open("data.json", "r") as f:
        data = json.load(f)
except:
    data = {}
    with open("data.json", "w") as f:
        json.dump(data, f)
try:
    with open("store.json", "r") as f:
        store = json.load(f)
except:
    store = {"app":[],"password":[]}
    with open("store.json", "w") as f:
        json.dump(store, f)
if len(data) == 0:
    signup()
else:
    main_window()
