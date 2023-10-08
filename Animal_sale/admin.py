from django.contrib import admin

from .models import Category1,Category2,Species1,Species2,Contact,Buy

class Category1Admin(admin.ModelAdmin):
      list_display=('title', 'createdAt')

class Category2Admin(admin.ModelAdmin):
      list_display=('title', 'createdAt')

class Species1Admin(admin.ModelAdmin):
      list_display=('title', 'createdAt')

class Species2Admin(admin.ModelAdmin):
      list_display=('title', 'createdAt')

class ContactAdmin(admin.ModelAdmin):
      list_display=('FirstName', 'LastName','Phone')

class BuyAdmin(admin.ModelAdmin):
      list_display=('YourName', 'Phone','AnimalCategory','AnimalBreed')




admin.site.register(Species1,Species1Admin)
admin.site.register(Species2,Species2Admin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Buy,BuyAdmin)


# Register your models here.
admin.site.register(Category1,Category1Admin)
admin.site.register(Category2,Category2Admin)
