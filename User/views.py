from django.shortcuts import render,redirect
from Guest.models import *
from Shop.models import *
from User.models import *
from django.db.models import Sum
from datetime import date
from django.http import JsonResponse
# Create your views here.
def homepage(request):
    pro=tbl_product.objects.all()
    return render(request, 'User/Homepage.html',{'product':pro})

def myprofile(request):   
    user=tbl_user.objects.get(id=request.session['uid']) 
    return render(request,'User/profile.html',{'user':user})


def editprofile(request):
    editdata=tbl_user.objects.get(id=request.session['uid'])   
    if request.method=="POST":
        editdata.user_name=request.POST.get('txt_name')
        editdata.user_email=request.POST.get('txt_email')
        editdata.user_contact=request.POST.get('txt_contact')
        editdata.user_address=request.POST.get('txt_address')
        editdata.save()
        return redirect('User:edit')
    else:
        return render(request,"User/editprofile.html",{'edit':editdata}) 
    


def changepass(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    dbpass=user.user_password
    if request.method=="POST":
        oldpass=request.POST.get("txt_old")
        newpass=request.POST.get("txt_new")
        retype=request.POST.get("txt_retype")
        if dbpass==oldpass:
            if newpass==retype:
                user.user_password=newpass
                user.save()
                return redirect("User:myprofile")
            else:
                return render(request,'User/changepass.html',{"msg":"Password Mismatch"})   
        else:
            return render(request,'User/changepass.html',{"msg":"Password Invalid"})   
    else:
        return render(request,'User/changepass.html')  


def viewshop(request):
    district=tbl_district.objects.all()
    shop=tbl_shop.objects.all()
    return render(request, 'User/ViewShop.html',{'district':district,'shop':shop})

def viewproduct(request,id):
    category=tbl_category.objects.all()
    typ=tbl_type.objects.all()
    product=tbl_product.objects.filter(shop=id)
    return render(request, 'User/ViewProduct.html',{'category':category,'type':typ,'product':product,'id':id})

def ajaxsearchshop(request):
    district=request.GET.get("cid")
    place=request.GET.get("tid")
    if (district !="") :
        shop=tbl_shop.objects.filter(place__district=district)
    elif (place !="") :
        shop=tbl_shop.objects.filter(place=place)
    elif (district !="") & (place !=""):
        shop=tbl_shop.objects.filter(place=place,place__district=district)
    return render(request,"User/AjaxSearchShop.html",{'shop':shop})

def ajaxsearchproduct(request):
    category = request.GET.get("cid")
    type_id = request.GET.get("tid")
    shop_id = request.GET.get("sid") 
  
    if category and type_id: 
        pro = tbl_product.objects.filter(category=category, type_id=type_id, shop=shop_id)
        print(pro)
    elif category:  
        pro = tbl_product.objects.filter(category=category, shop=shop_id)
    elif type_id:  
        pro = tbl_product.objects.filter(type_id=type_id, shop=shop_id)
    else:  
        pro = tbl_product.objects.filter(shop=shop_id)

    return render(request, "User/AjaxSearchProduct.html", {'product': pro})



def searchproduct(request):
    keyword = request.GET.get('keyword', '')  # Get the keyword from the request
    print("Search Keyword:", keyword)  # Debug print
    products = tbl_product.objects.filter(product_name__icontains=keyword)  # Filter by product name
    return render(request, "User/ProductPage.html", {'products': products, 'keyword': keyword})


def addcart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"User/ViewProduct.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            msg="Added To cart"
            return render(request,"User/ViewProduct.html",{'msg':msg})
    else:
        bookingdata = tbl_booking.objects.create(user=userdata)
        tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
        msg="Added To cart"
        return render(request,"User/ViewProduct.html",{'msg':msg})


def Mycart(request):
    
    if request.method=="POST":
        bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
        cart = tbl_cart.objects.filter(booking=bookingdata)
        for i in cart:
            i.cart_status = 1
            i.save()
        bookingdata.booking_totalamount=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        return redirect("User:payment")
    else:
        bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
        
        if bookcount > 0:
            book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
            request.session["bookingid"] = book.id
            cart = tbl_cart.objects.filter(booking=book)
           


            
            for i in cart:
                typ=i.product.type_id
                rate=tbl_rate.objects.filter(type_id=typ).last()
                amt=rate.rate_amount
                # print(rate.rate_amount)
                
                total_stock = tbl_stock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_quantity'))['total']
                total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=0).aggregate(total=Sum('cart_quantity'))['total']
                # print(total_stock)
                # print(total_cart)
                if total_stock is None:
                    total_stock = 0
                if total_cart is None:
                    total_cart = 0
                total =  total_stock - total_cart
                i.total_stock = total
            return render(request,"User/MyCart.html",{'cartdata':cart,'amt':amt})
        else:
            return render(request,"User/MyCart.html")
    
        

def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:Mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_quantity=qty
   cartdata.save()
   return redirect("User:Mycart")  


def customization(request, id):
    customization=tbl_customization.objects.filter(user=request.session["uid"])
    typ=tbl_type.objects.all()
    category=tbl_category.objects.all()
    if request.method=="POST":
         tbl_customization.objects.create(
            customization_details=request.POST.get("txt_details"),
            types=tbl_type.objects.get(id=request.POST.get("sel_type")),
            customization_weight=request.POST.get("txt_weight"),
            category=tbl_category.objects.get(id=request.POST.get("sel_category")),
            user=tbl_user.objects.get(id=request.session['uid']),
            shop=tbl_shop.objects.get(id=id)
        )
         return redirect("User:customization",id)
    else:
        return render(request,"User/customization.html",{'category':category,'type':typ,'customization':customization,"id":id})

def customizationdelete(request, did,id):
    tbl_customization.objects.delete(id=did)
    return redirect("User:customization",id)



def payment(request):
   bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
   cart=tbl_booking.objects.get(booking=bookingdata)
   amt=boookingdata.booking_amount
   if request.method=="POST":
    cart.cart_status=2
    cart.save()
    bookingdata.booking_status=2
    bookingdata.save()
    return redirect("User:loader") 
   else:
    return render(request,"User/Payment.html",{'amt':amt})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def MyBooking(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    booking=tbl_booking.objects.filter(user=user,booking_status__gte=0)
    cartdata = []
    for booking_obj in booking:
        carts_for_booking = tbl_cart.objects.filter(booking=booking_obj)
        cartdata.extend(carts_for_booking)
    return render(request,'User/MyBooking.html',{'data':cartdata})


def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(shop=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(shop=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,shop=tbl_shop.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(shop=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(shop=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(shop=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def complaint(request):
    data=tbl_complaint.objects.filter(user=request.session['uid'])
    if request.method=="POST":
        file=request.FILES.get('txt_file')
        content=request.POST.get('txt_content')
        tbl_complaint.objects.create(complaint_file=file,complaint_description=content,user=tbl_user.objects.get(id=request.session['uid']))
        return render(request,"User/Complaint.html",{'data':data})

    else:
        return render(request,"User/Complaint.html",{'data':data})

def delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:complaint")

