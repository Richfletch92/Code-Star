from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    creates a page for the about section of the website.
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    creates a model for collaboration requests.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
