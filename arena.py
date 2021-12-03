from random import randint as rand

class Arena:

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.run_up_flag = False
        self.points_for_team1 = {}
        self.points_for_team2 = {}
        self.summary_damage1 = 0
        self.summary_damage2 = 0

    def battle(self, master1, master2, team1, team2, points_for_team1, points_for_team2, flag, summary_damage1,
               summary_damage2):
        if flag:
            input('Битва начинается!\n')
            p1 = master1.pokemons
            p2 = master2.pokemons
            strategy1 = Strategy(master1, master2)
            strategy2 = Strategy(master2, master1)
            for i in range(max(len(p1), len(p2))):
                a = self.scramble(team1, team2, i, p1, strategy1, strategy2,
                             points_for_team1, points_for_team2, summary_damage1, summary_damage2)
                if a:
                    summary_damage1, summary_damage2 = a[0], a[1]
                a = self.scramble(team2, team1, i, p2, strategy2, strategy1,
                             points_for_team2, points_for_team1, summary_damage2, summary_damage1)
                if a:
                    summary_damage2, summary_damage1 = a[0], a[1]
            return summary_damage1, summary_damage2
        else:
            print('Команды не готовы к сражению')

    def counts(self, master):
        count_live, count_death = 0, 0
        for pokemon in master.pokemons:
            if pokemon.health > 15:
                count_live += 1
            if pokemon.health <= 0:
                count_death += 1
                print(pokemon.name)
        return count_live, count_death

    def scramble(self, team1, team2, i, p1, strategy1, strategy2, points_for_team1, points_for_team2, summary_damage1,
                 summary_damage2):
        try:
            if p1[i].health > 15:
                for victim in strategy1.pokemon_victims[p1[i].name]:
                    if victim.name in strategy2.pokemon_victims and p1[i] in strategy2.pokemon_victims[victim.name]:
                        input(f'Начинается схватка между {p1[i].name} и {victim.name}\n')
                        duration1 = strategy1.pokemon_skill[p1[i].name].duration
                        duration2 = strategy2.pokemon_skill[victim.name].duration
                        damage1 = self.hit(strategy1.pokemon_skill[p1[i].name], victim, p1[i])
                        damage2 = self.hit(strategy2.pokemon_skill[victim.name], p1[i], victim)
                        if duration2 > duration1:
                            self.hill(duration2, duration1, victim, p1[i], points_for_team1, team1)
                        if duration1 > duration2:
                            self.hill(duration1, duration2, p1[i], victim, points_for_team2, team2)
                        if p1[i] in strategy2.pokemon_victims[victim.name]:
                            strategy2.pokemon_victims[victim.name].pop(
                                strategy2.pokemon_victims[victim.name].index(p1[i]))
                        summary_damage1 += damage1
                        summary_damage2 += damage2
                    else:
                        summary_damage1 += self.hit(strategy1.pokemon_skill[p1[i].name], victim, p1[i])
                    return [summary_damage1, summary_damage2]
        except:
            pass

    def hit(self, skill, pokemon, attacker):
        damage = skill.check_damage(pokemon.__class__.__name__)
        procent = attacker.damage
        for i in range(int(damage // 2)):
            r = rand(1, 100)
            if r <= procent:
                break
            else:
                damage -= 2
                procent += 1
        pokemon.health -= damage
        input(f'{attacker.name} бьет {pokemon.name} и наносит ему {damage} повреждений\n')
        return damage

    def hill(self, duration2, duration1, victim, p, points_for_team, team):
        d = min(duration2 // duration1 - 1, points_for_team[p.name])
        if d > 0:
            input(f'Во время атаки {victim.name} у {p.name} осталось время полечиться {d} раз\n')
        doctor = team.choose_doctor()
        for _ in range(d):
            doctor.hill(p)

    def start(self, points=0):
        print(f'Добро пожаловать на арену типа {self.__class__.__name__} щя буит месилово')
        print(f'Команды готоваятся к сражению...')
        self.master1 = self.team1.choose_master()
        self.master2 = self.team2.choose_master()
        print(f'Намечается битва между {self.master1.name} из команды {self.team1.name} и {self.master2. name} из команды {self.team2.name}!')
        f = 1
        for i in self.master1.pokemons:
            if i.health < 15:
                f = 0
            self.points_for_team1[i.name] = points
        for i in self.master2.pokemons:
            if i.health < 15:
                f = 0
            self.points_for_team2[i.name] = points
        if f and len(self.master1.pokemons) and len(self.master2.pokemons):
            self.run_up_flag = True

        else:
            print('Боя не будет, не все покемоны в командах здоровы или вообще существуют')

    def mesivo(self):
        if self.run_up_flag:
            self.summary_damage1, self.summary_damage2 = self.battle(self.master1, self.master2, self.team1, self.team2,
                self.points_for_team1, self.points_for_team2,
                self.run_up_flag,
                self.summary_damage1, self.summary_damage2)
        else:
            print('Команды не готовы')

    def end(self):
        if not self.run_up_flag:
            print('че бля')
            return
        print(self.summary_damage1, self.summary_damage2)
        print('Битва окончена')
        print(f'Команда {self.team1.name} в сумме нанесла команде {self.team2.name} {self.summary_damage1} очков урона')
        print(f'Команда {self.team2.name} в сумме нанесла команде {self.team1.name} {self.summary_damage2} очков урона')
        self.master1.pokemons = [i for i in self.master1.pokemons if i.health > 0]
        self.master2.pokemons = [i for i in self.master2.pokemons if i.health > 0]
        result = (max(self.summary_damage1, self.summary_damage2)-min(self.summary_damage1, self.summary_damage2))/10
        if self.summary_damage1 > self.summary_damage2:
            print(f'Побеждает команда {self.team1.name}')
            print(f'Мастеру {self.master1.name} присуждается {result} очков опыта')
            self.master1.score_bust(result)
        elif self.summary_damage1 < self.summary_damage2:
            print(f'Побеждает команда {self.team1.name}')
            print(f'Мастеру {self.master2.name} присуждается {result} очков опыта')
            self.master2.score_bust(result)
        else:
            print(f'Поебедила дружба')


class WaterArena(Arena):
    def __init__(self, team1, team2):
        super().__init__(team1, team2)

    def bonus(self, gift):
        if self.run_up_flag:
            r = ''.join(list(self.__class__.__name__.split('Arena')))
            print(f'Организаторы дарят бонус всем покемонам типа {r}, их point увеличивается на {gift}')
            for i in self.points_for_team1:
                self.points_for_team1[i] += gift
            for i in self.points_for_team1:
                self.points_for_team1[i] += gift
        else:
            print(f'Сорян, никаких бонусов, команды не готовы к битве')


class Strategy():
    def __init__(self, master1, master2):
        self.pokemon_skill, self.pokemon_victims = self.strategy(master1, master2)
    def strategy(self, master1, master2):
        pokemon_skill = {}
        pokemon_victims = {}
        p1 = master1.pokemons
        p2 = master2.pokemons
        for pokemon in p1:
            pokemon_skill[pokemon.name], pokemon_victims[pokemon.name] = self.choose_skill(pokemon, p2)
        return pokemon_skill, pokemon_victims
    def choose_skill(self, pokemon, victims):
        max_damage = 0
        for ability in pokemon.skills:
            damage_, victims_ = self.summary_damage(ability, victims)
            if damage_ > max_damage:
                max_skill = ability
                max_damage = damage_
                max_victims = victims_
        # print(max_damage)
        return max_skill, max_victims
    def summary_damage(self, ability, victims):
        damages = {}
        for pokemon in victims:
            damage = ability.check_damage(pokemon.__class__.__name__)
            try:
                damages[damage].append(pokemon)
            except:
                damages[damage] = [pokemon]
        damages_ = sorted(damages)[::-1]
        sum_damage = 0
        sum_victims = []
        count = ability.goals
        for i in damages_:
            for j in damages[i]:
                if count == 0:
                    break
                else:
                    sum_damage += i
                    sum_victims.append(j)
                    count -= 1
        return sum_damage, sum_victims
