#Sets
###Intro
* list = ordered sequence
* disctionary = key -> value mapping
* **set** = unordered collection of data with no duplicates

###Example 1
http://www.codeskulptor.org/#examples-sets.py

```python
instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

# set(['Warren', 'Rixner', 'Greiner', 'Wong'])

inst2 = set(['Rixner', 'Rixner', 'Warren', 'Warren', 'Greiner', 'Wong'])

print inst2

# set(['Warren', 'Rixner', 'Greiner', 'Wong'])

print instructors == inst2

# True

for inst in instructors:
	print inst

# Warren
# Rixner
# Greiner
# Wong

instructors.add('Colbert')
print instructors
instructors.add('Rixner')
instructors.remove('Wong')
print instructors

# set(['Warren', 'Rixner', 'Greiner', 'Colbert'])
```
###Putting Sets in Game

We want to use sets so we can make lots of rocks that don't get duplicated

http://www.codeskulptor.org/#examples-set_difference.py

```python
instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

# set(['Warren', 'Rixner', 'Greiner', 'Wong'])

def get_rid_of(inst_set, starting_letter):
	remove_set = set([])
	for inst in inst_set:
		if inst[0] == starting_letter:
			remove_set.add(inst)
	inst_set.difference_update(remove_set)

get_rid_of(instructors, "W")
print instructors

# set([Rixner', 'Greiner'])

get_rid_of(instructors, "G")

# set(['Warren', 'Rixner', 'Wong'])
```

#Collisions for Sprites
###Intro
* Collision Logic
	* given d = distance between two radii
	* if d > r1 + r2, no collision
	* if d < r1 + r2, collision
* Objects
	* ship
	* rocks (set)
	* missiles (set)
		* so you can make multiple missiles
* Collisions
	* ship - rock
		* rock.collide(ship)
```python
def groupCollide(g, s):
	rs = set([])
	for s in myset:
		rs.add(s)
	myset.d_u(rs) #difference update

# or

	for s in list(myset):
		myset.remove(s)
```
	* missiles - rocks
```python
def groupGroupCollide(g1, g2): #g1 = missile, #g2 = rock
	groupCollide(...) #call first groupCollide, which returns T/F
		return numberOfTrues 
```
#Sprite Animation
###Intro

http://www.codeskulptor.org/#examples-asteroid_animation.py

http://www.codeskulptor.org/#examples-explosion_animation.py

http://www.codeskulptor.org/#examples-ricerocks_template.py

#Final Product

http://www.codeskulptor.org/#user41_9m7bPSM3qo_5.py
