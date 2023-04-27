from django.contrib import admin
from .models import (
    Category,
    ProductGroup,
    SubCategory,
    ProductType,
    ProductImage,
    Product,
    ProductComment,
    ProductCommentImage
)

admin.site.register(Category)
admin.site.register(ProductGroup)
admin.site.register(SubCategory)
admin.site.register(ProductType)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(ProductCommentImage)