#7 pritns yes
#8 prints no
#9 prints 3.99
#10 prints 
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)