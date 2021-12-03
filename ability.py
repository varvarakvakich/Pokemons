
class Ability():

    def __init__(self, name, damage, duration, goals, rules):
        self.name = name
        self.damage = damage
        self.duration = duration
        self.goals = goals
        self.rules = rules

    def use(self, pokemon1, pokemon2):
        print(f'{pokemon1.name} использовал {self.name} против {pokemon2.name}')
        pokemon2.health-=self.damage
        print(f'здоровье {pokemon2.name} уменьшилось на {self.damage}')

    def check_damage(self, pokemon):
        if pokemon in self.rules:
            return self.damage * self.rules[pokemon]
        else:
            return self.damage


class WaterAbility(Ability):
    def __init__(self, name, damage, duration, goals, rules):
        super().__init__(name, damage, duration, goals, rules)


class FireAbility(Ability):
    def __init__(self, name, damage, duration, goals, rules):
        super().__init__(name, damage, duration, goals, rules)
