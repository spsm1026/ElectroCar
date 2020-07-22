from django.shortcuts import render
from .models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from map.models import Carcharger

# main.html 을 불러주는 함수
def home(request):
    return render(request, 'customer/test.html')

# customer.html 을 불러주는 함수
def create(request):
    return render(request, 'customer/customer.html')
def find(request):
    return render(request, 'customer/new_pw.html')

# 회원가입
def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User(
                useremail = request.POST['useremail'], password = request.POST['password1'], cars = request.POST['cars'])
            user.save()
            return render(request, 'customer/register_success.html')
            # return HttpResponseRedirect('/electrocar/create')
        return render(request, 'customer/customer.html')
    return render(request, 'customer/customer.html')

# 로그인
def login(request):
    car_charge_list = Carcharger.objects.order_by('id')
    if request.method == 'POST':
        useremail = request.POST['useremail']
        password = request.POST['password']
        try:
            user = User.objects.get(useremail = useremail, password = password)
            if user is not None:
                request.session['useremail'] = useremail
                return render(request, 'customer/login_success.html')
            # return HttpResponseRedirect('/electrocar/home')
        except :
            return render(request, 'customer/login_fail.html')  
       
    else:
        return render(request, 'customer/customer.html', {'car_charge_list' : car_charge_list})

# 로그아웃
def logout(request):
    request.session['useremail'] = None
    request.session.clear()

    return HttpResponseRedirect('electrocar_c/home')
    # return HttpResponseRedirect(reverse('home'))

# 비밀번호 찾기
def find_password(request):
    if request.method == 'POST':
        try:
            # 2 user 모델에서 이메일 확인
            useremail = request.POST['useremail']
            print(useremail)
            user = User.objects.get(useremail = useremail)
            print(user)


            if user:
                request.session['useremail'] = useremail
            # 확인 되는 경우 비밀번호 입력 화면으로 이동
                return HttpResponseRedirect('/electrocar_c/find/')
        except:
            return render(request, 'customer/find_pw.html')

    # 1 이메일을 입력할 수 있는 화면 보여주기
    return render(request, 'customer/find_pw.html')
    
# 새비밀번호 설정
def new_password(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # user = User(
            #     useremail = request.session['useremail'], password = request.POST['password1'], cars = request.POST['cars'])
            
            useremail = request.session['useremail']
            user = User.objects.get(useremail = useremail)
            user.password = request.POST['password1']
            user.save()
            return render(request, 'customer/change_success.html')
            # return HttpResponseRedirect('/electrocar/create')
        else:
            return render(request, 'customer/change_fail.html')
        
    
    # 3 비밀번호를 변경할 수 있는 화면 보여주기
    return render(request, 'customer/new_pw.html')