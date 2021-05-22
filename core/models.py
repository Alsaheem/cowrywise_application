from django.db import models

# Create your models here.
class MyUUIDCreator(models.Model):
    generated_id = models.UUIDField("")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
