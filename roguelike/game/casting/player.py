from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

global player_x
global player_y
player_x=1
player_y=1

class Player(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._x = player_x
        self._y = player_y
        self._lives = current_lives

    # def get_location(self) -> tuple:
    #     """Gets the bat's location on world map.
        
    #     Returns:
    #         Tuple of location.
    #     """
    #     return self._x, self._y

    # def set_location(self, x, y) -> None:
    #     """Gets the player's location on world map.
        
    #     Returns:
    #         Tuple of location.
    #     """
    #     player_x=x
    #     player_y=y
    #     return

    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the bat to the left."""
        velocity = Point(-PLAYER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the bat to the right."""
        velocity = Point(PLAYER_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def swing_up(self):
        """Steers the bat to the up."""
        velocity = Point(0, -PLAYER_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_down(self):
        """Steers the bat to the down."""
        velocity = Point(0, PLAYER_VELOCITY)
        self._body.set_velocity(velocity)

    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)

    def bounce(self):
        velocity_x = self._body.get_velocity().get_x()
        velocity_y = self._body.get_velocity().get_y()
        x = self._body.get_position().get_x()
        y = self._body.get_position().get_y()
        if velocity_x==0:
            if velocity_y < 0:
                self._body.set_position(Point(x,y+16))
            elif velocity_y > 0:
                self._body.set_position(Point(x,y-16))
        elif velocity_y==0:
            if velocity_x < 0:
                self._body.set_position(Point(x+16,y))
            elif velocity_x > 0:
                self._body.set_position(Point(x-16,y))
        # velocity = Point(x, y)
        # self._body.set_velocity(velocity)

    