from django.shortcuts import render,HttpResponse
from.models import product,customer,cart,orders
from django.contrib.auth.hashers import make_password,check_password
from datetime import date
from django.contrib.auth.hashers import make_password,check_password
import razorpay
from django.conf import settings

# Create your views here.


def Addcustomer(request):
    if request.method=='POST':
        emailId=request.POST['emailId']
        custname=request.POST['custname']
        password=request.POST['password']
        passw = make_password(password)
        contact_No=request.POST['contact_No']

        data=customer.objects.create(emailId=emailId,custname=custname,password=passw,contact_No=contact_No)
        data.save()

        return HttpResponse("Customer added  Successfully")
    else:
        return render(request,'component/addcustomer.html')


def getallproduct(request):
    data=product.objects.all()
    return render(request,'component/productlist.html',{"product":data})





def addcart(request,pid):
    product_obj=product.objects.get(pid=pid)
    emailId='q@gmail.com'
    cust_obj=customer.objects.get(emailId=emailId)
    quantity=1
    totalprice=product_obj.price*quantity
    data=cart.objects.create(product_obj=product_obj,cust_obj=cust_obj,quantity=quantity,totalprice=totalprice)
    data.save()
    return HttpResponse("Add to cart successfully")

 
def deletecart(request,id):
    product_obj=cart.objects.get(id=id)
    product_obj.delete()
    return HttpResponse("Removed form Cart  successfully")


def showcart(request):
    cust_obj='q@gmail.com'
    data=customer.objects.get(emailId=cust_obj)
    data=cart.objects.filter(cust_obj=data)
    return render(request,'component/cart.html',{'cart':data})



from datetime import date
from django.conf import settings
import razorpay
from django.http import HttpResponse
from django.shortcuts import render
from .models import customer, cart, orders

def showorderform(request):
    if request.method == 'POST':
        emailId = 'q@gmail.com'
 
        customer_data = customer.objects.get(emailId=emailId)
        
         
        cart_items = cart.objects.filter(cust_obj=customer_data)
        
         
        totalbill = sum(item.totalprice for item in cart_items)
        
         
        name = request.POST.get('name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        phoneno = request.POST.get('phoneno')

         
        if not all([name, address, city, state, pincode, phoneno]):
            return render(request, 'component/order.html', {'error': 'All fields are required.'})

        
        order_data = orders.objects.create(
            emailId=emailId,
            name=name,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            phoneno=phoneno,
            totalbillamount=totalbill
        )

         
        today = date.today().strftime('%Y%m%d')   
        order_number = f"{order_data.id}{today}"
        order_data.ordernumber = order_number
        order_data.save()

         
        order_data = orders.objects.get(emailId=emailId, ordernumber=order_number)
        
        
        razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        
        currency = 'INR'
        amount = totalbill * 100   

      
        razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

       
        razorpay_order_id = razorpay_order['id']

       
        context = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_merchant_key': settings.RAZORPAY_KEY_ID,
            'razorpay_amount': amount,
            'currency': currency
        }

      
        return render(request, 'component/Payment.html', {'orderobj': order_data, 'totalbill': totalbill, 'context': context})

    else:
        
        return render(request, 'component/order.html')




def login(request):
    if request.method == 'POST':
        emailId = request.POST['email']
        password = request.POST['password']
        
        
        user_type = 'user'  

        if user_type == 'user':
            try:
                cust = customer.objects.get(emailId=emailId)
                if cust:
                    if check_password(password, cust.password):
                        request.session['username'] = emailId
                        return render(request,"component/index.html")  
                    else:
                        return render(request, "component/login.html", {'error': 'Wrong password'})
            except customer.DoesNotExist:
                return render(request, "component/login.html", {'error': 'User does not exist'})
    
   
    return render(request, "component/login.html")



def logout(request):
    session_key=list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return render(request,"component/index.html")


def payment(request):
    return render(request,'component/Payment.html')

def paysucc(request,oid,pid):
    return render(request,'component/PaymentSuccss.html')




def index(request):
    return render(request,'component/index.html')


def About(request):
    return render(request,'component/About.html')
