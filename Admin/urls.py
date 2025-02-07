from django.urls import path,include
from Admin import views
app_name='Admin'

urlpatterns = [
     path('District/',views.District,name="District"),
     path('deldistrict/<int:did>',views.deldistrict,name="deldistrict"),
     path('editdistrict/<int:eid>',views.editdistrict,name="editdistrict"),

     path('Catagory/',views.Catagory,name="Catagory"),
     path('delcatagory/<int:did>',views.delcatagory,name="delcatagory"),
     path('editcatagory/<int:eid>',views.editcatagory,name="editcatagory"),


     path('Place/',views.place,name="Place"),
     path('delplace/<int:did>',views.delplace,name="delplace"),
     path('editplace/<int:eid>',views.editplace,name="editplace"),


     
     path('adminreg/',views.adminreg,name="adminreg"),
     path('Adminhome/',views.Adminhome,name="Adminhome"),
   
      path('Type/',views.Type,name="Type"),
     path('deltype/<int:did>',views.deltype,name="deltype"),
     path('edittype/<int:eid>',views.edittype,name="edittype"),

      path('rate/',views.rate,name="rate"),
     path('delrate/<int:did>',views.delrate,name="delrate"),
     path('editrate/<int:eid>',views.editrate,name="editrate"),

     path('ViewComplaint/',views.viewcomplaint,name="viewcomplaint"),
     path('Reply/<int:id>',views.reply,name="reply"),

     path('shopverification/',views.shopverification,name="shopverification"),
     path('accept/<int:id>',views.accept,name="accept"),
     path('reject/<int:id>',views.reject,name="reject"),

     path('userlist/',views.userlist,name="userlist"),




]