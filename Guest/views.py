from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *


# Create your views here.
def signup(request):
    district=tbl_district.objects.all()
    if request.method == "POST":
        name = request.POST.get("txt_name")
        address = request.POST.get("txt_address")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        gender = request.POST.get("txt_gender")
        place_id=tbl_place.objects.get(id=request.POST.get("selplace"))
        password = request.POST.get("txt_password")
        print(password)
        photo=request.FILES.get("filephoto")
        dob = request.POST.get('txt_date')
        tbl_user.objects.create(
            user_name=name,
            user_address=address,
            user_email=email,
            user_contact=contact,
            place=place_id,
            user_gender=gender,
            user_password=password, 
            user_dob=dob,
            user_photo=photo
        )
        return render(request, "Guest/Signup.html")
    else:
        return render(request, "Guest/Signup.html", {'dis':district})

def ajaxplace(request):
    district=tbl_district.objects.get(id=request.GET.get("did"))
    place=tbl_place.objects.filter(district=district)
    return render(request,'Guest/AjaxPlace.html',{'plc':place})



def login(request):
    if request.method == "POST":   
        email=request.POST.get('txt_email') 
        password=request.POST.get('txt_password')
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        shopcount=tbl_shop.objects.filter(shop_email=email,shop_password=password).count()

        if usercount>0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=user.id
            return redirect('User:homepage')
        elif admincount>0:
            admin=tbl_admin.objects.get(admin_email=email, admin_password=password)
            request.session['aid']=admin.id
            return redirect('Admin:Adminhome')
        elif shopcount>0:
            shop=tbl_shop.objects.get(shop_email=email,shop_password=password)
            request.session['sid']=shop.id
            return redirect('Shop:homepage') 
        else:
            return render(request, "Guest/login.html")
    else:
        return render(request, "Guest/login.html")


def shop(request):
    district=tbl_district.objects.all()
    if request.method == "POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        address = request.POST.get("txt_address")
        place_id=tbl_place.objects.get(id=request.POST.get("selplace"))
        photo=request.FILES.get("filephoto")
        proof=request.FILES.get("fileproof")
        password = request.POST.get("txt_password")
        print(password)
        tbl_shop.objects.create(
            shop_name=name,
            shop_email=email,
            shop_contact=contact,
            shop_proof=proof,
            shop_photo=photo,
            place=place_id,
            shop_address=address,
            shop_password=password, 
        )
        return render(request, "Guest/Shop.html")
    else:
        return render(request, "Guest/Shop.html", {'dis':district})     


def index(request):
    if request.method == "POST":
        return render(request, "Guest/index.html")
    else:
        return render(request, "Guest/index.html")

 


