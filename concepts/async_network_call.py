import asyncio
import aiohttp
import json


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:

        # wait for data
        result = await fetch(session, "https://pokeapi.co/api/v2/pokemon/ditto")

        # deserialize the json string into a python object
        json_object = json.loads(result)

        # print the json python object as a formatted json string
        print(json.dumps(json_object, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
