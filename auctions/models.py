from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    img_url = models.CharField(max_length=256)
    category = models.CharField(max_length=64)
    date = models.DateTimeField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.title} \n {self.description} \n {self.img_url} \n {self.category} \n {self.date} \n {self.price}"


class Bid(models.Model):
    bid = models.FloatField()
    title = models.CharField(max_length=64)
    prod_id = models.IntegerField()
    user = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user} \n {self.title} \n {self.prod_id} \n {self.bid}"


class Comment(models.Model):
    comment = models.CharField(max_length=256)
    user = models.CharField(max_length=64)
    prod_id = models.IntegerField()
    date = models.DateTimeField()
    #
    # def __str__(self):
    #     return f"USER:{self.user}" \
    #            f" \nComment: {self.comment}" \
    #            f" \nProduct id: {self.prod_id}" \
    #            f" \nDate: {self.date}\n"


class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    prod_id = models.IntegerField()

    def __str__(self):
        return f"User: {self.user} \n Product id: {self.prod_id}\n"


class Winner(models.Model):
    owner = models.CharField(max_length=64)
    winner = models.CharField(max_length=64)
    prod_id = models.IntegerField()
    winprice = models.IntegerField()
    title = models.CharField(max_length=64, null=True)