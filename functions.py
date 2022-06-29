import bcrypt
import json
def addUser(data, password, email, window):
    data["email"] = email
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    hashed = hashed.decode("utf-8")
    data["password"] = hashed
    with open("data.json", "w") as f:
        json.dump(data, f)
    window.destroy()
