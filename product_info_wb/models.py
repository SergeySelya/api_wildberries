from django.db import models


class Products(models.Model):
    article = models.IntegerField()
    brand = models.CharField(max_length=20)
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "Products"
