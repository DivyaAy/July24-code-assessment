from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.loginview,name='loginview'),
    path('register/',views.regview,name='regview'),
    
   
    path('registeraction/',views.user_create,name='user_create'),
    path('viewprofile/',views.login_check,name='login_check'),
]