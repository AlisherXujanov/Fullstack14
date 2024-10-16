from django.db import models
from django.contrib.auth.models import User

# ORM  ->  Object Relational Mapping

# Create your models here.
class Todos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True, blank=True)
    background_color = models.CharField(max_length=20, default='lightblue')
    text_color = models.CharField(max_length=20, default='black')
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} of - {self.owner}" 

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
    