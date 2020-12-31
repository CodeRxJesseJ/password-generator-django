from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.


def home(request):
    return render(request, 'pass_gen/home.html',)


def password(request):
    characters = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    numbers = string.digits
    if request.GET.get('uppercase'):
        characters += uppercase
    if request.GET.get('number'):
        characters += (numbers)
    if request.GET.get('spl_chr'):
        characters += '~`!@#$%^&*()_-+={}[]:;<>,.?/|\\'
    length = int(request.GET.get('length', 12))
    thepassword = ''
    # characters = random.shuffle(list(characters))
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'pass_gen/password.html', {'password': thepassword})

def about(request):
    return render(request,'pass_gen/about.html',)
