# getting rotation values for knee and thigh joint
# based on desired x and y displacement from rotation axis

import math

a = 200
b = 150

max_hyp = math.sqrt(a**2 + b**2) * 0.98

while True:

    y = round(float(input("enter desired y displacement: ")), 4)
    x = round(float(input("enter desired x displacement: ")), 4)

    #if math.sqrt(x**2 + y**2) > max_hyp:
        #pass
    #else:

    gamma = math.tan(x/y)
    theta = math.acos(((x**2 + y**2) + a**2 - b**2)/(2*a*math.sqrt(x**2 + y**2)))
    phi = math.acos((a**2 + b**2 - (x**2 + y **2))/(2*a*b))

    # rotations are measured from position 0 (or relative 0)

    hip_pos = math.degrees(theta) * 1/360
    knee_pos = math.degrees(phi) * 1/360
    
    print(round(math.degrees(gamma), 4), round(math.degrees(theta), 4), round(math.degrees(phi), 4))

    print(hip_pos, knee_pos)

