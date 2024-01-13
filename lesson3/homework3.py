users = []
currentUser = None
def register_user(login, password):
    user = {"login": login, "password": password}
    users.append(user)
    return user

login = input("Введите логин: ")
password = input("Введите пароль: ")
password2 = input("Введите пароль еще раз: ")

if (password == password2):
    currentUser = register_user(login, password)
else:
    print("Пароли не совпадают.")

if currentUser != None:
    print(f"Добро пожаловать, {currentUser['login']}")

def login_user():
    loginuser = input('Введите логин:')
    passworduser = input('Введите пароль:')

    if (loginuser == login) and (passworduser == password):
        print('Вы вошли в систему')
    else:
        print('Введен неверный пароль или логин')


def view_user_info():
    print(users)

def logout_user():
    print('Вы вышли из системы')
    exit()