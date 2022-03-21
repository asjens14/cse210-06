from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.player import Player

class Enemy(Player):
    def __init__(self, body, animation, debug=False):
        super().__init__(body, animation, debug)