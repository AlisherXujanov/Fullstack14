from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Blog: " + self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Blogs"