from classes.soldier import Soldier

# 10 rooms
class House:
    def __init__(self):
       self.rooms = []

    def add_room(self):
        self.rooms.append()
        
#8 soldier
class Room:
    def __init__(self):
        self.soldier = []
    
    def add_soldier(self,solider: Soldier):
        self.soldier.append(solider)

h1 =House()
h2 = House()

room = Room()
room.add_soldier(Soldier)