from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.
from django.views import View
from .forms import UserRegisterationForm,VerificationCodeForm
import random
from utils import send_otp_code
from .models import OtpCode ,User
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(View):

    form_class=UserRegisterationForm

    template_name='accounts/register.html'

    def get(self,request):
        form=self.form_class()

        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            random_code=random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone'],random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'],code=random_code)

            request.session['user_registration_info']={

                    'email':form.cleaned_data['email'],
                    'phone_number':form.cleaned_data['phone'],
                    'full_name':form.cleaned_data['full_name'],
                    'password':form.cleaned_data['password1'],

            }
            messages.success(request,'we have sent you a  verification code','success')
            return redirect('accounts:verifying_code')

        return render(request,self.template_name,{'form':form})


class VerificationCodeView(View):
    form_class=VerificationCodeForm
    def setup(self, request, *args: any, **kwargs: any) -> None:
     
        self.code_instance=OtpCode.objects.get(phone_number=request.session['user_registration_info']['phone_number'])

        return super().setup(request, *args, **kwargs)

    def get(self,request):
        form=self.form_class
        return render(request,'accounts/verify.html',{'form':form})


    def post(self,request):
        form=self.form_class(request.POST)
        user_session=request.session['user_registration_info']
        ProductConfigform=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            if cd['code']==self.code_instance.code :
                User.objects.create_user(user_session['phone_number'],user_session['email'],user_session['full_name'],user_session['password'])                
                self.code_instance.delete()
                messages.success(request,'you have registered succcessfully','success')
                return redirect('home:home')

            else:
                messages.error(request,' This code is not valid','danger')
                return redirect('accounts:verifying_code')
        return redirect('home:home')


class UserLoginView(View):
    form_class=UserLoginForm
    template_class='accounts/login.html'
    def setup(self, request , *args ,**kwargs) -> None:
        self.next=request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)


    def get(self,request):
        form=UserLoginForm
        return render(request,'accounts/login.html',{'form':form})
        
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate (request,phone_number=cd['phone'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'you are logged in','success')
                if self.next:
                    return redirect(self.next)
                return redirect('home:home')

            messages.error(request,'the username or password is wrong')
            return render(request,self.template_class,{'form':form})
        
        return render(request,self.template_class,{'form':form})


class UserLogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'you loged out successfully','success')
        return redirect('home:home')

