from django.shortcuts import render,redirect
from .models import MyUser
from .forms import LoginForm,SignupForm
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from maintainbill.models import *

# Create your views here.
@require_GET
@login_required
def main(request):
	if request.user.is_authenticated():
		for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
		return render(request,'main.html')
	else:
		form=LoginForm()
		return render(request,'login.html',{'loginform':form})
@require_POST
def handleSignup(request):
	if request.user.is_authenticated():
		for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
		return redirect('main')
	f=SignupForm(request.POST)
	next_url=request.POST.get('next')
	if f.is_valid():
		user=f.save()
		user.is_active=False
		user.save()
		loginform=LoginForm()
		data={'user':user,'loginform':loginform}
		return render(request,'login.html',data)
	else:
		signupform=f
		loginform=LoginForm()
		data={'signupform':signupform,'loginform':loginform,'next':next_url}
		return render(request,'signup.html',data)
@require_POST
def handleLogin(request):
	if request.user.is_authenticated():
		for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
		return redirect('main')
	f=LoginForm(request.POST)
	next_url=request.GET.get('next')
	if f.is_valid():
		user=f.get_user()
		login(request,user)
		for checkuser in ServiceProvider.objects.all():
			if checkuser.id==user.id:
				logout(request)
				return render(request,'invalidloginuserlogout.html')
		if not next_url:
			return redirect('main')
		else :
			return redirect(next_url)
	else:
		loginform=f
		signupform=SignupForm()
		data={'signupform':signupform,'loginform':loginform,'next':next_url}
		return render(request,'login.html',data)

@require_GET
@login_required
def logoutview(request):
	if request.user.is_authenticated():
		logout(request)
		form=LoginForm()
		return render(request,'login.html',{'loginform':form})
@require_GET
def renderLogin(request):
	if request.user.is_authenticated():
		for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
		return redirect('main')
	next_url=request.GET.get('next')
	loginform=LoginForm()
	data={'loginform':loginform,'next':next_url}
	return render(request,'login.html',data)
@require_GET
def renderSignup(request):
	if request.user.is_authenticated():
		for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
		return redirect('main')
	next_url=request.GET.get('next')
	signupform=SignupForm(initial={'phone':'+91'})
	data={'signupform':signupform,'next':next_url}
	return render(request,'signup.html',data)

