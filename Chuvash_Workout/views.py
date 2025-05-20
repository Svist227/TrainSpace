from bdb import foo

from django.conf.urls import handler404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.

from Chuvash_Workout.models import training, data_people, Reviews


def main(request):
    forms = Reviews.objects.all()

    return render(request,'Chuvash_Workout/mainn.html', {'form': forms})


def about(request):
    return render(request, 'Chuvash_Workout/about.html')
@login_required(login_url='users:login')
def programs(request):
    prog = training.objects.all
    #prog = get_object_or_404(training,slug=slug_id)
    data = {
        'title': prog,
    }
    return render(request, 'Chuvash_Workout/programs.html',data)
@permission_required(perm="Chuvash_Workout.view_training" ,raise_exception=True)
def programs_slug(request,slug_id):  ##настройка фронтенда
    prog = get_object_or_404(training,slug=slug_id)
    data = {
        'title': prog,

    }
    return render(request,'Chuvash_Workout/programs_base.html',data )










@login_required(login_url='users:login')
def profile(request):
    form = get_user_model
    return render(request, "Chuvash_Workout/profile.html", {'form':form})
@login_required(login_url='users:login')

def review(request):
    if request.method == 'POST':
        form = Reviews(request.POST)
        Reviews.objects.create(reviews=request.POST.get('reviews'))
    else:
        form = Reviews()
    listt = Reviews.objects.all()
    paginaror = Paginator(listt,3)
    page_number = request.GET.get('page')
    page_obj = paginaror.get_page(page_number)
    return render(request, 'Chuvash_Workout/review.html',{'page_obj':page_obj})





def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Извини брат, но страница не найдена<h1>")


def permission_denied(request,exception,template_name='Chuvash_Workout/403.html'):
    return render(request,template_name)

