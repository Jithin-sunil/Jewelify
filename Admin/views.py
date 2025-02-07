from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
# Create your views here.
def District(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_district")
        tbl_district.objects.create(district_name=name)
        return render(request,"Admin/District.html",{'data':data})
                
    else:
        return render(request,"Admin/District.html",{'data':data})
        
    
def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')

def editdistrict(request,eid):
    editdata=tbl_district.objects.get(id=eid)   
    if request.method=="POST":
        editdata.district_name=request.POST.get('txt_district')
        editdata.save()
        return redirect('Admin:District')
    else:
        return render(request,"Admin/District.html",{'edit':editdata})

def Catagory (request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_cat")
        tbl_category.objects.create(category_name=name)
        return render(request,"Admin/Catagory.html",{'data':data})
                
    else:
        return render(request,"Admin/Catagory.html",{'data':data})        

def delcatagory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect('Admin:Catagory')

def editcatagory(request,eid):
    editdata=tbl_category.objects.get(id=eid)   
    if request.method=="POST":
        editdata.category_name=request.POST.get('txt_cat')
        editdata.save()
        return redirect('Admin:Catagory')
    else:
        return render(request,"Admin/Catagory.html",{'edit':editdata})


def place(request): 
    dis=tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_place")
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=name,district=district)
        return render(request,"Admin/place.html",{'data':data,'district':dis})
    else:
         return render(request,"Admin/place.html",{'data':data,'district':dis}) 
def delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('Admin:Place')
def editplace(request,eid):
    dis=tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)   
    if request.method=="POST":
        editdata.place_name=request.POST.get('txt_place')
        editdata.district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.save()
        return redirect('Admin:Place')
    else:
        return render(request,"Admin/Place.html",{'edit':editdata,'district':dis})




def adminreg(request):
    
    if request.method == "POST":

        tbl_admin.objects.create(
            admin_name=request.POST.get("txt_name"),
            
            admin_email=request.POST.get("txt_email"),
           
            admin_password=request.POST.get("txt_password"), 
              
        )
        return render(request, "Admin/adminreg.html",{'msg':"Data Inserted"})
    else:
        return render(request, "Admin/adminreg.html")         





def Adminhome(request):
    return render(request,"Admin/Adminhome.html")
    

def Type(request):
    data=tbl_type.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_type")
        tbl_type.objects.create(type_name=name)
        return render(request,"Admin/Type.html",{'data':data})
                
    else:
        return render(request,"Admin/Type.html",{'data':data})
        
    
def deltype(request,did):
    tbl_type.objects.get(id=did).delete()
    return redirect('Admin:Type')

def edittype(request,eid):
    editdata=tbl_type.objects.get(id=eid)   
    if request.method=="POST":
        editdata.type_name=request.POST.get('txt_type')
        editdata.save()
        return redirect('Admin:Type')
    else:
        return render(request,"Admin/Type.html",{'edit':editdata})

 
def rate (request):
    typ=tbl_type.objects.all()
    data=tbl_rate.objects.all()
    if request.method=="POST":
        amount=request.POST.get("txt_amount")
        type_id=tbl_type.objects.get(id=request.POST.get("sel_type"))
        tbl_rate.objects.create(rate_amount=amount,type_id=type_id)
        return redirect("Admin:rate")
    else:
        return render(request,"Admin/Rate.html",{'data':data,'type':typ})  

def delrate(request,did):
    tbl_rate.objects.get(id=did).delete()
    return redirect('Admin:rate')

def editrate(request,eid):
    typ=tbl_type.objects.all()
    editdata=tbl_rate.objects.get(id=eid)   
    if request.method=="POST":
        editdata.rate_amount=request.POST.get('txt_amount')
        editdata.type_id=tbl_type.objects.get(id=request.POST.get("sel_type"))
        editdata.save()
        return redirect('Admin:rate')
    else:
        return render(request,"Admin/Rate.html",{'edit':editdata,'type':typ})  

def viewcomplaint(request):
    user = tbl_user.objects.all()
    usercom = tbl_complaint.objects.filter(user__in=user,complaint_status=0)
    userrep = tbl_complaint.objects.filter(user__in=user,complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{"user":usercom,'userrep':userrep})

def reply(request,id):
    com = tbl_complaint.objects.get(id=id)
    if request.method == "POST":
        com.complaint_status = 1
        com.complaint_replay = request.POST.get("txt_reply")
        com.save()
        return redirect("Admin:viewcomplaint")
    else:
        return render(request,"Admin/Reply.html")


def shopverification(request):
    shop = tbl_shop.objects.all()
    shopver = tbl_shop.objects.filter(shop_status=1)
    shoprep = tbl_shop.objects.filter(shop_status=2)
    return render(request,"Admin/ShopVerification.html",{"verified":shopver,'reject':shoprep,'data':shop})


def accept(request,id):
    shop = tbl_shop.objects.get(id=id)
    shop.shop_status = 1
    shop.save()
    return redirect("Admin:shopverification")

def reject(request,id):
    shop = tbl_shop.objects.get(id=id)
    shop.shop_status = 2
    shop.save()
    return redirect("Admin:shopverification")

def userlist(request):
    user = tbl_user.objects.all()
    return render(request,"Admin/UserList.html",{"data":user})