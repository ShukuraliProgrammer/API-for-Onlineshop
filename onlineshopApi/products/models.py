from django.db import models
from accounts.models import Profile
from django.shortcuts import reverse


# Create your models here.

class Category(models.Model):
    LEVEL = {
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    }
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, db_index=True)
    description = models.CharField(max_length=150, null=True)
    # icon = models.
    slug = models.SlugField(max_length=800, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # updated = models.DateTimeField(auto_created=True)
    activate = models.BooleanField()
    level = models.CharField(max_length=200, choices=LEVEL, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_ancestors(self):
        if self.parent is None:
            return Category.objects.none()
        return Category.objects.filter(pk=self.parent.pk) | self.parent.get_ancestors()

    def __str__(self):
        return self.name if self.name else super.__str__()

    # 3- problem
    #     @property
    def total_product_quantity(self):
        total = self.products.count()
        return total

    def get_absolute_url(self):
        return reverse('shop:product',kwargs={
                       'slug': self.slug
        })


class Brand(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='images/brand/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Color(Brand):
    # icon = models.ImageField(upload_to='images/color/', null=True, blank=True)
    pass


class Product(models.Model):
    STATUS_CHOICE = (
        ('available', 'Sotuvga tayyor'),
        ('out of stock', 'Sotuvda qolmagan'),
        ('privet', "Hech kimda ko'rinmaydi"),
    )
    LABEL_CHOICE = (
        ('P', 'primary'),
        ('S', 'Secondary'),
        ('D', 'danger'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=4, verbose_name='price', null=True, blank=True)
    discount_price = models.FloatField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='product_brand')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, related_name='product_color')
    sold_count = models.PositiveIntegerField(null=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICE, default='private', max_length=30)
    available = models.BooleanField(default=True)
    label = models.CharField(max_length=1, choices=LABEL_CHOICE, null=True, blank=True)

    # color = models.ForeignKey(Color, models.SET_NULL)
    # quality = models.IntegerField()
    # solid = models.CharField(max_length=200, null=True, blank=True)
    # rating = models.IntegerField()
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse('products:product', kwargs={
            'slug': self.slug,
        })


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rating')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_rating')
    ball = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.ball
