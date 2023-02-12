from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_member_list, name='member_list'),
    path('add/', views.create_member, name='add_member'),
    path('update/<int:pk>/', views.update_member, name="update_member"),
    path('delete/<int:pik>/', views.delete_member, name='delete_member')
]