from animal import Animal
import random

class Human(Animal):
    def __init__(self, name, damage, color, sex, age, intelligence):
        super().__init__(name, damage, color, sex, age)
        self.intelligence = intelligence

    def cheer_up(self):
        print(f'не волнуйся, {self.name}, хор5 - норм оценка')

    def bulling(self):
        print(f'не волнуйся, {self.name}, хор5 - норм оценка))))')


class Doctor(Human):
    def __init__(self, name, damage, color, sex, age, intelligence, skill, cured=0):
        super().__init__(name, damage, color, sex, age, intelligence)
        self.skill = skill
        self.cured = cured
        self.intelligence = intelligence

    def hill(self, pokemon):
        pokemon.health = (pokemon.health + self.skill) // 101
        input(f'Доктор {self.name} лечит {pokemon.name} и дает ему {self.skill} очков здоровья\n')
        self.cured += 1
        self.skill += self.cured // 5  # за каждых 5 вылеченных покемонов увеличивается скилл


class Master(Human):
    def __init__(self, name, damage, color, sex, age, intelligence, score, pokemons):
        super().__init__(name, damage, color, sex, age, intelligence)
        self.score = score
        self.pokemons = pokemons

    def score_bust(self, score):
        print(f'{self.name}: score + {score}')
        self.score += score

    def catch_pokemons(self, pokemons):
        for pokemon in pokemons:
            print(f'>{self.name} пытается поймать {pokemon.name}....')
            procent = random.randint(0, 100)
            if pokemon not in self.pokemons:
                if procent <= self.score:
                    print(f'>и ловит его!')
                    if pokemon.master:
                        print(f'Он забрал его у {pokemon.master.name}...')
                        for i in range(len(pokemon.master.pokemons)):
                            if pokemon.master.pokemons == pokemon:
                                pokemon.master.pokemons = pokemon.master.pokemons[:i]+pokemon.master.pokemons[i+1:]
                    self.pokemons.append(pokemon)
                    pokemon.master = self
                else:
                    print(f'... и ему не удается')
                    self.score += 0.5 #чел не ловит, но набирается опыта!!
            else:
                print(f'и ловит своего {pokemon.name}, чтобы потискать')


class Spectator():
    def __init__(self, name, damage, color, sex, age, intelligence, volume=10):
        super().__init__(name, damage, color, sex, age, intelligence)
        self.volume = volume

