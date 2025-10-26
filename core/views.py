from django.shortcuts import render, redirect
from django.views import View
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Gallery

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):

        context = {
        }

        return render(request, 'core/home.html', context)
    

class ServiceView(View):
    def get(self, request, *args, **kwargs):

        context = {
        }

        return render(request, 'core/services.html', context)
    

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
    
        template = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        })

        emailSender = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['jdmzacdeveloper@gmail.com']
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()

        messages.success(request, 'El correo electrónico se envió correctamente')

        return redirect('core:contact')
    return render(request, 'contact.html')


class GalleryView(View):
    def get(self, request, *args, **kwargs):
        jobs = Gallery.objects.all()

        context = {
            'jobs': jobs
        }

        return render(request, 'core/gallery.html', context)