import random
import string

def generate_registration_data():
    name_lenght = random.randint(5, 7)
    name = ''.join(random.choices(string.ascii_lowercase, p=name_lenght) + random.choices(string.digits, p=3))

    email_length = random.randint(5, 7)
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length)) + '@gmail.com'
    
    password_length = random.randint(6, 8)
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=password_length))
    return name, email, password  # Возвращаем кортеж (name, email, password)
