from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from users import views
from django.urls import path, reverse_lazy

from users.views import MyPasswordChangeView

app_name = 'users'
urlpatterns = [

    path('login/',views.Login_auth.as_view(), name= 'login'),
    path("register/" ,views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    # path("login/register/",views.register, name='register'),
    path('password-change/',MyPasswordChangeView.as_view() , name='password_change'),
    path('password-change/done/',PasswordChangeDoneView.as_view(template_name='Chuvash_Workout/password_change_done.html'), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(template_name='Chuvash_Workout/password_reset_form.html',
    email_template_name='Chuvash_Workout/password_reset_email.html',
 success_url=reverse_lazy('users:password_reset_done')                                                  ), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='Chuvash_Workout/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='Chuvash_Workout/password_reset_confirm.html',
     success_url=reverse_lazy('users:password_reset_complete') ), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view
    (template_name='Chuvash_Workout/password_reset_complete.html'),
         name='password_reset_complete' ),
    path('update-profile/<int:pk>', views.update_pro, name='update_profile')
]
