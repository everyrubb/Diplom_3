import random
import string

class Helpers:
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


    # метод генерации электронной почты
    def generate_random_email(self, domain="ya.ru", username_prefix="cherenkova_06"):
        random_number = random.randint(0, 9999)
        login = f"{username_prefix}{random_number}"
        email = f"{login}@{domain}"
        return email


    # метод генерации логина, пароля и имени
    def generate_data(self):
        email = self.generate_random_email()
        name = self.generate_random_string(10)
        password = self.generate_random_string(10)
        return email, name, password