from django.urls import path,include
from system import views

app_name='system'

urlpatterns=[
    path('',views.landingPage,name='landingPage'),
    path('signup',views.registerPage,name='register_page'),
    path('login',views.login,name='login'),
    path('rent_post',views.rent_Post,name='rent_post'),
]

