from django.db import models

class Comment(models.Model):
    thread = models.ForeignKey("threads.Thread", on_delete=models.CASCADE)
    reddit_id = models.CharField(max_length=20)
    body = models.TextField()
    score = models.IntegerField(default=0)
    permalink = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    parent_id = models.ForeignKey("Comment", on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField("tags.Tag", blank=True)

    def __str__(self):
        return self.body
