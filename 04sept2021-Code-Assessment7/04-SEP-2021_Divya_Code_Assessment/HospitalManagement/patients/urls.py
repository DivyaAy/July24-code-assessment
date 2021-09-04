from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add_value,name='add_value'),
    path('viewall/',views.view_value,name='view_value'),
    path('viewsingle/<id>',views.view_single,name='view_single'),
    path('search/',views.search,name='search'),
    path('update/',views.update,name='update'),
    path('updateact/',views.update_action,name='update_action'),
    path('delete/',views.delete,name='delete'),
    path('deleteact/',views.delete_action,name='delete_action'),

    path('homeui/',views.home,name='home'),
    path('addui/',views.add,name='add'),
    path('viewui/',views.view,name='view'),
    path('searchui/',views.pa_search,name='pa_search'),
    path('updateui/',views.pa_update,name='pa_update'),
    path('deleteui/',views.pa_delete,name='pa_delete'),
    
    
    
    
    
    
]