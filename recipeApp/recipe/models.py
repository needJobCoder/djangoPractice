from django.db import models
# Create your models here.


class Recipe(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    class Meta:
        app_label = 'recipe'
    def _str_(self):
        return self.title
    