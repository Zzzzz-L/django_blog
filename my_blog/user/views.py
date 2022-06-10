from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .forms import UserLoginForm


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html', {'user_form': UserLoginForm()})

    def post(self, request):
        user_form = UserLoginForm(data=request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            # 这里的authenticate是django自带的方法，可以根据用户名和密码进行认证
            user = authenticate(username=data['username'], password=data['password'])
            # 如果认证成功，则返回user对象，否则返回None
            if user:
                # 将用户信息保存到session中，即可获取用户信息
                login(request, user)
                return redirect('article:index')
            else:
                return render(request, 'user/login.html', {'error': True, 'error_msg': '用户名或密码错误'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('article:index')


class RegisterView(View):
    def get(self, request):
        return render(request, 'user/register.html')
