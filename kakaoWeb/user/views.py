from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from django.core import serializers
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


#회원가입
def signup_view(request):
    res_data = {}
    if request.method=='GET':
        return render(request, 'signup.html')
    elif request.method =='POST':
        # POST에서 값 받아옴
        username = request.POST['username']
        nickname = request.POST['nickname']
        age = request.POST['age']
        password = request.POST['password1']
        password2 =request.POST['password2']

        all = User.objects.all()
        username_lst = [x.username for x in all]
        nick_lst = [x.nickname for x in all]

        #예외처리
        if not(username and password and nickname and age):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != password2:
            res_data['error'] = '비밀번호가 다릅니다.'
        elif username in username_lst:
            res_data['error'] = '이미 있는 아이디입니다.'
        elif nickname in nick_lst:
            res_data['error'] = '이미 있는 닉네임입니다.'
        else:
            user=User.objects.create_user(
                username = username,
                password = password,
                nickname = nickname,
                age = age,
            )
            user.save()
            auth.login(request,user, backend='django.contrib.backends.ModelBackend')
            return redirect('stt:gate')
        return render(request, 'signup.html', res_data)

#로그인
def login_view(request):
    res_data={}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username = username, password = password)

        if User is not None:
            auth.login(request, User)
            return redirect('stt:gate')
        else:
            res_data['error'] = '로그인을 다시 해주세요'
    return render(request, 'login.html', res_data)


#로그아웃
@login_required
def logout_view(request):
    auth.logout(request)
    return redirect('stt:intro')