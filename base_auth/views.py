from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from authentication import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .token import generate_token
from .models import User_Profile

# Create your views here.
def home(request):
    return render(request,'base_auth/index.html')

def about(request):
    return render(request,'base_auth/about.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pword1 = request.POST['pword']
        pword2 = request.POST['cpword']
        if pword1 != pword2:
            messages.error(request,"Passwords do not match")
            return redirect('signup_page')
        
        myuser = User.objects.create_user(uname,email,pword1)
        myuser.is_active = False
        myuser.save()
        messages.success(request,'Successfully regesterd ,We have sent you a confirmation mail.Please activate your account by clicking it')

        # Welcome  Email
        subject = "Welcome to CustomerConnect CRM"
        msg = "Thankyou for visiting our site \n Please activate your account by clicking the url in the confirmation email \n We have sent you a confirmation email"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, msg, from_email, to_list, fail_silently=True)


        # Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your email #CustomerConnect CRM"
        msg2 = render_to_string('base_auth/email_confirmation.html',{
            'name': myuser.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        mail = EmailMessage(
            email_subject,
            msg2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        mail.fail_silently = True
        mail.send()

        return redirect('signin_page')

    return render(request,'base_auth/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pword']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'base_auth/index.html',{
                'user':request.user
            })
        else:
            messages.error(request,'bad credentials')
            return redirect('homepage')

    return render(request,'base_auth/signin.html')

def signout(request):
    logout(request)
    return redirect('homepage')

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)   
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        myuser.save()
        User_Profile.objects.create(user=myuser)
        login(request,myuser)
        return redirect('homepage')
    else:
        return render(request,'base_auth/activation_failed.html')

