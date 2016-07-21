SPACESHIP

http://www.codeskulptor.org/#examples-spaceship.py

	Make a spaceship that can fly, turn, stop in space, with friction 

	self.pos = ship's position (vectory in x, y)
	self.vel = ship's velocity (vector in x, y)
	self.angle = ship's angle (scalar)
	self.thrust = is it going forward or not? (bool)

```python
	self.pos[0] += self.vel[0]
	self.pos[1] += self.vel[1]

	forward = [math.cos(self.angle), math.sin(self.angle)]
		#the most important line of code, as you can turn yet still go forward
		self.vel[0] += forward[0]
		self.vel[1] += forward[1]

	self.vel[0] += forward[0]
	self.vel[1] += forward[1]

	friction = -c * velocity
	acceleration = thrust + friction
	velocity = velocity + acceleration
	velocity = velocity + thrust + friction
	velocity = velocity + thrust - c *  velocity
	velocity = (1 - c) * velocity + thrust

	self.pos[0] += self.vel[0]
	self.pos[1] += self.vel[1]

	self.vel[0] *= (1 - c)
	self.vel[1] *= (1 - c)


class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

class Spaceship(self, angle, angle_vel):
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

	def draw(self):
		canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

	def update(self):
        pass
```

SOUNDS

http://www.codeskulptor.org/#examples-sound.py        

SPRITES

http://www.codeskulptor.org/#examples-sprite_example.py

	velocity, angle, acceleration, will all 
	work together with the draw function

PROGRAMMING TIPS

http://www.codeskulptor.org/#examples-spaceship_template.py


