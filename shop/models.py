from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name="Title", unique=True)

class ProductGroup(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name     = models.CharField(max_length=80, verbose_name="Name")
    

class SubCategory(models.Model):
    pass

class ProductType(models.Model):
    pass

class ProductImage(models.Model):
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE)
    image   = models.FileField()

class Product(models.Model):
    title       = models.CharField(max_length=80, verbose_name="Name")
    price       = models.FloatField(min=0.0, verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    rate        = models.FloatField(min=0.0, max=5.0)
    quantity    = models.PositiveIntegerField()

class ProductCommentImage(models.Model):
    product_comment = models.ForeignKey("ProductComment")
    image           = models.FileField()

class ProductComment(models.Model):
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE)
    content = models.TextField()
    rate    = models.FloatField(min=0.0, max=5.0)
