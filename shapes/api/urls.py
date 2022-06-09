from django.urls import path, include
from . import views

app_name = 'shapes'

urlpatterns = [
    path('shapes/', views.ShapeListView.as_view(), name='shape_list'),
    path('shapes/add/', views.ShapeAddView.as_view(), name='shape_add'),
    path('users/add/', views.UserAddView.as_view(), name='user_add'),
    path('users/',views.UserListView.as_view(), name='user_list'),
    path('users/<pk>/', views.UserDetailView.as_view(), name='user_detail'),
    
]