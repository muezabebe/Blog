
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name="home"),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD

    path('dashboard', views.dashboard, name="dashboard"),
    path('dashboardall', views.dashboardall, name="dashboardall"),

    path('create-record', views.create_record, name="create-record"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),

    path('record/<int:pk>', views.singular_record, name="record"),
    path('allrecord/<int:pk>', views.allsingular_record, name="allrecord"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

    

]






