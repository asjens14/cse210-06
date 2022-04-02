from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.player import Player
from game.casting.ball import Ball 
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image

import random
class Enemy(Player):
    def __init__(self, body, animation, type, debug=False):
        super().__init__(body, animation, debug)
        if type == 'a':
            self.swing_right()
        if type == 'b':
            self.swing_down()
        self._type = type
        self._lives = ENEMY_LIVES
        # self._video_service = video_service
    def bounce(self):
        if self._type == 'a':
            self.bounce_x()
        elif self._type == 'b':
            self.bounce_y()
    
    def bounce_x(self):
        if self._body.get_velocity().equals(Point(-PLAYER_VELOCITY, 0)):
                self.swing_right()
        else:
            self.swing_left()

    def bounce_y(self):
        if self._body.get_velocity().equals(Point(0, -PLAYER_VELOCITY)):
                self.swing_down()
        else:
            self.swing_up()

    def spawn_ball(self, cast, video_service):
        player = self.get_body().get_position()
        player_x = player.get_x()
        player_y = player.get_y()
        direction = random.choice(['l','r','u','d'])
        if direction == 'l': 
            position = Point(player_x - ENEMY_WIDTH, player_y)
            velocity = Point(-BALL_VELOCITY, 0)
        elif direction == 'r': 
            position = Point(player_x+ENEMY_WIDTH, player_y)
            velocity = Point(BALL_VELOCITY, 0)
        elif direction == 'u': 
            position = Point(player_x, player_y-ENEMY_HEIGHT)
            velocity = Point(0, -BALL_VELOCITY)
        elif direction == 'd': 
            position = Point(player_x, player_y+ENEMY_HEIGHT)
            velocity = Point(0, BALL_VELOCITY)
        
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)
        video_service.draw_image(image, position)
        # ball.release()
