from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

#요청받는 request에서 username이 존재하는지
#요청받는 request에서 pasword 존재하는지
#요청받는 request에서 password와 password_check가 같은지
def sign_up(request):
    context ={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check=request.POST.get('password_check')   
        
        if (username and password and password == password_check ):
            try:
                new_user = User.objects.create_user(username=username, password=password)
                auth.login(request, new_user)            
                return redirect('blog_samples:home')
            except:
                context['error']='이미 존재하는 아이디 입니다.'
               
        else:
            context['error'] ='잘못입력했습니다.'


    return render(request, 'my_accounts/sign_up.html', context)


def login(request):
    #쿠키값에 세션id값이 담겨있어 로그인된 상태를 인지 (blog home)으로 redirect
    if request.user.is_authenticated:
        return redirect("blog_samples:home")
    context={}
    #요청이 리퀘스트인지 확인 
    if request.method == 'POST':
        #아이디 입력받은 것 있는지
        username = request.POST.get('username')
        #비밀번호 입력받은 것 있는지
        password = request.POST.get('password')
        if (username and password ):
            #비밀번호 체크 ---- 추가적으로 필요한 함수
            user = auth.authenticate(request, username= username, password=password)
            #로그인 o
            if user : 
                auth. login(request, user)
                #리다이렉트o
                return redirect('blog_samples:home')
            else:
                context['error'] ='아이디랑 비밀번호 틀렸습니다.'
        else:
            context['error'] = '아이디 혹은 비밀번호를 입력해주세요...'
        #context에 에러메세지 담아주기

    
    return render(request, 'my_accounts/login.html', context)


def logout(request):
    # 요청이 post인지 확인
    # if request.method == "POST":
    auth.logout(request)
    # 리다이렉트
    return redirect('blog_samples:home')


def naver_test(request):
    return render(request, 'my_accounts/naver_test.html')