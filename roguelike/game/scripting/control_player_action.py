from constants import *
from game.scripting.action import Action
from game.casting.ball import Ball 
from game.casting.point import Point
from game.casting.body import Body
from game.casting.enemy import Enemy
from game.casting.animation import Animation

class ControlPlayerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._ball = Ball()

    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        if self._keyboard_service.is_key_down(SPACE): 
            # cast.clear_actors(ENEMY_GROUP)
            # stats = cast.get_first_actor(STATS_GROUP)
            # level = stats.get_level() % BASE_LEVELS
            # filename = ENEMY_FILE.format(level)

        

            # x = FIELD_LEFT + ENEMY_WIDTH
            # y = FIELD_TOP + ENEMY_HEIGHT
            
            # # type = column[0]
            # # frames = int(column[1])

            
            # position = Point(x, y)
            # size = Point(ENEMY_WIDTH, ENEMY_HEIGHT)
            # velocity = Point(0, 0)

            # images = ENEMY_IMAGE[0]

            # body = Body(position, size, velocity)
            # animation = Animation(images, ENEMY_RATE)

            # enemy = Enemy(body, animation, type)
            # cast.add_actor(ENEMY_GROUP, enemy)
            print('shoot')


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