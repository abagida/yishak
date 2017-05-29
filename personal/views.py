from django.shortcuts import render
from django.http import HttpResponse
from personal.forms import ThingForm
from personal.models import Thing
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from personal.forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def index(request):
    return render(request, 'personal/home.html')


def about(request):
    return render(request, 'personal/about.html')


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

        # Email the profile with the 
        # contact information
            template = get_template('personal/contact_template.txt')
            context = Context({'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content, })

            content = template.render(context)

            email = EmailMessage("New submission", content, "http://yishak.herokuapp.com" + '', ['yishak21@gmail.com'], headers={'Reply-To': contact_email})

            email.send()

            return redirect('contact')

    return render(request, 'personal/contact.html', {'form': form_class, })


def ui(request):
    return render(request, 'personal/ui.html')


def frontend(request):
    return render(request, 'personal/frontend.html')


def backend(request):
    return render(request, 'personal/backend.html')


def projects(request):
    return render(request, 'personal/projects.html')
