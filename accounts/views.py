from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'erp/index.html')
# 회원가입
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/index.html')
        else:
            return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if password != password2:
            # 패스워드가 다름
            return render(request, 'accounts/signup.html', {'error': '패스워드를 확인 해 주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'accounts/signup.html', {'error': '사용자 이름과 비밀번호는 필수 입니다!'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'accounts/signup.html', {'error': '사용자가 이미 존재합니다.'})
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')


# 로그인
def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)
        # 장고모듈로 검사를 하게하고 유저정보를 me에 담음
        if me is not None:  # 사용자가 비어있지 않다면 그 사용자를 로그인시켜줌
            auth.login(request, me)
            return redirect('/')  # 잘 로그인되는부분
        else:
            return render(request, 'accounts/signin.html', {'error': '유저이름 혹은 패스워드를 다시 확인해주세요.'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            print("1")
            return render(request, 'erp/index.html')
        else:
            print("2")
            return render(request, 'accounts/signin.html')

@login_required  # 로그인이 꼭 되어있어야 접근이 가능하다는 말
def logout(request):
    auth.logout(request)
    return render(request, 'accounts/signin.html')