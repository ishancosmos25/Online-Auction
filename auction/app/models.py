import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.IntegerField(validators=[MinValueValidator(1)],default=0,  null=True)
#    def __str__(self):
#        return self.user.username


class Product(models.Model):

#    user = models.ForeignKey(Bids,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    desp = models.TextField(max_length=500, blank=False, null=True)
    image = models.ImageField(upload_to='../static/images/', blank=True,null=True)
    category = models.CharField(max_length=50, blank=True,null=True)
    minimum_price = models.IntegerField(blank=True, validators=[MinValueValidator(1)],default=1)
    start = models.DateTimeField(default=timezone.now(), null=True)
    end_date = models.DateTimeField(default=datetime.date.today() + datetime.timedelta(days=1))
    #end_time = models.TimeField(blank=True, null=True)
    current_bid = models.IntegerField(default=0)
    buy_product = models.ForeignKey(Bids, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Bidsmade(models.Model):
#
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     bidder_name = models.CharField(max_length=30, blank=False)
#     bid_time = models.TimeField(timezone.now())
#     bid_amount = models.DecimalField(max_digits=10,decimal_places=2)
#
#     def __str__(self):
#         return self.product.name

