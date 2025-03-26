from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="მომხმარებელი")
    title = models.CharField(max_length=200, verbose_name="დასახელება")
    description = models.TextField(null=True, verbose_name="აღწერა")
    complete = models.BooleanField(default=False, verbose_name="შესრულება")
    created = models.DateTimeField(auto_now_add=True, verbose_name="შექმნილია") # უცვლელად დაიმახსოვრებს დამატების თარიღს

    def __str__(self):
        return self.title


class Meta:
    ordering = ['complete', '-created'] 

# Create your models here.
