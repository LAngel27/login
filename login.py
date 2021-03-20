import random

def verifer_password():
    enter_password = input('Inserta tu contraseña: ')
    if len(enter_password) < 4:
        return False
    else:
        return (
            enter_password
        )

def login():
    db = []
    status = False
    name = input('Escriba su nombre: ')
    lastName = input('Escriba su apellido: ')
    email = input('Ingrese su email: ')
    password = verifer_password()


    while not email.count('@') >= 1:
        print('por favor coloque una direccion de correo valida')
        email = input('Ingrese una direccion valida: ')

    if name[0].islower() or name[0].isdigit():
        raise UserWarning('Error')
    else:
        id = random.randint(0,999999)
        status = True
        send = {
            'name': name,
            'last_name': lastName,
            'email': email,
            'id': id,
            'status': status,
            'password': password
        }

        db.append(send)
        
        
    return db

def show_db(fn = login()):
    for i in fn:
        print(i)

        print('Registro exitoso! Welcome {}'.format(i['name']))

        options = """
        Que operacion desea realizar

        1. sign in
        2. logout
        """

        options_selection = input(options)

        if options_selection == '1':
            user_sign_in(fn) 
        else:
            print('Vuelva pronto {}'.format(i['name']))


def user_sign_in(data):
    user_email = input('Username or Email: ')
    user_password = input('Password: ')

    while not data[0]['password'] == user_password not in data[0]['email'] == user_email:
        print('Datos invalidos por favor insertelos de nuevo')
        user_email = input('Username or Email: ')
        user_password = input('Password: ')
    else:
        print('contraseña correcta')

if __name__ == "__main__":
    show_db(),