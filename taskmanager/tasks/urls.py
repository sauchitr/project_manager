from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/edit/', views.project_update, name='project_update'),
    path('project/<int:pk>/task/new/', views.task_create, name='task_create'),
    path('project/<int:pk>/task/edit/', views.task_update, name='task_update'),

    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),


    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="tasks/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="tasks/logout.html"), name="logout"),

]
