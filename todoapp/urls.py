from django.urls import path
from .views import home, register, loginpage, DeleteTask, Update, LogoutView


urlpatterns = [
    path('', home, name = 'home-page'),
    path('register/', register, name = 'register'),
    path('login/', loginpage, name = 'login'),
    path('logout/', LogoutView, name='logout'),
    path('delete-task/<str:name>/', DeleteTask, name='delete'),
    path('update/<str:name>/', Update, name='update'),
]