from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='user-login'),
#     path('logout/', views.user_logout, name='logout'),
]