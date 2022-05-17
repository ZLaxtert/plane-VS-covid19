from typing import Sized
from ursina import *
from ursina import texture
from ursina import collider
from ursina import curve
 
app = Ursina()
me = Animation('assets/animation',collider='box',x=-12,y=5,scale=5)
Sky()
camera.orthographic = True
camera.fov = 20

Entity(model='quad',texture='assets/bg',scale=37,z=1)

fly = Entity(
    model='cube',
    texture='assets/enemy',
    collider='box',
    scale=2,
    x=20,
    y=-10
)
flies = []
def newFly():
    new = duplicate(
        fly,
        y=-5+(5214*time.dt)%15
    )
    flies.append(new)
    invoke(newFly, delay=1)
newFly()

def update():
    for fly in flies:
        fly.x -= 4*time.dt
    me.y += held_keys['w']*6*time.dt
    me.y -= held_keys['s']*6*time.dt
    me.x += held_keys['d']*6*time.dt
    me.x -= held_keys['a']*6*time.dt
    a = held_keys['w']*-20
    b = held_keys['s']*20
    if a != 0:
        me.rotation_z = a
    else :
        me.rotation_z = b    
    for fly in flies:
        fly.x -= 4*time.dt 
        touch = fly.intersects()
        if touch.hit:
            flies.remove(fly)
            destroy(fly)
        t = me.intersects()
        if t.hit and t.entity.scale==2:
            quit()
    
def input(key):
    if key == 'space':
        e = Entity(
            y = me.y,
            x = me.x+4,
            model='cube',
            texture='assets/ammo',
            collider='cube'
        )

        e.animate_x(
            30,
            duration=2,
            curve=curve.linear
        )
        invoke(destroy, e, delay=2)

app.run()

