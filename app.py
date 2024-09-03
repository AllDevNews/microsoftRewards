from Services.rewards.RewardsService import RewardsService
import asyncio
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':

    RS=RewardsService()
    asyncio.get_event_loop().run_until_complete(RS.run())