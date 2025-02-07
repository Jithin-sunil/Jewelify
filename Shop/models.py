from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_product(models.Model):
    product_name=models.CharField(max_length=50)
    product_size=models.CharField(max_length=50)
    product_makingprice=models.CharField(max_length=50)
    product_weight=models.CharField(max_length=50)
    product_photo=models.FileField(upload_to="Assets/Shop/")
    product_details=models.CharField(max_length=100)
    type_id=models.ForeignKey(tbl_type,on_delete=models.CASCADE)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)


class tbl_stock(models.Model):
    stock_date=models.DateField(auto_now_add=True)
    stock_quantity=models.CharField(max_length=50)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    