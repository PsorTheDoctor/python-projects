from random import randint
from time import sleep


class User(object):

    def __init__(self, num, email, password):
        self.num = num
        self.email = email
        self.password = password
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.name = self.first_name + ' ' + self.last_name
        self.login = self.first_name.lower() + self.generate_nick()

    def __str__(self):
        return self.login

    @staticmethod
    def generate_first_name():
        girls = ['Lena', 'Jula', 'Zuzia', 'Maja', 'Zosia', 'Amelia', 'Hanka', 'Ola', 'Wika', 'Natalia']
        boys = ['Kuba', 'Kacper', 'Filip', 'Szymek', 'Janek', 'Tony', 'Michal', 'Wojtek', 'Mati', 'Bartek']
        first_name = girls + boys
        sleep(0.1)
        rand = randint(0, len(first_name) - 1)
        return first_name[rand]

    @staticmethod
    def generate_last_name():
        last_name = ['Nowak', 'Wojcik', 'Kowalczyk', 'Wozniak', 'Mazur',
                     'Krawczyk', 'Kaczmarek', 'Zajac', 'Krol', 'Wrobel']
        sleep(0.1)
        rand = randint(0, len(last_name) - 1)
        return last_name[rand]

    @staticmethod
    def generate_nick():
        nick = ['_xxx', '_stunt', 'free', 'x', '_spicy', '69_', '_official', 'pure', 'lover', '18_']
        sleep(0.1)
        rand = randint(0, len(nick) - 1)
        sleep(0.1)
        num = randint(0, 10000)
        return nick[rand] + str(num)

    def save_to_file(self):
        file = open('user_db.txt', 'a')
        file.write('USER ' + str(self.num) + '\n')
        file.write(str(self.email) + '\n')
        file.write(str(self.name) + '\n')
        file.write(str(self.login) + '\n')
        file.write('\n')
