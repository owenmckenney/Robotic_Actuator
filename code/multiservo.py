# rotates two servo motors on CAN bus 1 ID 1 and ID 2
# rotation time is not synced (spinning ID 1 clockwise 2 rotations
# and ID 2 clockwise 1 rotation will not complete simultaneously however 
# they will start simultaneously)

import math
import time
import asyncio
import moteus
import moteus_pi3hat

async def main():
    transport = moteus_pi3hat.Pi3HatRouter(
        servo_bus_map = {
            1:[11],
            2:[11]
        }
    )

    s1 = moteus.Controller(id=1, transport=transport)
    s2 = moteus.Controller(id=2, transport=transport)

    await s1.set_stop()
    await s2.set_stop()

    while True:
        s1_command = round(float(input("Enter desired pos for servo 1")), 2)
        s2_command = round(float(input("Enter desired pos for servo 2")), 2)

        commands = [
            s1.make_position(
                position = s1_command,
                velocity = 0.0,
                accel_limit = 2.0,
                velocity_limit = 1,
                maximum_torque = 0.15,
                watchdog_timeout = math.nan,
                query = True
                ),
            s2.make_position(
                position = s2_command,
                velocity = 0.0,
                accel_limit = 2.0,
                velocity_limit = 1,
                maximum_torque = 0.15,
                watchdog_timeout = math.nan,
                query = True
                )
            ]

        states = await transport.cycle(commands)

if __name__ == '__main__':
    asyncio.run(main())



