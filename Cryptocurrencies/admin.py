from django.contrib import admin
from Cryptocurrencies.models import *

class CryptoAdmin(admin.ModelAdmin):
    list_display = ['name','symbol','price','updated'];
    list_editable = ['symbol','price']
    list_per_page = 10

admin.site.register(Crypto,CryptoAdmin)
