from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    USER_TYPE = (
        ('User','User'),
        ('Restaurant','Restaurant'),
        ('Delivery_Partner','Delivery_Partner')
    )
    email = models.EmailField(unique=True)
    profile_img = models.ImageField(upload_to='images/',null=True)
    contact = models.CharField(max_length=15,null=True)
    role = models.CharField(choices=USER_TYPE,max_length=20,null=True)


class Restaurant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='restaurant_profile')
    restaurant_name = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=15)

    def __str__(self):
        return self.restaurant_name

   

class DeliveryPartner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='delivery_partner_profile')
    vehicle_number = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)




class Category(models.Model):
    CATEGORY_CHOICES = [
    ('Pizza', '\U0001F355'),  # 🍕
    ('Burgers', '\U0001F354'),  # 🍔
    ('Sushi', '\U0001F363'),  # 🍣
    ('Desserts', '\U0001F370'),  # 🍰
    ('Indian', '\U0001F35B'),  # 🍛
    ('Chinese', '\U0001F961'),  # 🥡
    ('Mexican', '\U0001F32E'),  # 🌮
    ('Salads', '\U0001F957'),  # 🥗
    ('Beverages', '\U0001F964'),  # 🥤
    ('Seafood', '\U0001F99E'),  # 🦞
    ('BBQ', '\U0001F356'),  # 🍖
    ('Pasta', '\U0001F35D'),  # 🍝
    ('Breakfast', '\U0001F373'),  # 🍳
    ('Ice Cream', '\U0001F366'),  # 🍦
    ('Fruits', '\U0001F349'),  # 🍉
    ('Coffee', '\u2615'),  # ☕
    ('Steak', '\U0001F969'),  # 🥩
    ('Soup', '\U0001F35C'),  # 🍜
    ('Tacos', '\U0001F32E'),  # 🌮
    ('Donuts', '\U0001F369'),  # 🍩
    ('Cookies', '\U0001F36A'),  # 🍪
    ('Popcorn', '\U0001F37F'),  # 🍿
    ('Sandwich', '\U0001F96A'),  # 🥪
    ('Chicken', '\U0001F357'),  # 🍗
    ('Beer', '\U0001F37A'),  # 🍺
    ('Wine', '\U0001F377'),  # 🍷
    ('Cocktails', '\U0001F378'),  # 🍹
]
    name = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.icon}"
    

    def save(self,*args,**kwargs):
        # Automatically set the icon based on the selected name
        if not self.icon:  # If the icon field is empty, set it
            self.icon = dict(self.CATEGORY_CHOICES).get(self.name)

        super().save(*args,**kwargs)