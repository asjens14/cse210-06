from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
# from game.casting.cast import Cast


class CollideEnemyAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        enemies = cast.get_actors(ENEMY_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        balls = cast.get_actors(BALL_GROUP)


        for enemy in enemies:
            player_body = player.get_body()
            enemy_body = enemy.get_body()
    
            if self._physics_service.has_collided(player_body, enemy_body):
                player.bounce()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
               
                callback.on_next(NEXT_LEVEL)
                break
        
        for ball in balls:
            player_body = player.get_body()
            ball_body = ball.get_body()
    
            if self._physics_service.has_collided(player_body, ball_body):
                player.bounce()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
               
                callback.on_next(NEXT_LEVEL)
                break