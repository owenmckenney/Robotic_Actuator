# getting rotation values for knee and thigh joint
# based on desired x and y displacement from rotation axis

import math
import time
import asyncio
import moteus
import moteus_pi3hat

a = 200
b = 150

max_hyp = math.sqrt(a**2 + b**2) * 0.98

async def main():
    transport = moteus_pi3hat.Pi3HatRouter(
        servo_bus_map = {
            1:[11],
            2:[11]
        }
    )

    hip_servo = moteus.Controller(id=1, transport=transport)
    knee_servo = moteus.Controller(id=2, transport=transport)

    await hip_servo.set_stop()
    await knee_servo.set_stop()

#async def zero(s1_zero, s2_zero):

    while True:

        y = round(float(input("enter desired y displacement: ")), 4)
        x = round(float(input("enter desired x displacement: ")), 4)

        gamma = math.tan(x/y)
        theta = math.acos(((x**2 + y**2) + a**2 - b**2)/(2*a*math.sqrt(x**2 + y**2)))
        phi = math.acos((a**2 + b**2 - (x**2 + y **2))/(2*a*b))

        # rotations are measured from position 0 (or relative 0)
    
        hip_pos = math.degrees(theta) * 1/360 * -6
        knee_pos = math.degrees(phi) * 1/360 * -6
    
        print(round(math.degrees(gamma), 4), round(math.degrees(theta), 4), round(math.degrees(phi), 4))

        print(hip_pos, knee_pos)

        commands = [
            hip_servo.make_position(
                position = hip_pos,
                accel_limit = 2.0, 
                velocity_limit = 4,
                maximum_torque = 0.1, 
                watchdog_timeout = math.nan
            ),
            knee_servo.make_position(
                position = knee_pos,
                accel_limit = 2.0,
                velocity_limit = 4.0,
                maximum_torque = 0.1,
                watchdog_timeout = math.nan
            )
        ]

        results = await transport.cycle(commands)


if __name__ == '__main__':
    asyncio.run(main())


