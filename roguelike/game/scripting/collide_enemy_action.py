from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
import time
# from game.casting.cast import Cast


class CollideEnemyAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._start=time.time()
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        enemies = cast.get_actors(ENEMY_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        balls = cast.get_actors(BALL_GROUP)

        elapsed = time.time() - self._start
        print(elapsed)
        if elapsed >= 1:
            for enemy in enemies:
                player_body = player.get_body()
                enemy_body = enemy.get_body()
        
                if self._physics_service.has_collided(player_body, enemy_body):
                    # player.bounce()
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    stats = cast.get_first_actor(STATS_GROUP)
                    stats.lose_life()
                    self._start=time.time()

                    # callback.on_next(NEXT_LEVEL)
                    if stats.get_lives() == 0:
                        callback.on_next(GAME_OVER)
                        # self._audio_service.play_sound(over_sound)
                for ball in balls:
                    ball_body = ball.get_body()
                    if self._physics_service.has_collided(ball_body, enemy_body):
                        cast.remove_actor(ENEMY_GROUP, enemy)
                        cast.remove_actor(BALL_GROUP, ball)
                break
            
            for ball in balls:
                player_body = player.get_body()
                ball_body = ball.get_body()
                enemy_body = enemy.get_body()

                if self._physics_service.has_collided(player_body, ball_body):
                    # player.bounce()
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    stats = cast.get_first_actor(STATS_GROUP)
                    stats.lose_life()
                    self._start = time.time()
                
                
                    # callback.on_next(NEXT_LEVEL)
                    break
                