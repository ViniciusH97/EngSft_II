from django.urls import path
from app.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),  
    path('login/', LoginView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('funcionarios/', FuncionariosView.as_view(), name='funcionarios'),
    path('imoveis/', ImoveisView.as_view(), name='imoveis'),
    path('contratos/', ContratosView.as_view(), name='contratos'),
    path('vendasimoveis/', VendasImoveisView.as_view(), name='vendasimoveis'),
    path('locadores/', LocadoresView.as_view(), name='locadores'),
]