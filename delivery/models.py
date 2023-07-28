from django.db import models
from cloudinary.models import CloudinaryField

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    caption = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    # def __str__(self):
    #     return self.name
    
    def __str__(self):
        return self.caption if self.caption != "" else "No caption"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)


def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'