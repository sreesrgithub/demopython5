from . import views
from django.urls import path

urlpatterns = [

    path('', views.index, name='demo'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('new_page', views.new_page, name='new_page'),
    path('form', views.form, name='form'),
    path('submit', views.submit, name='submit'),
    path('logout', views.logout, name='logout'),

]
