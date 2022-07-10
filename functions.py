from tkinter import Entry, PhotoImage, StringVar, Toplevel, messagebox
import bcrypt
import json
import re
import string
import random


salt = b'$2b$10$De948JaGOK000Rth4xSztO'
def addUser(data, password, email, window):
    if emailVerifier(email):
        data["email"] = email
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, salt)
        hashed = hashed.decode("utf-8")
        data["password"] = hashed
        with open("data.json", "w") as f:
            json.dump(data, f)
        window.destroy()
    else:
        messagebox.showerror("Invalid email", "Please enter a valid email")

def checkUser(data, password, email, window):
    print(email == data["email"])
    if email == data["email"]:
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, salt)
        a = data["password"].encode('utf-8')
        if hashed==a:
            print("authenticated")
            window.destroy()
            return True
        else:
            return False

def showpass(window,store,a):
    lWindow = Toplevel(window)
    lWindow.title("Login - password manager")
    lWindow.geometry("400x150")
    lWindow.resizable(False, False)
    photoL = PhotoImage(file=".//assets//icons1.png")
    lWindow.iconphoto(False, photoL)
    a = StringVar(value=store["password"][a])
    Entry(lWindow, textvariable=a).pack()
    lWindow.mainloop()

def emailVerifier(email):
    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    result = re.match(pattern,email)
    if(result):
        return True
    else:
        return False

def passwordStrength(password):
    p=1
    if (len(password)>=8):
        p+=1
    pattern_1='[A-Z]+'
    result_1=re.match(pattern_1,password)
    if(result_1):
        p+=1
    pattern_2='[a-z]+'
    result_2=re.match(pattern_2,password)
    if(result_2):
        p+=1
    pattern_3='[0-9]+'
    result_3=re.match(pattern_3,password)
    if(result_3):
        p+=1
    pattern_4= '[\(?=.*[!|@|#|?]\$\)]+'
    result_4=re.match(pattern_4,password)
    if(result_4):
        p+=1
    return p

def generatePassword() :
    s1 = string.ascii_lowercase
    #print (s1)
    s2 = string.ascii_uppercase
    #print (s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
   #print(S4) 
    plen = 10
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #print(s)
    random.shuffle(s)
    #return (s)
    return ''.join(s[0:plen])