from django.db import models
from accounts.models import Profile
from products.models import Product
from django.apps import apps
from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import BaseUser


# Create your models here.
class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    completed = models.BooleanField(default=False)

    #date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.user.first_name


@receiver(post_save, sender=Profile)
def create_user_cart(sender, created, instance, *args, **kwargs):
    if created:
        Cart.objects.create(profile=instance)
    # @property
    # def totalcart(self):
    #     total = self.cart.cartitems.all()
    #     return total

    # @property
    # def total_cartitem(self):
    #     cartitem = self.cart.cartitems.all()
    #     total = sum([item.quantity for item in cartitem])
    #     return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems', null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='producitems', null=True)
    quantity = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"cartitem -{str(self.quantity)}"
