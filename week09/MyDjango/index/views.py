from django.shortcuts import render, redirect, reverse
from .form import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def error(request, msg):
    print(msg)
    param = {}
    param['msg'] = msg
    return render(request, 'error.html', param)

@login_required
def result(request):
    return render(request, 'result.html')

@login_required
def logout_view(request):
    logout(request)#此时Django认证模块会将数据库的session数据给清空
    return redirect("/login")

def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)  
                return redirect('/result')
            else:
                url = reverse('error',kwargs={'msg':'登录失败，密码错误'})
                return redirect(url)
        else:
            url = reverse('error',kwargs={'msg':'登录失败，无效参数'})
            return redirect(url)
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})