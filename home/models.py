from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    desc=models.TextField(null=True, blank=True)

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.PositiveIntegerField()
    cat=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')