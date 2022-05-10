from django.shortcuts import render, redirect
from .forms import ContactForm, SnippetForm
from .models import Snippet

# Create your views here.

my_contacts = []

def index(request):
    context = {
        'contacts': my_contacts,
        'i': len(my_contacts),
        'snippets': Snippet.objects.all()
    }
    return render(request, 'index.html', context)


def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            category = form.cleaned_data['category']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            
            my_contacts.append([fname, lname, email, category, subject, body])
            return redirect('home')
            
    
    context = {
        'form': ContactForm
    }
    return render(request, 'contact.html', context)

def snippet(request):
    
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    
    context = {
        'form': SnippetForm
    }
    return render(request, 'snippet.html', context)