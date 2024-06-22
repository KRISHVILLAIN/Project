from django.contrib import admin

from .models import Register_model, order_model, driver_model


# Register your models here.
@admin.register(Register_model)
class Register_model(admin.ModelAdmin):
    list_display = ['id', 'c_name', 'c_model', 'c_am', 'c_price', 'file']


@admin.register(driver_model)
class driver_model(admin.ModelAdmin):
    list_display = ['id', 'first', 'last', 'dob', 'email', 'phone', 'aadhar', 'address']


@admin.register(order_model)
class order_model(admin.ModelAdmin):
    list_display = ['id', 'c_name', 'c_price', 'c_model', 'c_am', 'first', 'last', 'email', 'phone', 'address',
                    'aadhar', 'office', 'time', 'driver', 'from_date', 'to_date', 'days', 'passengers',
                    'payment_type', 'd_bill', 'bill']
