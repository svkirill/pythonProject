import sys

users = []
currentUser = None

def find_user_by_login(login):
    for user in users:
        if user["login"] == login:
            return user
    return None

def register_user(login, password):
    foundUser = find_user_by_login(login)

    if foundUser == None:
        user = {"login": login, "password": password}
        users.append(user)
        return user

    return None


def find_user(login, password):
    for user in users:
        if user["login"] == login and user['password'] == password:
            return user
    return None

def login_user(inputLogin, inputPassword):
    user = find_user(inputLogin, inputPassword)
    return user

def view_user_info(user):
    if user != None:
        print("Информация о текущем пользователе:")
        for k,v in user.items():
            print(f"{k}: {v}")

def logout_user():
    global currentUser
    currentUser = None

    print('Вы вышли из системы')

def register_or_login(cmd):
    global currentUser

    if currentUser == None:
        if cmd == "/register":
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            password2 = input("Введите пароль еще раз: ")

            if (password == password2):
                currentUser = register_user(login, password)

                if currentUser == None:
                    print("Ошибка при регистрации.")
            else:
                print("Пароли не совпадают.")
        elif cmd == "/login":
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            currentUser = login_user(login, password)

            if currentUser == None:
                print("Такого пользователя не существует.")

        if currentUser != None:
            print(f"Добро пожаловать, {currentUser['login']}")
    else:
        print("Вы должны выйти из системы.")


def start():
    while True:
        cmd = input(">> ")

        if cmd == "/q":
            sys.exit()
        elif cmd == "/userinfo":
            view_user_info(currentUser)
        elif cmd == "/logout":
            logout_user()
        else:
            register_or_login(cmd)


if __name__ == "__main__":
    start()