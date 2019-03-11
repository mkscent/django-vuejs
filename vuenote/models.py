from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.title
