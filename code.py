from tkinter import PhotoImage, Tk, Label

def signup():
    window = Tk()
    window.title("Signup - password manager")
    window.geometry("400x150")
    window.resizable(False, False)
    
    Label(window, text="Welcome to password manager", font="12").pack()

    window.mainloop()

signup()