from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        messages.info(request, 'Қате деректер жазылған!')
        return redirect('login')

    return render(request, 'account/login.html')


def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']


        if User.objects.filter(username=username).exists():
            messages.info(request, 'Қолданушы аты бұрын тіркелген!')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Қолданушы email бұрын тіркелген!')
            return redirect('register')

        if len(first_name)  == 0:
            messages.info(request, 'Есіміңізді толтырыңыз')
            return redirect('register')

        if  len(last_name)  == 0:
            messages.info(request, 'Тегіңізді толтырыңыз')
            return redirect('register')

        if  len(username)  == 0:
            messages.info(request, 'Қолданушы атын  жазыңыз')
            return redirect('register')

        if len(password) == 0:
            messages.info(request, 'Құпия сөзді жазыңыз')
            return redirect('register')


        if len(password)>=8 and any(char.isdigit() for char in password) and password != password.upper() and password!= password.lower() and password == password1:
            pass
        else:
            messages.info(request, 'Қупия сөз қате')
            return redirect('register')



        User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password).save()
        return redirect('login')

    return render(request, 'account/register.html')


def Logout(request):
    pass