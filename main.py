from human import Human, Doctor, Master
from pokemon import Pokemon, FaltPokemon, WaterPokemon, FirePokemon
from ability import Ability, WaterAbility, FireAbility
from team import Team
from arena import Arena, WaterArena
vjuh1 = WaterAbility('vjuh1', 15, 1, 1, {'FirePokemon': 1.5})
vjuh2 = FireAbility('vjuh2', 16, 4, 1, {'WaterPokemon': 1.5})
vjuh3 = Ability('vjuh3', 15, 1, 1, {})
pika1 = WaterPokemon('Pikachu1', 70, 'yellow', 'male', 10, [vjuh1, vjuh2, vjuh3], '')
pika2 = FirePokemon('Pikachu2', 50, 'yellow', 'male', 10, [vjuh2, vjuh3], '')
pika3 = Pokemon('Pikachu3', 60, 'yellow', 'male', 10, [vjuh2], '')
brbr1 = FirePokemon('brbr1', 10, 'yellow', 'male', 10, [vjuh1, vjuh2, vjuh3], '')
brbr2 = FirePokemon('brbr2', 10, 'yellow', 'male', 10, [vjuh1, vjuh2, vjuh3], '')
brbr3 = Pokemon('brbr3', 10, 'yellow', 'male', 10, [vjuh1, vjuh2, vjuh3], '')

ash1 = Master('Ash1', 50, '...', 'male', 14, 100, 50, [])
ash2 = Master('Ash2', 50, '...', 'male', 14, 100, 100, [])
doc1 = Doctor('Doc1', 50, '...', 'non-binary', 20, 100, 5)
doc2 = Doctor('Doc2', 50, '...', 'female', 20, 100, 5)
ash1.catch_pokemons([pika1, pika2])
ash2.catch_pokemons([brbr1, brbr2, brbr3])
team1, team2 = Team('team1', [ash1], [doc1]), Team('team2', [ash2], [doc2])
ash1.score = 50
ash2.score = 50
ar = WaterArena(team1, team2)
ar.start()
ar.bonus(1)
ar.mesivo()
ar.end()
pika3.info()