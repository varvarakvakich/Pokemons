import random


class Team():
    def __init__(self, name, masters=[], doctors=[], spectators=[]):
        self.name = name
        self.masters = masters
        self.doctors = doctors
        self.spectators = spectators

    def choose_master(self):
        return self.masters[random.randint(0, len(self.masters)-1)]

    def choose_doctor(self):
        return self.doctors[random.randint(0, len(self.doctors)-1)]

    def add(self, human):
        if human.__class__.__name__ == 'Master':
            self.masters.append(human)
        if human.__class__.__name__ == 'Doctor':
            self.doctors.append(human)
        if human.__class__.__name__ == 'Spectator':
            self.spectators.append(human)

