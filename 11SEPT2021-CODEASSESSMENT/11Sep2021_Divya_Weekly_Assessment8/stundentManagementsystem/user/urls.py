from django.urls import path,include
from . import views

urlpatterns = [
    path('useradd/',views.user_add,name="user_add"),
    path('userview/',views.user_view,name="user_view"),
    path('usersingle/<id>',views.user_viewsingle,name="user_viewsingle"),
    path('viewstdprofile/',views.login_check,name="login_check"),
    path('update/',views.update_user,name="update_user"),
    path('updateaction/',views.update_action,name="update_action"),
    

    path('regui/',views.register,name="register"),
    path('loginui/',views.loginuser,name="loginuser"),
    # path('viewui/',views.viewuser,name="viewuser"),
    path('profile/',views.viewprofile,name="viewprofile"),
    
    
]