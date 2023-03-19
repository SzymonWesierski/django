from django.contrib import admin

from .models import Rentals, Books, CDs, Films

# Register your models here.

admin.site.register(Rentals)
admin.site.register(Books)
admin.site.register(CDs)
admin.site.register(Films)

