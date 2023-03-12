import requests
import asyncio
import aiohttp


NUMBER_OF_BASKET_SERVERS = 15


async def get_article_info(article, session, articles_list: list):
    server_id = 0
    try:
        while True:
            server_id += 1
            server_id_str = f"0{server_id}" if server_id < 10 else str(server_id)
            async with session.get(
                f"https://basket-{server_id_str}.wb.ru/vol{article[:-5]}/part{article[:-3]}/{article}/info/ru/card.json"
            ) as resp:
                if resp.status == 200:
                    card_json = await resp.json()
                    articles_list.append(
                        {
                            "article": card_json["nm_id"],
                            "brand": card_json["selling"]["brand_name"],
                            "title": card_json["imt_name"],
                        }
                    )
                    break
                elif server_id == NUMBER_OF_BASKET_SERVERS:
                    raise ConnectionError
    except:
        articles_list.append(
            {
                "article": article,
                "brand": "Incorrect article",
                "title": "Incorrect article",
            }
        )


async def run(articles, articles_list):
    async with aiohttp.ClientSession() as session:
        a = []
        for article in articles:
            task = asyncio.ensure_future(
                get_article_info(
                    article=str(article), session=session, articles_list=articles_list
                )
            )
            a.append(task)
        await asyncio.gather(*a)


def main(articles):
    # try:
    articles_list = []
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.ensure_future(run(articles=articles, articles_list=articles_list))
    loop.run_until_complete(future)
    # loop.close()
    return articles_list
