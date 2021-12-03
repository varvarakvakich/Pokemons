from animal import Animal

class Pokemon(Animal):
    def __init__(self, name, damage, color, sex, age, skills, master):
        super().__init__(name, damage, color, sex, age)
        self.skills = skills
        self.master = master

    def evolution(self):
        print(f'{self.name} эволюционировал и у него улучшились статы посмотрите на них!!')
        self.damage += 1
        self.age += 1
        self.info()

    def info(self):
        super().info()
        print(f' >{len(self.skills)}')

    def study(self, ability):
        print(f'{self.name} приобрел навык {ability.name}')
        self.skills.append(ability)


class WaterPokemon(Pokemon):
    def __init__(self, name, damage, color, sex, age, skills, master):
        super().__init__(name, damage, color, sex, age, skills, master)


class FaltPokemon(Pokemon):
    def __init__(self, name, damage, color, sex, age, skills, master):
        super().__init__(name, damage, color, sex, age, skills, master)


class FirePokemon(Pokemon):
    def __init__(self, name, damage, color, sex, age, skills, master):
        super().__init__(name, damage, color, sex, age, skills, master)
