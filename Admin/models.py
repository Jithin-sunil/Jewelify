from django.db import models

# Create your models here.
class tbl_district(models.Model):
       district_name=models.CharField(max_length=30)

class tbl_category(models.Model):
       category_name=models.CharField(max_length=30)  

class tbl_place(models.Model):
       district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
       place_name=models.CharField(max_length=30)  


       
class tbl_admin(models.Model):
       admin_name=models.CharField(max_length=30)    
       admin_email=models.CharField(max_length=30)   
       admin_password=models.CharField(max_length=30)    

class tbl_type(models.Model):
       type_name=models.CharField(max_length=30)

class tbl_rate(models.Model):
       rate_amount=models.CharField(max_length=30)
       rate_date=models.DateField(auto_now_add=True)
       type_id=models.ForeignKey(tbl_type,on_delete=models.CASCADE)


