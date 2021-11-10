from django.db import models

# Create your models here.
class campingTools(models.Model):
    name = models.CharField(max_length = 30)
    quantity = models.IntegerField(default = 10)
    rental_fee = models.IntegerField(default = 20000)
    body = models.CharField(max_length = 300)   

    # 캠핑 용품 카테고리
    CATEGORIES = (("tent", "tent")
                , ("grill", "grill")
                , ("table", "table")
                , ("lantern", "lantern")
                , ("firewood", "firewood"))

    category = models.CharField(max_length = 20, choices = CATEGORIES, default = "tent")
    image = models.ImageField(default = 'static/lantern.jpg')

