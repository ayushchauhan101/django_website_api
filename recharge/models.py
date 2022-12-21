from django.db import models


days_valid = [
    # stored in the DB , human readable info
    ('28', 'month pack'),
    ('56', 'two months pack'),
    ('84', 'three months pack'),
    ('180', 'half yearly pack'),
    ('365', 'yearly pack'),
    ('70', 'special pack 1'),
]


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    validity = models.CharField(max_length=3, choices=days_valid, default=28)
    daily_internet = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"The recharge pack named: {self.name} of price {self.price} was created."
