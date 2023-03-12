import requests
import asyncio
import aiohttp


NUMBER_OF_BASKET_SERVERS = 11
result =[]

async def get_one(article, session):
    server_id = 0
    while True:
        server_id += 1
        server_id_str = f"0{server_id}" if server_id < 10 else str(server_id)
        async with session.get(
                f"https://basket-{server_id_str}.wb.ru/vol{article[:-5]}/part{article[:-3]}/{article}/info/ru/card.json"
        ) as resp:
            if resp.status == 200:
                card_json = await resp.json()
                result.append({
                    "article": card_json["nm_id"],
                    "brand": card_json["selling"]["brand_name"],
                    "title": card_json["imt_name"],
                })
                break
            elif server_id == NUMBER_OF_BASKET_SERVERS:
                return {'article is not avaible'}


async def run(articles):
    async with aiohttp.ClientSession() as session:
        a = []
        for article in articles:
            task = asyncio.ensure_future(get_one(str(article),session))
            a.append(task)
        await asyncio.gather(*a)



def main(articles):
    try:
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(run(articles))
        loop.run_until_complete(future)
        return result
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            asyncio.get_event_loop()
            future = asyncio.ensure_future(run(articles))
            loop.run_until_complete(future)
            return result



if __name__ == "__main__":
    main()



# NUMBER_OF_BASKET_SERVERS = 11
#
#
# def get_product(article: str):
#     server_id = 0
#     while True:
#         server_id += 1
#         server_id_str = f"0{server_id}" if server_id < 10 else str(server_id)
#         response = requests.get(
#             f"https://basket-{server_id_str}.wb.ru/vol{article[:-5]}/part{article[:-3]}/{article}/info/ru/card.json"
#         )
#         if response.status_code == 200:
#             card_json = response.json()
#             break
#         elif server_id == NUMBER_OF_BASKET_SERVERS:
#             return {'article is not avaible': None}
#     return {
#         "article": card_json["nm_id"],
#         "brand": card_json["selling"]["brand_name"],
#         "title": card_json["imt_name"],
#     }
#
#
# if __name__ == "__main__":
#     get_product('66807011')
