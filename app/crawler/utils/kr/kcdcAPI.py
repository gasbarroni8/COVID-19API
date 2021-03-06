import aiohttp
from app.ext.utils.Performance import Performance
from async_lru import alru_cache
from bs4 import BeautifulSoup


class kcdcAPI:
    def __init__(self, mode):
        """Initialize
        mode: 
            11 -> 발생동향
            12 -> 확진환자 이동경로
            13 -> 시도별 발생동향
        """
        self.loop = Performance()
        # 질병관리본부 COVID-19 URL
        self.url = "http://ncov.mohw.go.kr/bdBoardList_Real.do"
        self.MainUrl = "http://ncov.mohw.go.kr/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10.0.0; SM-F700NZPAKOO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"
        }
        self.payload = {
            "brdGubun": mode 
        }

    @alru_cache(maxsize=32)
    async def GetInfectiousDiseases(self):
        """국내 감염증 정보 파싱"""
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url, params=self.payload) as resp:
                info = await resp.text()
        soup = await self.loop.run_in_threadpool(lambda: BeautifulSoup(info, 'lxml'))
        return soup

    @alru_cache(maxsize=32)
    async def GetInfectiousDiseases2(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url, params=self.payload) as resp:
                info = await resp.text()
        return info

    @alru_cache(maxsize=32)
    async def GetInfectiousDiseases3(self):
        """국내 감염증 정보 파싱"""
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.url, params=self.payload) as resp:
                info = await resp.text()
        return info

    @alru_cache(maxsize=32)
    async def GetInfectiousDiseases4(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url=self.MainUrl) as resp:
                info = await resp.text()
        return info