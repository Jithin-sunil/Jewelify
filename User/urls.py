from django.urls import path,include
from User import views
app_name="User"

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('myprofile/',views.myprofile,name='profile'),
    path('edit/',views.editprofile,name='edit'),
    path('changepass/',views.changepass,name='changepass'),
    path('viewproduct/<int:id>',views.viewproduct,name='viewproduct'),
     path('searchproduct/', views.searchproduct, name='searchproduct'),
    path('viewshop/',views.viewshop,name='viewshop'),
    path('ajaxsearchproduct/',views.ajaxsearchproduct,name='ajaxsearchproduct'),
    path('ajaxsearchshop/',views.ajaxsearchshop,name='ajaxsearchshop'),
    path('addcart/<int:pid>',views.addcart,name='addcart'),
    path('Mycart/',views.Mycart, name='Mycart'),   
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),
    path('customization/<int:id>',views.customization,name='customization'), 
    path('customizationdelete/<int:did>/<int:id>',views.customizationdelete,name='customizationdelete'), 

    path("payment/",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path('MyBooking/',views.MyBooking, name='MyBooking'),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('Complaint/',views.complaint,name="complaint"),
    path('delcomplaint/<int:did>',views.delcomplaint,name="delcomplaint"),
]