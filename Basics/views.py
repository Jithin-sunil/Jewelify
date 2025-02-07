from django.shortcuts import render

# Create your views here.
def add(request):
    if request.method=="POST":
        number1=int(request.POST.get("txt_number1"))
        number2=int(request.POST.get("txt_number2"))
        result=number1 + number2
        return render(request,"Basics/Add.html",{'sum':result})
    else:
        return render(request,"Basics/Add.html")
        

def Calculator(request):
    if request.method=="POST":
        number1=int(request.POST.get("txt_number1"))
        number2=int(request.POST.get("txt_number2"))
        btn=request.POST.get('btnlog')
        if btn=='+':
            result=number1 + number2
        elif btn=='-':
            result=number1 - number2
        elif btn=='*':
            result=number1 * number2
        elif btn=='/':
            result=(number1 / number2)
        return render(request,"Basics/Calculator.html",{'sum':result})
    else:
     
        return render(request,"Basics/Calculator.html")


def Largest(request):  
        if request.method=="POST":
            number1=int(request.POST.get("txt_number1"))
            number2=int(request.POST.get("txt_number2")) 
            number3=int(request.POST.get("txt_number3"))
            if number1>=number2 and number1>=number3:
                result=number1
            elif number2>number3 and number2>=number1:
                result=number2
            elif number3>number1 and number3>=number2:
                result=number3
            return render(request,"Basics/Largest.html",{'sum':result})
        else:
            return render(request,"Basics/Largest.html",{'sum':result})


def OddorEven(request):
    if request.method=="POST":
        number=int(request.POST.get("text_number"))
        if number % 2 == 0:
            result="Even"
        else:
            result="odd" 
        return render(request,"Basics/OddorEven.html",{'sum':result})
                
    else:
        return render(request,"Basics/OddorEven.html")





            
    
             
         

