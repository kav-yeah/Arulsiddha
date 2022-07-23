from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic import ListView
from django.core.mail import send_mail
# Create your views here.
def home(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
    
    if form.is_valid():
        subject = form.cleaned_data['subject']
        email= form.cleaned_data['email_address']
        message=form.cleaned_data['message'] 
        send_mail(subject, message, email, ['kavyayasotha@gmail.com']) 
    return render(request, "home.html",{'form':form})
    # if form.is_valid():
    # subject = form.cleaned_data['subject']
    # message = form.cleaned_data['message']
    # sender = form.cleaned_data['sender']
    # cc_myself = form.cleaned_data['cc_myself']

    # recipients = ['info@example.com']
    # if cc_myself:
    #     recipients.append(sender)

    # send_mail(subject, message, sender, recipients)
    # return HttpResponseRedirect('/thanks/')

def service(request):
    return render(request, "services.html")

