from django.db import models
from Guest.models import *
from Shop.models import *
# Create your models here.
class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_status=models.IntegerField(default=0)
    booking_amount=models.CharField(max_length=20)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_cart(models.Model):
    cart_quantity=models.IntegerField(default=1)
    cart_status=models.IntegerField(default=0)
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)


class tbl_customization(models.Model):   
       customization_details=models.CharField(max_length=30)      
       customization_weight=models.CharField(max_length=30)      
       types=models.ForeignKey(tbl_type,on_delete=models.CASCADE) 
       category=models.ForeignKey(tbl_category,on_delete=models.CASCADE) 
       user=models.ForeignKey(tbl_user,on_delete=models.CASCADE) 
       customization_status=models.IntegerField(default=0)   
       shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE) 
       customization_date=models.DateField(auto_now_add=True)    
       customization_amount = models.CharField(max_length=50)

class tbl_complaint(models.Model):
       complaint_date=models.DateField(auto_now_add=True)  
       complaint_replay=models.CharField(max_length=30)     
       complaint_status=models.IntegerField(default=0) 
       user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)   
       complaint_file=models.FileField(upload_to="Assets/UserDocs/")
       complaint_description=models.CharField(max_length=30) 

class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)  



class tbl_point(models.Model):
        point_value=models.CharField(max_length=30)     
        point_status=models.CharField(max_length=30)  
        user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)        



class tbl_wishlist(models.Model):
    wishlist_date=models.CharField(max_length=30)  
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)   
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)   

   

             
             
    
         
      
    