from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    date = models.DateField(auto_now=True)
    img = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f'Author: {self.author} <---> Title: {self.title}'