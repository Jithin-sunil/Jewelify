from django.db import models
from Guest.models import *
from Admin.models import *


class tbl_user(models.Model):
       user_name=models.CharField(max_length=30)    
       user_email=models.CharField(max_length=30)   
       user_address=models.CharField(max_length=30)   
       user_contact=models.CharField(max_length=30)  
       user_gender=models.CharField(max_length=30) 
       user_password=models.CharField(max_length=30)    
       user_dob=models.DateField()   
       place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
       user_photo=models.FileField(upload_to="Assets/UserDocs/")


class tbl_shop(models.Model):
       shop_name=models.CharField(max_length=30)    
       shop_email=models.CharField(max_length=30)      
       shop_contact=models.CharField(max_length=30)
       shop_proof=models.FileField(upload_to="Assets/UserDocs/")
       shop_photo=models.FileField(upload_to="Assets/UserDocs/")
       place=models.ForeignKey(tbl_place,on_delete=models.CASCADE) 
       shop_status=models.CharField(max_length=30)     
       shop_address=models.CharField(max_length=30)  
       shop_password=models.CharField(max_length=30) 


       

