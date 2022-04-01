from constants import *
from game.scripting.action import Action
from game.casting.ball import Ball 
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image

class ControlPlayerAction(Action):

    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        if self._keyboard_service.is_key_down(SPACE): 
            self._spawn_ball(cast, player.get_body().get_position())
        if self._keyboard_service.is_key_down(LEFT) or self._keyboard_service.is_key_down(LEFT2): 
            player.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT) or self._keyboard_service.is_key_down(RIGHT2): 
            player.swing_right()
        elif self._keyboard_service.is_key_down(UP) or self._keyboard_service.is_key_down(UP2): 
            player.swing_up()
        elif self._keyboard_service.is_key_down(DOWN) or self._keyboard_service.is_key_down(DOWN2): 
            player.swing_down()   
        else: 
            player.stop_moving()

    def _spawn_ball(self, cast, player:Point):
        # cast.clear_actors(BALL_GROUP)
        x = CENTER_X - BALL_WIDTH / 2
        y = CENTER_Y - BALL_HEIGHT / 2
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)
        self._video_service.draw_image(image, position)
