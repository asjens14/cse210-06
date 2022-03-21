from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
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