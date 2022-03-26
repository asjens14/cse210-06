import random
from constants import *


class CreateMap:

    def __init__(self):
        self.rooms = ROOMS
        
        
    def choose_random_room(self):
        room = random.choice(self.rooms)
        
        
        
        return room