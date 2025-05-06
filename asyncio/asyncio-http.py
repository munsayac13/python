import aiohttp
import asyncio
from bs4 import BeautifulSoup


# It is a very common practice to use async keyword with HTTP requests, if we fetch data from multiple URLs using a synchronous approach, each request blocks the execution until it completes. However, with async, we can send multiple requests simultaneously, making the program much faster.
# aiohttp is a library used for making async http requests
async def func():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.skysports.com/premier-league-results/2025-04") as res:
            data = await res.text()
            soup = BeautifulSoup(data, features="html.parser")
            print(soup.select(".fixres__item")[0].get_text(strip=True))
            print(soup.select(".fixres__item")[0].get_text(strip=True, separator="|"))
            print(soup.select(".fixres__item")[0].get_text(strip=True, separator="|").split("|")[:5])
            print(soup.select(".fixres__item")[0].find_previous(class_="fixres__header2"))
            print(soup.select(".fixres__item")[0].find_previous(class_="fixres__header2").get_text(strip=True))


asyncio.run(func())


async def get_url_text(session, url):
    async with session.get(url) as response:
        return await response.text()

async def functwo():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://python.org"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [get_url_text(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        # Print type
        print(type(responses))

        for url, response in zip(urls, responses):
            print(f"URL: {url} - Length of response: {len(response)} characters")

asyncio.run(functwo())


