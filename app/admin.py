from django.contrib import admin
from app.models import Account
# Register your models here.

@admin.register(Account)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("email", "number", "product_key", "date_created")
