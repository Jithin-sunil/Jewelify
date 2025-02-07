from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Shop.models import *
from User.models import *

# Create your views here.
def homepage(request):
    return render(request, 'Shop/Homepage.html')
def editshop(request):
    editdata=tbl_shop.objects.get(id=request.session['sid'])   
    if request.method=="POST":
        editdata.shop_name=request.POST.get('txt_name')
        editdata.shop_email=request.POST.get('txt_email')
        editdata.shop_contact=request.POST.get('txt_contact')
        editdata.shop_address=request.POST.get('txt_address')
        editdata.save()
        return redirect('Shop:editshop')
    else:
        return render(request,"Shop/editshop.html",{'editshop':editdata}) 

def shopprofile(request):   
    shop=tbl_shop.objects.get(id=request.session['sid']) 
    return render(request,'Shop/Shopprofile.html',{'Shop':shop})        
    
def shopchangepass(request):
    shop=tbl_shop.objects.get(id=request.session['sid'])
    dbpass=shop.shop_password
    if request.method=="POST":
        oldpass=request.POST.get("txt_old")
        newpass=request.POST.get("txt_new")
        retype=request.POST.get("txt_retype")
        if dbpass==oldpass:
            if newpass==retype:
                shop.shop_password=newpass
                shop.save()
                return redirect("Shop:shopprofile")
            else:
                return render(request,'Shop/shopchangepass.html',{"msg":"Password Mismatch"})   
        else:
            return render(request,'Shop/shopchangepass.html',{"msg":"Password Invalid"})   
    else:
        return render(request,'Shop/shopchangepass.html')  

def product(request):
    category=tbl_category.objects.all()
    typ=tbl_type.objects.all()
    pro=tbl_product.objects.filter(shop=request.session['sid'])
    if request.method=="POST":
        tbl_product.objects.create(
            product_name=request.POST.get("txt_name"),
            product_size=request.POST.get("txt_size"),
            product_makingprice=request.POST.get("txt_makepirce"),
            product_weight=request.POST.get("txt_weight"),
            product_photo=request.FILES.get("file_photo"),
            product_details=request.POST.get("txt_details"),
            type_id=tbl_type.objects.get(id=request.POST.get("sel_type")),
            category=tbl_category.objects.get(id=request.POST.get("sel_category")),
            shop=tbl_shop.objects.get(id=request.session['sid'])
        )
        return redirect("Shop:product")
    else:
        return render(request,"Shop/Product.html",{'category':category,'type':typ,'product':pro})


def Stock(request,id):
    data=tbl_stock.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_stock")

        tbl_stock.objects.create(stock_quantity=name,product=tbl_product.objects.get(id=id))
        return render(request,"Shop/Stock.html",{'data':data})
                
    else:
        return render(request,"Shop/Stock.html",{'data':data})
        
    
def delstock(request,did):
    tbl_stock.objects.get(id=did).delete()
    return redirect('Shop:Stock')


def viewrate(request):
    rate=tbl_rate.objects.all()
    return render(request,'Shop/ViewRate.html',{'rate':rate})

def viewbooking(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    cartdata=tbl_cart.objects.filter(product__shop=shop)
    return render(request,'Shop/ViewBooking.html',{'data':cartdata})

def orderstatus(request,id,sts):
    cart=tbl_cart.objects.get(id=id)
    cart.cart_status=sts
    cart.save()
    return redirect("Shop:viewbooking")

def customizationrequest(request):
    shop=tbl_shop.objects.get(id=request.session["sid"])
    data=tbl_customization.objects.filter(shop=shop)
    return render(request,'Shop/CustomizationRequest.html',{'data':data})