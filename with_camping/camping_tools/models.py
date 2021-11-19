from django.db import models

# Create your models here.
class CampingTools(models.Model):
    name = models.CharField(max_length = 30)
    quantity = models.IntegerField(default = 10)
    price = models.IntegerField(default = 5000)
    rental_price = models.IntegerField(default = 20000)
    body = models.CharField(max_length = 10000)   

    # 캠핑 용품 카테고리
    CATEGORIES = (("tent", "tent")
                , ("grill", "grill")
                , ("table", "table")
                , ("lantern", "lantern")
                , ("firewood", "firewood"))

    category = models.CharField(max_length = 20, choices = CATEGORIES, default = "lentern")
    image = models.ImageField(default = 'static/lantern.jpg')

    def __str__(self) :
        return self.name

class OrderList(models.Model) :
    order_Member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    order_List = models.ForeignKey('camping_tools.CampingTools', on_delete=models.CASCADE)

