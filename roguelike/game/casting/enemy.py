from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.player import Player

class Enemy(Player):
    def __init__(self, body, animation, debug=False):
        super().__init__(body, animation, debug)
        self.swing_right()
        self._lives = ENEMY_LIVES
    
    def bounce(self):
        if self._body.get_velocity().equals(Point(-PLAYER_VELOCITY, 0)):
            self.swing_right()
        else:
            self.swing_left()

    def gets_hit(self):
        cast.remove_actor(BRICK_GROUP, brick)
