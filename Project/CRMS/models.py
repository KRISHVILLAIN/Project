from django.db import models


# Create your models here.
class Register_model(models.Model):
    c_name = models.CharField(max_length=50)
    c_model = models.CharField(max_length=50)
    c_am = models.CharField(max_length=10)
    c_price = models.CharField(max_length=50)
    file = models.FileField(upload_to="media/photo", default='0')


class order_model(models.Model):
    c_name = models.CharField(max_length=20,default='0')
    c_price = models.CharField(max_length=20,default='0')
    c_model = models.CharField(max_length=20,default='0')
    c_am = models.CharField(max_length=20,default='0')
    first = models.CharField(max_length=20,default='0')
    last = models.CharField(max_length=20,default='0')
    email = models.CharField(max_length=50,default='0')
    phone = models.CharField(max_length=10,default='0')
    address = models.CharField(max_length=100,default='0')
    aadhar = models.CharField(max_length=20,default='0')
    office = models.CharField(max_length=100,default='0')
    time = models.CharField(max_length=20,default='0')
    driver = models.CharField(max_length=20, default='0')
    from_date = models.CharField(max_length=20,default='0')
    to_date = models.CharField(max_length=20,default='0')
    days = models.CharField(max_length=20,default='0')
    passengers = models.CharField(max_length=20,default='0')
    payment_type = models.CharField(max_length=30,default='0')
    d_bill=models.CharField(max_length=30,default='0')
    bill = models.CharField(max_length=30,default='0')


class driver_model(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=20)
