import string

password = input("ВВедите пароль:")

def check_password(password):
    errors = []
    if len(password) != 8:
        errors.append("Длина пароля не равна 8")
    if password.lower() == password:
        errors.append("В пароле отсутствуют заглавные буквы")
    if password.upper() == password:
        errors.append("В пароле отсутствуют строчные буквы")
    if not any(symbol.isdigit() for symbol in password):
        errors.append("В пароле отсутствуют цифры")
    chars = set('*-#')
    if not any(symbol in chars for symbol in password):
        errors.append("В пароле отсутствуют специальные символы")
    allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
    if not all(symbol in allowed for symbol in password):
        errors.append("В пароле используются непредусмотренные символы")
    if not errors:
        print("Надежный пароль")
    else:
        for error in errors:
            print(error)

check_password(password)

