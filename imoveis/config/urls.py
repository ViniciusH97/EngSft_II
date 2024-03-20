from django.urls import path
from app.views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'), 
    path('index/', Index.as_view(), name='index'),  
    path('logout/', LogoutView.as_view(), name='logout'),
    path('funcionarios/', funcionarios_view, name='funcionarios'),
    path('imoveis/', imoveis_view, name='imoveis'),
    path('contratos/', contratos_view, name='contratos'),
    path('vendasimoveis/', vendasimoveis_view, name='vendasimoveis'),
    path('locatarios/', locatarios_view, name='locatarios'),
    path('locadores/', locadores_view, name='locadores'),
]
