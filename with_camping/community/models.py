from django.db import models

# Create your models here.
# 게시글에 대한 모델
class BulletinPost(models.Model):
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)
    creation_date = models.DateTimeField(blank = True, null = True)

    # 게시글 카테고리
    CATEGORIES = (("camping_tools", "camping_tools")
                , ("camping_ground", "camping_ground")
                , ("free", "free")
                , )

    category = models.CharField(max_length = 20, choices = CATEGORIES, default = "camping_tools")
    body = models.CharField(max_length = 300)