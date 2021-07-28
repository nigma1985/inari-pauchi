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

        left, top, right, bottom = 0, 0, img.width, img.height
        if img.height > img.width:
            cut = img.height - img.width
            top = cut/2
            bottom = img.height - (cut/2)
        if img.width > img.height:
            cut = img.width - img.height
            left = cut/2
            right = img.width - (cut/2)

        cropped = img.crop((left, top, right, bottom))

        if cropped.height > 300 or cropped.width > 300:
            form_factor = max([cropped.height, cropped.width]) / min([cropped.height, cropped.width])
            size = min([300, cropped.height, cropped.width]) * form_factor
            output_size = (size, size)
            cropped.thumbnail(output_size)
            
        cropped.save(self.image.path)