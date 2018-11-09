from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View


class Login(View):
    def get(self, request):
        username = ""
        password = ""
        next = request.GET.get('next','/')
        if request.user.is_authenticated:
            return HttpResponseRedirect(next)
        return render(request, 'login.html',{'next':next,'loginerror':False})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST.get('next','/')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
        return render(request, 'login.html',{'next':next,'loginerror':True})


class Logout(View):
    def get(self, request):
        next = request.GET.get('next','/')
        logout(request)
        return HttpResponseRedirect(next)

    def post(self, request):
        next = request.POST.get('next','/')
        logout(request)
        return HttpResponseRedirect(next)