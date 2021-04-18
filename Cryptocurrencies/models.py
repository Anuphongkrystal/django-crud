from django.db import models

class Crypto(models.Model):
    name = models.CharField(max_length=255,unique=True)
    symbol = models.CharField(max_length=30,unique=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to = "crypto",default="crypto/default.jpg",blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cryptocurrencies'
        verbose_name_plural = "Cryptocurrencies"
