from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('diagram/', views.diagram, name='diagram'),
    path('report/', views.report, name='report'),
    path('delete/<str:table>/<int:item_id>/', views.delete_item, name='delete_item'),
    path('edit/<str:table>/<int:item_id>/', views.edit_item, name='edit_item'),
    path('edit_comment/<int:item_id>/<str:class_veh_or_not>/', views.edit_comment, name='edit_comment'),
    path('save_comment/', views.save_comment, name='save_comment'),
    path('comment_history/', views.comment_history, name='comment_history'),
]  
