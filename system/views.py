from django.shortcuts import render
from . models import Owners
from . models import Renter
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def landingPage(request):
    return render(request,'home.html')

def registerPage(request):

    if(request.method=="POST"):
        if(request.POST.get("register_owner")):
            fullname=request.POST['fullname']
            username=request.POST['username']
            email=request.POST['email']
            phone_no=request.POST['phoneNo']
            nid_no=request.POST['nid']
            address=request.POST['address']
            password=request.POST['password']

            try:
                new_owner=Owners.objects.create(
                fullname=fullname,username=username,email_id=email,
                phone_no=phone_no,nid_no=nid_no,address=address
            )
                new_owner.save()
                getMember=Owners.objects.get(username=username)
                if(User.objects.filter(email=getMember.email_id)):
                    messages.info(request,"You are already signed up!")
                else:
                    user=User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    
                    messages.info(request,"Registered as Owner")

            except:
                messages.info(request,"Database error occured")
        if(request.POST.get('register_renter')):
            print("hocche")
            
        else:
            return render(request,'register.html')
        
        # new_register=Login.objects.create(username=username,password=password)
        # new_register.save()
        

        if(request.POST.get("register_renter")):
            fullname=request.POST['fullname']
            username=request.POST['username']
            email=request.POST['email']
            phone_no=request.POST['phoneNo']
            nid_no=request.POST['nid']
            occupation=request.POST['occupation']
            password=request.POST['password']


            try:
                new_renter=Renter.objects.create(
                fullname=fullname,username=username,email_id=email,
                phone_no=phone_no,nid_no=nid_no,occupation=occupation
            )
                new_owner.save()
                getMember=Renter.objects.get(username=username)
                if(User.objects.filter(email=getMember.email_id)):
                        messages.info(request,"You are already signed up!")
                else:
                    user=User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    
                    messages.info(request,"Registered as renter")

            except:
                messages.info(request,"Database error occured")
        if(request.POST.get('register_owner')):
            print("hocche")
        
    return render(request,'register.html')
# ------------------------------------------------------------

def login(request):
    return render(request,'login.html')    
def rent_Post(request):
    return render(request,'rent_post.html') 
def rent_events(request):
    return render(request,'rent_events.html')
def admin_log(request):
    return render(request,'admin_log.html')

      