from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)\

class Product(models.Model):
    product_id = models.CharField(unique=True, max_length=255)
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Customer(models.Model):
    customer_id = models.CharField(unique=True, max_length=255)
    customer_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)

class Platform(models.Model):
    platform_name = models.CharField(max_length=100)

class Order(models.Model):
    order_id = models.CharField(unique=True, max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    selling_price = models.FloatField()
    delivery_status = models.CharField(max_length=50, choices=[
        ('Delivered', 'Delivered'),
        ('In Transit', 'In Transit'),
        ('Cancelled ', 'Cancelled'),
    ])

class FileUploader(models.Model):
    file = models.FileField(upload_to="files/")