from constants import *
from game.scripting.action import Action
from game.casting.ball import Ball 
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
import time

class ControlPlayerAction(Action):

    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._start = time.time()

    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        elapsed = time.time()-self._start
        if self._keyboard_service.is_key_down(SPACE) and elapsed >= .5: 
            self._spawn_ball(cast, player.get_body().get_position())
            self._start = time.time()

        if self._keyboard_service.is_key_down(LEFT): #or self._keyboard_service.is_key_down(LEFT2): 
            player.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): #or self._keyboard_service.is_key_down(RIGHT2): 
            player.swing_right()
        elif self._keyboard_service.is_key_down(UP): #or self._keyboard_service.is_key_down(UP2): 
            player.swing_up()
        elif self._keyboard_service.is_key_down(DOWN): #or self._keyboard_service.is_key_down(DOWN2): 
            player.swing_down()   
        else: 
            player.stop_moving()

    def _spawn_ball(self, cast, player:Point):
        player_x = player.get_x()
        player_y = player.get_y()
        if self._keyboard_service.is_key_down(LEFT2) or self._keyboard_service.is_key_down(J): 
            position = Point(player_x - PLAYER_WIDTH, player_y)
            velocity = Point(-BALL_VELOCITY, 0)
        elif self._keyboard_service.is_key_down(RIGHT2) or self._keyboard_service.is_key_down(L): 
            position = Point(player_x+PLAYER_WIDTH, player_y)
            velocity = Point(BALL_VELOCITY, 0)
        elif self._keyboard_service.is_key_down(UP2) or self._keyboard_service.is_key_down(I): 
            position = Point(player_x, player_y-PLAYER_HEIGHT)
            velocity = Point(0, -BALL_VELOCITY)
        elif self._keyboard_service.is_key_down(DOWN2) or self._keyboard_service.is_key_down(K): 
            position = Point(player_x, player_y+PLAYER_HEIGHT)
            velocity = Point(0, BALL_VELOCITY)
        else: 
            position = Point(player_x, player_y+PLAYER_HEIGHT)
            velocity = Point(0, 0)
        
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)
        self._video_service.draw_image(image, position)
        # ball.release()
