from . import views
from django.urls import path
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'), #ustawiam w settings
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name = 'logout'), #ustawiam w settings
    path('password_change/', auth_view.PasswordChangeView.as_view(template_name='password_change_form.html'), name='password_change'),
    path('password_change/done', auth_view.PasswordChangeDoneView.as_view(template_name='password_change_done'), name='password_change_done')
    ]