from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.cast import Cast
from game.casting.body import Body

class Ball(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        
    # def bounce_x(self):
    #     """Bounces the ball in the x direction."""
    #     velocity = self._body.get_velocity()
    #     rn = random.uniform(0.9, 1.1)
    #     vx = velocity.get_x() * rn * -1
    #     vy = velocity.get_y()
    #     velocity = Point(vx, vy)
    #     self._body.set_velocity(velocity)

    # def bounce_y(self):
    #     """Bounces the ball in the y direction."""
    #     velocity = self._body.get_velocity()
    #     rn = random.uniform(0.9, 1.1)
    #     vx = velocity.get_x()
    #     vy = velocity.get_y() * rn * -1 
    #     velocity = Point(vx, vy)
    #     self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def release(self):
        """Release the ball from the posistion of the entity"""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BALL_VELOCITY * rn, BALL_VELOCITY * rn])
        vy = -BALL_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
       
        # vx = Point.get_x()
        # vy = Point.get_y()
        # velocity = Point(vx, vy)
        # self._body.set_velocity(velocity)
        # cast.clear_actors(BALL_GROUP)
        
       
        
        
        # ball = Ball(body, self.image, True)
        # cast.add_actor(BALL_GROUP, ball)
    
    
    # def _add_ball(self, cast):
        # cast.clear_actors(BALL_GROUP)
        # x = CENTER_X - BALL_WIDTH / 2
        # y = SCREEN_HEIGHT - PLAYER_HEIGHT - BALL_HEIGHT  
        # position = Point(x, y)
        # size = Point(BALL_WIDTH, BALL_HEIGHT)
        # velocity = Point(0, 0)
        # body = Body(position, size, velocity)
        # image = Image(BALL_IMAGE)
        # ball = Ball(body, image, True)
        # cast.add_actor(BALL_GROUP, ball)