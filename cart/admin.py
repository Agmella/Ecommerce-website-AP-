from django.contrib import admin
from .models import product, transaction, order, User


# Register your models here.
admin.site.register(product)
admin.site.register(transaction)
admin.site.register(order)
admin.site.register(User)
