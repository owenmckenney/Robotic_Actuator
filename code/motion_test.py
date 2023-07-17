import asyncio
import math
import moteus

async def main():
    c = moteus.Controller()

    await c.set_stop()

    while True:
    
        state = await c.set_position(position=math.nan, query=True)

        # Print out everything.
        print(state)

        # Print out just the position register.
        print("Position:", state.values[moteus.Register.POSITION])

        # And a blank line so we can separate one iteration from the
        # next.
        print()

        await asyncio.sleep(0.02)

if __name__ == '__main__':
    asyncio.run(main())
