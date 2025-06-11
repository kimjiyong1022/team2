from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')  # 닉네임
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 사용 중인 닉네임입니다.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')  # 또는 원하는 페이지로 리디렉션

    return render(request, 'accounts/signup.html')