from constants import *
from game.scripting.action import Action


class DrawPlayerAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        body = player.get_body()

        if player.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = player.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)