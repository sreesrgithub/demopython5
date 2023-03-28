from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images')
    author = models.CharField(max_length=250)
    date = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.title
