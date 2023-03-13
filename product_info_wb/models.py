from django.db import models


class Products(models.Model):
    article = models.IntegerField()
    brand = models.CharField(max_length=20)
    title = models.CharField(max_length=20)

    @classmethod
    def create(cls,article, brand,title):
        article = cls(article=article)
        brand = cls(brand=brand)
        title = cls(title=title)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "Products"


