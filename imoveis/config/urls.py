from django.urls import path
from app.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),  
    path('login/', LoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='index.html'),
]
