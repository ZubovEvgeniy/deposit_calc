from django.db import models


class Deposit(models.Model):
    date = models.DateField(auto_now_add=True)
    periods = models.IntegerField()
    amount = models.IntegerField()
    rate = models.FloatField()

    def __str__(self):
        return self.name
