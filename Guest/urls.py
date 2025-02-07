from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path('Signup/',views.signup,name="Signup"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('login/',views.login,name="login"),
    path('Shop/',views.shop,name="shop"),
    path('',views.index,name="Index"),


] 