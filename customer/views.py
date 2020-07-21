from django.shortcuts import render
from .models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.

# main.html 을 불러주는 함수
def home(request):
    return render(request, 'main.html')
# customer.html 을 불러주는 함수
def create(request):
    return render(request, 'customer/customer.html')

# 회원가입
def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User(
                useremail = request.POST['useremail'], password = request.POST['password1'], cars = request.POST['cars'])
            user.save()
            return HttpResponseRedirect('/electrocar/create')
        return render(request, 'customer/customer.html')
    return render(request, 'customer/customer.html')

# 로그인
def login(request):
    if request.method == 'POST':
        useremail = request.POST['useremail']
        password = request.POST['password']
        user = User.objects.get(request, useremail = useremail, password = password)
        if user is not None:
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'customer/customer.html'), {'error': 'useremail or password is incorrect'}
    else:
        return render(request, 'customer/customer.html')

# 로그아웃
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home')
    # return HttpResponseRedirect(reverse('home'))

# 비밀번호 찾기
def find_password(request):
    return render(request, 'customer/customer.html')