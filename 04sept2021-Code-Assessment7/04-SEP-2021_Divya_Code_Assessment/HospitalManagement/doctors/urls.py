from django.urls import path,include
from . import views

urlpatterns = [
    path('insert/',views.insert_detail,name='insert_detail'),
    path('showall/',views.showall,name='showall'),
    path('showone/<id>',views.view_one,name='view_one'),
    path('find/',views.find,name='find'),
    path('updatedoc/',views.update_one,name='update_one'),
    path('upact/',views.up_action,name='up_action'),
    path('deletedoc/',views.delete_one,name='delete_one'),
    path('delact/',views.del_action,name='del_action'),

    path('homeui/',views.doc_home,name='doc_name'),
    path('insertui/',views.doc_insert,name='doc_insert'),
    path('showui/',views.doc_show,name='doc_show'),
    path('findui/',views.doc_search,name='doc_search'),
    path('updateui/',views.doc_update,name='doc_update'),
    path('deleteui/',views.doc_delete,name='doc_delete'),
    
    
    
    
    
    


]