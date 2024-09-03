from pyppeteer import launch
import os
import asyncio
from Helpers.AsyncioHelper import AsyncioHelper
class RewardsService:

    _page=None
    _browser=None

    def __init__(self) -> None:
        pass

    def setPage(self,page):
        self._page=page
        
    def setBrowser(self,browser):
        self._browser=browser
        
    async def run(self):
        print(os.getenv("executablePath"))
        await self.openBrowser()

    async def openBrowser(self):
        # print('I wanna Open Browser Now')
        browser = await launch(headless=False,executablePath=os.getenv("executablePath"),
                               ignoreDefaultArgs=["--enable-automation"],
                                defaultViewport=None)
        pagesTotal =await browser.pages()
        
        page = await browser.newPage()
        self.setPage(page)
        self.setBrowser(browser)
        
        
        
        await page.goto(os.getenv("rewardsUrl"))
        await asyncio.sleep(10)
        await self.getCardsRewards()
    
    async def getCardsRewards(self):
        firstThreeCards=await self._page.querySelectorAll("card-content")
        
        if len(firstThreeCards) > 3:
            for i in range(4):
                await asyncio.sleep(3)
                await self.openLinkRewards(firstThreeCards[i])
                
        
    
    async def openLinkRewards(self,card):
        await card.click()
        # await asyncio.sleep(3)
        # await self.closeLastTab()
 
    
    async def closeLastTab(self):
        pagesTotal = await self._browser.pages()

        print(f"Number of pages: {(pagesTotal)}")

        # # Close the last page
        # if pages:
        #     last_page = pages[-1]
        #     await last_page.close()
        #     print("Closed the last page.")
        
        
     