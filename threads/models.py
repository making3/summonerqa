from django.db import models

class Thread(models.Model):
    reddit_id = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    permalink = models.CharField(max_length=500)

    def __str__(self):
        return self.title
