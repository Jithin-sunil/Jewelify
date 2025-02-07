from django.urls import path,include
from Shop import views
app_name="Shop"
urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('editshop/',views.editshop,name='editshop'),
    path('shopchangepass/',views.shopchangepass,name='shopchangepass'),
    path('shopprofile/',views.shopprofile,name='shopprofile'),
    path('product/',views.product,name='product'),
    path('stock/<int:id>',views.Stock,name='stock'),
    path('delstock/<int:id>',views.delstock,name='delstock'),

    path('viewrate/',views.viewrate,name='viewrate'),
    path('viewbooking/',views.viewbooking,name='viewbooking'),
    path('orderstatus/<int:id>/<int:sts>',views.orderstatus,name='orderstatus'),
    
   
   
]

