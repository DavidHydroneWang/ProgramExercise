#!/usr/bin/env python
# coding=utf-8
from turtle import Shape, Screen, Turtle, Vec2D as Vec

# user input
G = 8
NUM_LOOPS = 4100
Ro_X = 0
Ro_Y = -85
Vo_X = 485
Vo_Y = 0


class GravSys():
    """runs a gravity simulation on n-bodies."""

    def __init__(self):
        self.bodies = []
        self.t = 0
        self.dt = 0.001

    def sim_loop(self):
        """loop bodies in a list through time steps"""
        for _ in range(NUM_LOOPS):
            self.t += self.dt
            for body in self.bodies:
                body.step()


class Body(Turtle):
    """Celestial object that orbits and projects gravity fields"""
    def __init__(self, mass, start_loc, vel, gravsys, shape):
        super().__init__(shape=shape)
        self.gravsys = gravsys
        self.penup()
        self.mass = mass
        self.setpos(start_loc)
        self.vel = vel
        gravsys.bodies.append(self)
        # self.resizemode("user")
        # self.pendown()  # nucomment to draw path behind object

    def acc(self):
        """calculate combined force on body and return vector components"""
        a = Vec(0, 0)
        for body in self.gravsys.bodies:
            if body != self:
                r = body.pos() - self.pos()
                a += (G * body.mass / abs(r)**3) * r  # Units: dist/time^2.
        return a

    def step(self):
        """Calculate position, orientation, and velocity of a body."""
        dt = self.gravsys.dt
        a = self.acc()
        self.vel = self.vel + dt * a
        self.setpos(self.pos() + dt * self.vel)
        if self.gravsys.bodies.index(self) == 2:
            rotate_factor = 0.0006
            self.setheading((self.heading() - rotate_factor * self.xcor()))
            if self.xcor() < -20:
                self.shape('arrow')
                self.shapesize(0.5)
                self.setheading(105)


def main():
    # setup screen
    screen = Screen()
    screen.setup(width=1.0, height=1.0)
    screen.bgcolor('black')
    screen.title('Apollo 8 Free Return simulation')

    # instantiate gravitational system
    gravsys = GravSys()

    # instantiate Earth turtle
    image_earth = 'earth_100x100.gif'
    screen.register_shape(image_earth)
    earth = Body(1000000, (0, -25), Vec(0, -2.5), gravsys, image_earth)
    earth.pencolor('white')
    earth.getscreen().tracer(0, 0)

    # instantiate moon turtle
    image_moon = 'moon_27x27.gif'
    screen.register_shape(image_moon)
    moon = Body(32000, (344, 42), Vec(-27, 147), gravsys, image_moon)
    moon.pencolor('gray')

    # build command-module(csm) shape
    csm = Shape('compound')
    cm = ((0, 30), (0, -30), (30, 0))
    csm.addcomponent(cm, 'white', 'white')
    sm = ((-60, 30), (0, 30), (0, -30), (-60, -30))
    csm.addcomponent(sm, 'white', 'black')
    nozzle = ((-55, 0), (-90, 20), (-90, -20))
    csm.addcomponent(nozzle, 'white', 'white')
    screen.register_shape('csm', csm)

    # instaniate Apollo 8 CSM module
    ship = Body(1, (Ro_X, Ro_Y), Vec(Vo_X, Vo_Y), gravsys, 'csm')
    ship.shapesize(0.2)
    ship.color('white')
    ship.getscreen().tracer(1, 0)
    ship.setheading(90)

    gravsys.sim_loop()


if __name__ == '__main__':
    main()