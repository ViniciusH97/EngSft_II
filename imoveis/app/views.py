from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Erro: Usuário ou senha inválida!'})
        

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')  


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        return redirect('index')

class FuncionariosView(TemplateView):
    template_name = 'funcionarios.html'

class ImoveisView(TemplateView):
    template_name = 'imoveis.html'

class ContratosView(TemplateView):
    template_name = 'contratos.html'

class VendasImoveisView(TemplateView):
    template_name = 'vendasimoveis.html'

class LocadoresView(TemplateView):
    template_name = 'locadores.html'