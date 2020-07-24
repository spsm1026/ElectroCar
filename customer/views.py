from django.shortcuts import render
from .models import User, Bookmark
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from map.models import Carcharger

# main.html 을 불러주는 함수
def home(request):
    return render(request, 'customer/test.html')

# customer.html 을 불러주는 함수
def create(request):
    return render(request, 'customer/customer.html')
    
def home2(request):
    return render(request, 'customer/test2.html')

#new_pw.html 를 불러주는 함수
def find(request):
    return render(request, 'customer/new_pw.html')

# 회원가입
def register(request):
    car_charge_list = Carcharger.objects.order_by('id')
    if request.method == 'POST':
        # 입력값이 같다면 DB에 저장
        if request.POST['password1'] == request.POST['password2']:
            user = User(
                useremail = request.POST['useremail'], password = request.POST['password1'], cars = request.POST['cars'])
            user.save()
            return render(request, 'customer/register_success.html')
            # return HttpResponseRedirect('/electrocar/create')
        else:
            return render(request, 'customer/register_fail.html')
        # DB에 데이터 저장후 로그인 화면으로 이동
        return render(request, 'customer/customer.html')
    # 로그인/회원가입 화면 보여주기

    uri = request.META['HTTP_REFERER']
    print('uri', uri)
    request.session['redirect_uri'] = uri

    return render(request, 'customer/customer.html', {'car_charge_list' : car_charge_list})

# 로그인
def login(request):
    car_charge_list = Carcharger.objects.order_by('id')
    user_list = User.objects.order_by('id')
    if request.method == 'POST':
        useremail = request.POST['useremail']
        password = request.POST['password']

        for user_i in user_list:
            if user_i.useremail == useremail:
                login_user_id = user_i.id
        try:
            user = User.objects.get(useremail = useremail, password = password)
            # user 안에 입력한 값이 있나 확인 후 메인페이지로 이동
            if user:
                session_save(request, useemail, login_user_id)
                # del request.session['redirect_uri']
                return render(request, 'customer/login_success.html')
            # return HttpResponseRedirect('/electrocar/home')
        except :
            # user 안에 입력한 값이 없을 경우 없다고 안내 후 로그인 페이지로 다시 이동
            return render(request, 'customer/login_fail.html')  
    else:
        return render(request, 'customer/customer.html', {'car_charge_list' : car_charge_list})

# 로그아웃
def logout(request):
    request.session['useremail'] = None
    request.session.clear()
    return HttpResponseRedirect('/electrocar_c/home2')
    # return HttpResponseRedirect(reverse('home'))

# 비밀번호 찾기
def find_password(request):
    if request.method == 'POST':
        try:
            # 2 user 모델에서 이메일 확인
            useremail = request.POST['useremail']
            user = User.objects.get(useremail = useremail)

            if user:
                request.session['useremail'] = useremail
            # 확인 되는 경우 비밀번호 입력 화면으로 이동
                return HttpResponseRedirect('/electrocar_c/find/')
        except:
            return render(request, 'customer/find_fail.html')

    # 1 이메일을 입력할 수 있는 화면 보여주기
    return render(request, 'customer/find_pw.html')
    
# 새비밀번호 설정
def new_password(request):
    if request.method == 'POST':
        # 첫번째 입력한 비밀번호와 두번째 입력한 비밀번호 비교후 같으면 DB 수정
        if request.POST['password1'] == request.POST['password2']:
            # user = User(
            #     useremail = request.session['useremail'], password = request.POST['password1'], cars = request.POST['cars'])
            
            useremail = request.session['useremail']
            user = User.objects.get(useremail = useremail)
            user.password = request.POST['password1']
            user.save()
            return render(request, 'customer/change_success.html')
            # return HttpResponseRedirect('/electrocar/create')
        # 입력한 비밀번호가 같지 않을 경우
        else:
            return render(request, 'customer/change_fail.html')
    # 3 비밀번호를 변경할 수 있는 화면 보여주기
    return render(request, 'customer/new_pw.html')

def bm_input(request):
    bm = Bookmark(user_id = request.session.login_user_id , bookmar_address = request.GET["address_input"] )
    bm.save()
    return 1