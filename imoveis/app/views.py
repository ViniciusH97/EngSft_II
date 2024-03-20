from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView
from app.models import Funcionario, Imovel, Contrato_de_Locacao, Vendas_de_imoveis, Locador

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        print(user)


        if user is not None:
            #if user.is_superuser:
            login(request, user)
            return redirect('index')
           # else:
               # return render(request, 'login.html', {'error_message': 'Erro: Acesso negado!'})
        else:
            return render(request, 'login.html', {'error_message': 'Erro: Usuário ou senha inválida!'})
        

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login') 


class Index(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        return redirect('index')

class FuncionariosView(TemplateView):
    template_name = 'funcionarios.html'

def funcionarios_view(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios.html', {'funcionarios': funcionarios})

class ImoveisView(TemplateView):
    template_name = 'imoveis.html'

def imoveis_view(request):
    imoveis = Imovel.objects.all()
    return render(request, 'imoveis.html', {'imoveis': imoveis})

class ContratosView(TemplateView):
    template_name = 'contratos.html'

def contratos_view(request):
    contratos = Contrato_de_Locacao.objects.all()
    return render(request, 'contratos.html', {'contratos': contratos})

class VendasImoveisView(TemplateView):
    template_name = 'vendasimoveis.html'

def vendasimoveis_view(request):
    vendasimoveis = Vendas_de_imoveis.objects.all()
    return render(request, 'vendasimoveis.html', {'vendasimoveis': vendasimoveis})

class LocatarioView(TemplateView):
    template_name = 'locatarios.html'

def locatarios_view(request):
    locatarios = Locador.objects.all()
    return render(request, 'locatarios.html', {'locatarios': locatarios})

class locadoresView(TemplateView):
    template_name = 'locadores.html'

def locadores_view(request):
    locadores = Locador.objects.all()
    return render(request, 'locadores.html', {'locadores': locadores})