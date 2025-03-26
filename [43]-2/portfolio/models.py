from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# Create your models here.
