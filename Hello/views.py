from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from Hello.models import Contact,Detail
from django.db.models import Q
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


def index(request):
    
    subject = 'Testing Email',
    from_email ='kumarsumit120919@gmail.com'
    to = 'mksumit1209@gmail.com'
    msg= '<p>Welcome to <strong>Book stroe </strong>, please read.</p>'
    msg = EmailMultiAlternatives(subject, msg, from_email, [to])
    msg.content_subtype='html'
    msg.send()
    
 #   send_mail(
 #   'Testing Email',
 #   'hii , how are you',
 #   'kumarsumit120919@gmail.com',
 #  ['mksumit1209@gmail.com'],
 #   fail_silently=False,
#)
    
    abc=Detail.objects.all()
    context={
        'xyz': abc
    }
    return render(request, 'index.html',context)


def about(request):

    return render(request, 'about.html')


def services(request):
    
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'contact.html')
# for search button

def search (request):
    if request.method =='POST':
        nameName=request.POST['nameName']

        stu=Detail.objects.all()
        if nameName :
            stu=stu.filter(Q(subject__icontains=nameName) | Q(writer__icontains=nameName) | Q(publication__icontains=nameName))
        
        context={
            'stu':stu 
        }
        return render(request, 'index.html',context)
    
    return HttpResponse('doesnot search')
 #-------------------------------login logout registration----------------------------------   

def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email_id=request.POST["email_id"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"usernmse already registerd")
                return redirect('/')
            elif User.objects.filter(email=email_id).exists():
                messages.info (request,"Email_id already registered")
                return redirect('/')


            else:
                xyz=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email_id,password=pass1,last_login=datetime.now())
                xyz.save()
                print("registration done")
                return redirect('login')
        else:
            print("password doesn't matched")
            messages.info (request,"password doesn't matched")

        return redirect("/")

def login(request):
    if request.method=="POST":
        username_1=request.POST["username2"]
        password_1=request.POST["password2"]

        uvw=auth.authenticate(username=username_1,password=password_1)

        if uvw is not None:
            auth.login(request,uvw)
            return redirect ('/')
        else:
            messages.error(request,"invalid credentials")
            return redirect("login")
        
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')

