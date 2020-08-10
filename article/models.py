from django.db import models


# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=80)
  subtitle = models.CharField(max_length=240, blank=True)
  body = models.TextField()
  image = models.ImageField(null=True, upload_to='static/article_images/')
  datetime = models.DateTimeField(auto_now_add=True, name="datetime", verbose_name="datetime")
