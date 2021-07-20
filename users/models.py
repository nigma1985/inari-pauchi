from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            form_factor = max([img.height, img.width]) / min([img.height, img.width])
            size = min([300, img.height, img.width]) * form_factor
            output_size = (size, size)
            img.thumbnail(output_size)
            img.save(self.image.path)