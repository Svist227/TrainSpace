from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import Autoriz, Register, classAutoriz, MyformChangePass, AddRegister, UpdateProfile
from Chuvash_Workout.models import data_people, MyUsers


# Create your views here. Работает функция по отправке полей авторизации
# def login_auth(request):
#     if request.method == 'POST':
#         form = Autoriz(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('main'))
#             else:
#                 messages.error(request, 'Вы не можете зайти т.к. не зарегестрированы')
#                 return redirect('users:login')
#     else:
#         form = Autoriz()
#     return render(request,'Chuvash_Workout/login.html', {'form': form} )



class Login_auth(LoginView):
    template_name = 'Chuvash_Workout/login.html'
    form_class = classAutoriz
    # def get_success_url(self):
    #     return reverse_lazy('main')


# def register(request):
#
#     if request.method == 'POST':
#         Form = Register(request.POST)
#         if Form.is_valid():
#             try:
#                 data_people.objects.create(**Form.cleaned_data)
#                 return redirect('main')  # перенаправление на глав стр
#             except:
#                 Form.add_error(None, 'Ошибка сохранения')
#
#     else:
#         Form = Register()
#     return render(request, 'Chuvash_Workout/register.html',{'form': Form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def register(request):
    if request.method == 'POST':
        Form = Register(request.POST)
        Form2= AddRegister(request.POST,request.FILES)
        if Form.is_valid() and Form2.is_valid():
            user = Form.save()
            user2 = Form2.save(commit=False)
            phot = MyUsers(photo=Form2.cleaned_data['photo'])
            user.set_password(Form.cleaned_data['password1'])
            user2.user = user
            user2.save()
            return redirect('users:login')
    else:
        Form = Register()
        Form2= AddRegister()
    return render(request,'Chuvash_Workout/register.html',{'form':Form, 'form2':Form2})

# class RegisterUser(CreateView):
#     form_class = Register
#     template_name = 'Chuvash_Workout/register.html'
#     success_url = reverse_lazy('users:login')
#     success_message = "%(calculated_field)s was created successfully"


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'Chuvash_Workout/password_change_form.html'
    form_class = MyformChangePass
    success_url = reverse_lazy('users:password_change_done')

def update_pro(request, pk):
    Form3 = User.objects.get(pk=pk)
    Form4 = MyUsers.objects.get(user=pk)

    if request.method == 'POST':
        Form = UpdateProfile(request.POST, instance= Form3)
        Form2 = AddRegister(request.POST,request.FILES, instance=Form4)
        if Form.is_valid() and Form2.is_valid():
            user = Form.save()
            user2 = Form2

            user2.user = user
            user2.save()
            return redirect('profile')
    context = {
        'form': UpdateProfile(instance=Form3), 'form2': AddRegister(instance=Form4)
    }
    return render(request, 'Chuvash_Workout/update_profile.html',context)