from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.scripting.create_map import CreateMap
import time
class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        # self._director = Director
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for brick in bricks:
            player_body = player.get_body()
            brick_body = brick.get_body()
            points = brick.get_points()
            if points == "1":
                if self._physics_service.has_collided(player_body, brick_body):
                    player.bounce()
                    # player.stop_moving()
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    # points = brick.get_points()
                    # stats.add_points(points)
                    # cast.remove_actor(BRICK_GROUP, brick)
            elif points == 'd':
                #send to next room
                if self._physics_service.has_collided(player_body, brick_body):
                    direction = self._find_direction(player_body.get_position())
                    # player_x, player_y = player.get_location()
                    stats = cast.get_first_actor(STATS_GROUP)
                    room = stats.get_level()
                    for r, row in enumerate(ROOMS):
                        for c, column in enumerate(row):
                            if(column == room):
                                player_x=c
                                player_y=r
                    if(direction == "Left"):
                        player_x -= 1
                    elif(direction == "Right"):
                        player_x += 1
                    elif(direction == "Up"):
                        player_y -= 1
                    elif(direction == "Down"):
                        player_y += 1
                    
                    # next_room = CreateMap.choose_random_room()
                    stats.next_level(ROOMS[player_y][player_x])
                    print(ROOMS)
                    print(player_x, player_y, ROOMS[player_y][player_x])
                    # player.set_location(player_x,player_y)
                    callback.on_next(NEXT_LEVEL)
                    break
            
    
    def _find_direction(self, position) -> str:
        if position.get_x() < FIELD_LEFT + 64:
            return "Left"
        elif position.get_x() > FIELD_RIGHT - 64:
            return "Right"
        elif position.get_y() < FIELD_TOP + 64:
            return "Up"
        elif position.get_y() > FIELD_BOTTOM - 64:
            return "Down"
        else:
            return "Cheater"

