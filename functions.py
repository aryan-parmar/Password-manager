import bcrypt
import json
import re
def addUser(data, password, email, window):
    data["email"] = email
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    hashed = hashed.decode("utf-8")
    data["password"] = hashed
    with open("data.json", "w") as f:
        json.dump(data, f)
    window.destroy()

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
print(passwordStrength("tfSDf$33"))