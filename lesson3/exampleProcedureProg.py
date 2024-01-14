'''def login():
    print("Success!")
def logout():
    print("Logout.")
def handle_cmd(cmd):
    if cmd == "/login":
        login()
    elif cmd == "/logout":
        logout()
def start():
    while True:
        cmd = input(">> ")

        if cmd == "/q":
            break
        else:
            handle_cmd(cmd)

print(__name__)
if __name__ == "__main__":'''

