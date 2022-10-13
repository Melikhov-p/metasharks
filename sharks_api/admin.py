from django.contrib import admin
from .models import *

# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'color', 'date')


admin.site.register(Color, ColorAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Order, OrderAdmin)
