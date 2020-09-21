from django.shortcuts import render,HttpResponse
from datetime import datetime
from App.common.models import Enroll
from django.core.mail import send_mail, send_mass_mail
# Create your views here.
from django.views.generic import TemplateView
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
def enroll(request):
    if request.method=="POST":
        name = request.POST.get('Name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course= request.POST.get('course')
        message = request.POST.get('message') 
        send_mail(
            'Subject - Enrollment successfully Done', 
            'Hello ' + name + ',\n' + 'Thankyou for enrolling with us Hope you will Enjoy learning with us.\n For more details about batches contact on given numbers.\n 8999519331', 
            'jainaish@gmail.com', # Admin
            [
                email,
            ])
        en = Enroll(name=name, email=email, phone=phone, course=course,message=message,date= datetime.today())
        en.save()
        messages.success(request, 'Your enrollment has be submitted!\n You will get an confirmation mail')
    return render(request,'enroll.html')
def contact(request):
    return render(request,'contact.html')
def team(request):
    return render(request,'team.html')
def batch(request):
    return render(request,'batch.html')


