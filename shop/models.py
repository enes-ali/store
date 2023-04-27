from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name="Title", unique=True)
    link  = models.CharField(max_length=120, verbose_name="Category link")

    def __str__(self):
        return self.title


class ProductGroup(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name     = models.CharField(max_length=80, verbose_name="Name")
    link     = models.CharField(max_length=120, verbose_name="Product group link")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    product_group = models.ForeignKey(to=ProductGroup, on_delete=models.CASCADE)
    name          = models.CharField(max_length=80, verbose_name="Name")
    link          = models.CharField(max_length=120, verbose_name="Product group link")
    image         = models.ImageField()
    
    def __str__(self):
        return self.name


class ProductType(models.Model):
    sub_category = models.ForeignKey(to=SubCategory, on_delete=models.CASCADE)
    name         = models.CharField(max_length=80, verbose_name="Name")
    link         = models.CharField(max_length=120, verbose_name="Subcategory link")
    image        = models.ImageField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE)
    image   = models.ImageField()


class Product(models.Model):
    type        = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    title       = models.CharField(max_length=80, verbose_name="Name")
    price       = models.FloatField(
                    validators=[MinValueValidator(0, "Product price cannot be lower than zero")],
                    verbose_name="Price"
                )
    description = models.TextField(verbose_name="Description")
    rate        = models.FloatField(
                    validators=[
                        MinValueValidator(0, "Product rate Cannot be lower than zero"),
                        MaxValueValidator(5, "Product rate Cannot be highrt than 5"),
                    ]
                )
    quantity    = models.PositiveIntegerField()



class ProductCommentImage(models.Model):
    product_comment = models.ForeignKey("ProductComment", on_delete=models.CASCADE)
    image           = models.ImageField()



class ProductComment(models.Model):
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    rate    = models.FloatField(
                validators=[
                    MinValueValidator(0, "Comment rate Cannot be lower than zero"),
                    MaxValueValidator(5, "Comment rate Cannot be highrt than 5"),
                ]
            )