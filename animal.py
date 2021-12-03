
class Animal():
    def __init__(self, name, damage, color, sex, age, death=False, health=100):
        self.health = health
        self.name = name
        self.damage = damage
        self.color = color
        self.sex = sex
        self.age = age
        self.death = death

#rrrr

    def bit(self, victim):
        print(f'{self.name} кусьнул {victim.name} оче больна///')
        victim.health -= self.damage
        if victim.health <= 0:
            victim.death = True
            print(f'блин..ю {victim.name} умер, зачем {self.name} его кусьнул')

    def bit(self):
        self.health -= 1
        print(f'вы ударили {self.name} зачем вы так сделали...')
        print(f'теперь его здоровье {self.health}')
        if self.health <= 0:
            self.death = True
            print(f'{self.name} umer:(')

    def getting_older(self):
        self.age += 1

    def info(self):
        print(f'Информация об {self.name}:')
        print(f' >Возраст: {self.age}')
        print(f' >Дамаг: {self.damage}')
        print(f' >Пол: {self.sex}')
        print(f' >Здоровье: {self.health}')
        print(f' >Цвет: {self.color}')
        print(f' >type: {self.__class__.__name__}')

