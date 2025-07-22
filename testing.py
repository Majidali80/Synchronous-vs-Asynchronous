#sync examples
import time

#step1:
print("Bike saf karo..")
time.sleep(5)
print("oil check karo")

#step#2
print("Chabi Byke main lagao...")
time.sleep(3)
print("Byke Start Karo")

#async example
import asyncio

#function banaye

async def bike():
    print("Bike saf karo..")
    await asyncio.sleep(5)
    print("oil check karo")

async def Oil_Check():
    print("Chabi Byke main lagao...")
    await asyncio.sleep(5)
    print("Byke Start Karo")

async def main():
    await asyncio.gather(
        bike(),
        Oil_Check()
    )

asyncio.run(main())
