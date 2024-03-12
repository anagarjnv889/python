DB = {
    'ajay' : 'Ajay@1233',
    'nagar' : 'Nagar@123'
}

def auth(func):
    def wrapper(username, password, *args, **kwargs):
        if username in DB and DB[username] == password:
            func(*args, **kwargs)
        else:
            print("Auth is failed")

@auth
def account(a, b):
    print(a+b)
account("ajay", "Ajay@1233", 5, 10)