from tkinter import Entry, PhotoImage, StringVar, Tk, Label

def signup():
    window = Tk()
    window.title("Signup - password manager")
    window.geometry("400x150")
    window.resizable(False, False)
    
    Label(window, text="Welcome to password manager", font="12").pack()
    
    Label(window,text="Email").place(x=100,y=50)
    email = StringVar()
    inputtxt = Entry(window, width = 20, textvariable = email)
    inputtxt.place(x=160,y=50)


    window.mainloop()

signup()