
from Chuvash_Workout import views
from django.urls import path


urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name= 'programs'),
    path('review/', views.review, name= 'review'),
    path('programs/<slug:slug_id>/', views.programs_slug, name= 'programs_more'),
    path("profile/" ,views.profile, name='profile'),
]
