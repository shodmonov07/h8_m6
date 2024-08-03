from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=0)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value, null=True, blank=True)
    discount = models.PositiveSmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100))
        return self.price

    def __str__(self):
        return self.name
