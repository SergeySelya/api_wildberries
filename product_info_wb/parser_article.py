import requests
import re


NUMBER_OF_BASKET_SERVERS = 11


def get_product(article: str):
    server_id = 0
    while True:
        server_id += 1
        server_id_str = f"0{server_id}" if server_id < 10 else str(server_id)
        response = requests.get(
            f"https://basket-{server_id_str}.wb.ru/vol{article[:-5]}/part{article[:-3]}/{article}/info/ru/card.json"
        )
        if response.status_code == 200:
            card_json = response.json()
            break
        elif server_id == NUMBER_OF_BASKET_SERVERS:
            return {'article is not avaible': None}
    return {
        "article": card_json["nm_id"],
        "brand": card_json["selling"]["brand_name"],
        "title": card_json["imt_name"],
    }


if __name__ == "__main__":
    get_product('66807011')
