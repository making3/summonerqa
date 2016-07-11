from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    regex = models.CharField(max_length=100)
    Category = models.ForeignKey(Category, blank=True, null=True)

    def __str__(self):
        return self.name
