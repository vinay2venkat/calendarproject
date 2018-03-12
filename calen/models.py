from django.db import models

class cartoon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    poster = models.FileField()
    download = models.FileField()

    def __str__(self):
        return self.name

class movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    poster = models.FileField()
    download = models.FileField()

    def __str__(self):
        return self.name

class music(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=100)
    poster = models.FileField()
    download = models.FileField()

    def __str__(self):
        return self.name
