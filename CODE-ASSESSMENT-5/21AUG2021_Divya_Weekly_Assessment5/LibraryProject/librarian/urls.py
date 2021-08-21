from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add,name='add'),
    path('viewall/',views.viewall,name='viewall'),
    path('view/<id>',views.view_single,name='view_single'),
    path('enroll_code/<fetchid>',views.view_code,name='view_code'),
    path('register/',views.reg,name='reg'),
    path('login/',views.log,name='log'),
]