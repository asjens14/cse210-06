from constants import *
from game.scripting.action import Action


class DrawBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        if cast.get_actors(BALL_GROUP) is not None:
            balls = cast.get_actors(BALL_GROUP)
            for ball in balls:
                body = ball.get_body()

                if ball.is_debug():
                    rectangle = body.get_rectangle()
                    self._video_service.draw_rectangle(rectangle, PURPLE)
                    
                image = ball.get_image()
                position = body.get_position()
                self._video_service.draw_image(image, position)

        if cast.get_actors(ENEMY_BALL_GROUP) is not None:
            eballs = cast.get_actors(ENEMY_BALL_GROUP)
            for eball in eballs:
                body = eball.get_body()

                if eball.is_debug():
                    rectangle = body.get_rectangle()
                    self._video_service.draw_rectangle(rectangle, PURPLE)
                    
                image = eball.get_image()
                position = body.get_position()
                self._video_service.draw_image(image, position)