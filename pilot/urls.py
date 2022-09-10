from django.contrib import admin
from django.urls import path,include
from pilot import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.register, name='register' ),
    path('register', views.register, name='register' ),
    path('login', views.login, name='login' ),
    path('add_task', views.add_task, name='add_task' ),
    path('delete', views.delete, name='delete' ),
    path('filter_data', views.filter_data, name='filter_data' ),
    
    
    
]
