import csv
from constants import *
from game.casting.animation import Animation
# from game.casting.ball import 
from game.casting.body import Body
from game.casting.brick import Brick
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.player import Player
from game.casting.enemy import Enemy
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_brick_action import CollideBrickAction
from game.scripting.collide_enemy_action import CollideEnemyAction
from game.scripting.collide_player_action import CollidePlayerAction
from game.scripting.control_player_action import ControlPlayerAction
from game.scripting.draw_ball_action import DrawBallAction
from game.scripting.draw_bricks_action import DrawBricksAction
from game.scripting.draw_enemy_action import DrawEnemyAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_player_action import DrawPlayerAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_player_action import MovePlayerAction
from game.scripting.move_enemy_action import MoveEnemyAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BRICKS_ACTION = CollideBrickAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_ENEMY_ACTION = CollideEnemyAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_PLAYER_ACTION = CollidePlayerAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_PLAYER_ACTION = ControlPlayerAction(KEYBOARD_SERVICE)
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    DRAW_BRICKS_ACTION = DrawBricksAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_PLAYER_ACTION = DrawPlayerAction(VIDEO_SERVICE)
    DRAW_ENEMY_ACTION = DrawEnemyAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_PLAYER_ACTION = MovePlayerAction()
    MOVE_ENEMY_ACTION = MoveEnemyAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        # self._add_ball(cast)
        self._add_bricks(cast)
        self._add_player(cast)
        self._add_enemies(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        # self._add_ball(cast)
        self._add_bricks(cast)
        self._add_player(cast)
        self._add_enemies(cast)
        # self._add_dialog(cast, PREP_TO_START)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 0))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        # self._add_ball(cast)
        self._add_player(cast)
        self._add_enemies(cast)
        self._add_dialog(cast, PREP_TO_START)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 0))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        # self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_PLAYER_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        # self._add_ball(cast)
        self._add_player(cast)
        self._add_enemies(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        #     ball.release()

    # def _add_ball(self, cast):
    #     cast.clear_actors(BALL_GROUP)
    #     x = CENTER_X - BALL_WIDTH / 2
    #     y = SCREEN_HEIGHT - PLAYER_HEIGHT - BALL_HEIGHT  
    #     position = Point(x, y)
    #     size = Point(BALL_WIDTH, BALL_HEIGHT)
    #     velocity = Point(0, 0)
    #     body = Body(position, size, velocity)
    #     image = Image(BALL_IMAGE)
    #     ball = Ball(body, image, True)
    #     cast.add_actor(BALL_GROUP, ball)

    def _add_bricks(self, cast):
        cast.clear_actors(BRICK_GROUP)
        
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)
        
        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            room_x, room_y = self._get_room(cast)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):

                    x = FIELD_LEFT + c * BRICK_WIDTH
                    y = FIELD_TOP + r * BRICK_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    points = color

                    # if frames == 1:
                    #     points *= 2
                    if room_x == 'Left':
                        if x == 0:
                            color = "1"
                            frames = 1
                            points = "1"
                    elif room_x == 'Right':
                        if x == 992:
                            color = "1"
                            frames = 1
                            points = color
                                
                    if room_y == "Top":
                        if y == 60: 
                            color = "1"
                            frames = 1
                            points = color
                    elif room_y == 'Bottom':
                        if y == 540:
                            color = "1"
                            frames = 1
                            points = color
                    
                    position = Point(x, y)
                    size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                    velocity = Point(0, 0)
                    images = BRICK_IMAGES[color][0:frames]

                    body = Body(position, size, velocity)
                    animation = Animation(images, BRICK_RATE, BRICK_DELAY)

                    brick = Brick(body, animation, points)
                    cast.add_actor(BRICK_GROUP, brick)

    def _get_room(self, cast) -> tuple:
        stats = cast.get_first_actor(STATS_GROUP)
        room = stats.get_level()
        for r, row in enumerate(ROOMS):
            for c, column in enumerate(row):
                if(column == room):
                    player_x=c
                    player_y=r
        if player_x == 0:
            x = "Left"
        elif player_x == ROOM_RIGHT:
            x = "Right"
        else:
            x= "None"
        if player_y == 0:
            y = "Top"
        elif player_y == ROOM_BOTTOM:
            y = "Bottom"
        else:
            y= "None"
        return x, y

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_player(self, cast):
        cast.clear_actors(PLAYER_GROUP)
        x = CENTER_X - PLAYER_WIDTH / 2
        y = CENTER_X / 2
        position = Point(x, y)
        size = Point(PLAYER_WIDTH, PLAYER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(PLAYER_IMAGES, PLAYER_RATE)
        player = Player(body, animation)
        cast.add_actor(PLAYER_GROUP, player)

    def _add_enemies(self, cast):
        cast.clear_actors(ENEMY_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = ENEMY_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):

                    x = FIELD_LEFT + c * ENEMY_WIDTH
                    y = FIELD_TOP + r * ENEMY_HEIGHT
                    
                    type = column[0]
                    frames = int(column[1])

                    if type != "0":
                        position = Point(x, y)
                        size = Point(ENEMY_WIDTH, ENEMY_HEIGHT)
                        velocity = Point(0, 0)

                        images = ENEMY_IMAGES[type][0:frames]

                        body = Body(position, size, velocity)
                        animation = Animation(images, ENEMY_RATE)

                        enemy = Enemy(body, animation, type)
                        cast.add_actor(ENEMY_GROUP, enemy)
    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        # script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.DRAW_BRICKS_ACTION)
        script.add_action(OUTPUT, self.DRAW_PLAYER_ACTION)
        script.add_action(OUTPUT, self.DRAW_ENEMY_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        # script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.MOVE_PLAYER_ACTION)
        script.add_action(UPDATE, self.MOVE_ENEMY_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BRICKS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_ENEMY_ACTION)
        script.add_action(UPDATE, self.COLLIDE_PLAYER_ACTION)
        # script.add_action(UPDATE, self.MOVE_PLAYER_ACTION)
        script.add_action(UPDATE, self.MOVE_ENEMY_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)