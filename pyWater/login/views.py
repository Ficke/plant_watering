from django.shortcuts import render


# Create your views here.

def home(request):
    name = 'Adam Ficke'
    numbers = [1,2,3,4,5]
    args = {'myName': name, 'numbers':numbers} 
    return render(request,'login/home.html',args)

