from pydantic import BaseModel
from product_info_wb.models import Products


class ProductsModel(BaseModel):
    article: int
    brand: str
    title: str


def main(articles):
    co_model = ProductsModel(**articles)
    Products.objects.create(article=co_model.article, brand=co_model.brand, title=co_model.title)
