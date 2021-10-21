from django.shortcuts import render
from .models import * 
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages



# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
    try:
        if Email.objects.filter(email = email).first():
            
            messages.success(request, 'Already Submitted')
        else:
            Email_obj = Email.objects.create(name= name, email = email)
            Email_obj.save()
            messages.success(request, 'Your Email has been successfully submitted.')
            send_email(email,name)
            print(f'{name}, had submitted his/her email {email}')
    except Exception as e:
        print(e)

    return render(request,"konera/index.html")


def send_email(email,name):
    subject = f'Congratulations! {name}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    html_message = render_to_string('konera/email.html',{'name': name})
    plain_message = strip_tags(html_message)
    send_mail(subject, plain_message , email_from ,recipient_list,html_message=html_message)

