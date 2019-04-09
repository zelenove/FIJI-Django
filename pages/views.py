from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def brothers(request):
    return render(request, "brothers.html", {})

def faq(request):
    return render(request, "faq.html", {})

def login(request):
    return render(request, "login.html", {})

def contact(request):
    return render(request, "contact.html", {})