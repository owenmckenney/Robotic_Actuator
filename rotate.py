# rotates a single servo motor on CAN bus 1 ID 1

import asyncio
import moteus
import time
import math
import sys

async def main():
    c1 = moteus.Controller()
    await c1.set_stop()

    while True:
        pos = input("entire desired postion: ")

        if pos == 'exit':
            sys.exit("")
        
        pos = round(float(pos), 2)
 
        state = await c1.set_position(
                position=pos, 
                velocity=0.0,
                accel_limit=2.0,
                velocity_limit=5,
                maximum_torque=0.075,
                watchdog_timeout=math.nan,
                query=True
                )
        
        print(state)
        print()

        await asyncio.sleep(0.02)

asyncio.run(main())
