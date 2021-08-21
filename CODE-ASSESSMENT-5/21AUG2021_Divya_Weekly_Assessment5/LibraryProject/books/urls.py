from librarian.views import viewall
from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.addbook,name='addbook'),
    path('viewall/',views.viewall,name='viewall'),
    path('view/<id>',views.view_single,name='view_single'),
    path('name/<fetchid>',views.view_name,name='view_name'),
    path('',views.book,name='book'),
]