from typing import Any
from django.db.models.query import QuerySet
from Contato.models import Contato
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from Contato.forms import ContatoModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

############## FUNCTION BASED VIEWS ##########################################
# def Contato_View(request):
#   contatos = Contato.objects.all()
# essa sintaxe pega o parametro da url ?search=''
#  parametro = request.GET.get('search')
# otima funcionalidade __ pode ser usado para navegar entre tabelas e fazer algumas funções, tipo contains, icontains ignora upcase
# if parametro:
#    contatos = Contato.objects.filter(
#        Categoria__Categoria__icontains=parametro).order_by('Categoria', 'Nome')
# print(contatos)
# return render(request, 'Contato.html', {'contatos': contatos})

############## CLASS BASED VIEWS - USANDO VIEW BASICA####################
# class ContatoView(View):
#    def get(self, request):
#        contatos = Contato.objects.all().order_by('Nome')
#        search = request.GET.get('search')
#
#        if search:
#            contatos = contatos.filter(
#                Categoria__Categoria__icontains=search).order_by('Categoria', 'Nome')
#
#        return render(
#            request, 'Contato.html', {'contatos': contatos}
#        )

@method_decorator(login_required(login_url='login'), name='dispatch')
class ContatoListView(ListView):
    model = Contato
    template_name = 'Contato.html'
    context_object_name = 'contatos'

    def get_queryset(self):
        # basicamente esse trecho navega com super para apontar para o pai, que no caso é o Contato, get_queryset é qs igual o Contato.objects.all()
        contatos = super().get_queryset().order_by('Categoria')
        search = self.request.GET.get('search')
        if search:
            contatos = contatos.filter(Categoria__Categoria__icontains=search)
        return contatos

############## FUNCTION BASED VIEWS ##########################################
# def New_Contato_View(request):
#    if request.method == 'POST':
#        New_Contato_Form = ContatoModelForm(request.POST, request.FILES)
#        print(New_Contato_Form.data)
#        if New_Contato_Form.is_valid():
#            New_Contato_Form.save()
#            return redirect('Contatos_list')
#    else:
#        New_Contato_Form = ContatoModelForm()
#    return render(request, 'New_Contato.html', {'New_Contato_Form': New_Contato_Form})

############## CLASS BASED VIEWS - USANDO VIEW BASICA####################
# class NewContatoView(View):
#
#    def get(self, request):
#        New_Contato_Form = ContatoModelForm()
#        return render(request, 'New_Contato.html', {'New_Contato_Form': New_Contato_Form})
#
#    def post(self, request):
#        New_Contato_Form = ContatoModelForm(request.POST, request.FILES)
#        if New_Contato_Form.is_valid():
#            New_Contato_Form.save()
#            return redirect('Contatos_list')
#        return render(request, 'New_Contato.html', {'New_Contato_Form': New_Contato_Form})

@method_decorator(login_required(login_url='login'), name='dispatch')
class ContatoCreateView(CreateView):
    model = Contato
    # lembra que tem q trocar o html para form, pois a view troca a informação automaticamente
    form_class = ContatoModelForm
    template_name = 'New_Contato.html'
    success_url = '/Contato/'


@method_decorator(login_required(login_url='Login'), name='dispatch')
class ContatoDetailView(DetailView):
    model = Contato
    template_name = 'Contato_detail.html'

@method_decorator(login_required(login_url='Login'), name='dispatch')
class ContatoUpdateView(UpdateView):
    model = Contato
    form_class = ContatoModelForm
    template_name = 'Contato_update.html'

    def get_success_url(self):
        return reverse_lazy('Contato_Detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='Login'), name='dispatch')
class ContatoDeleteView(DeleteView):
    model = Contato
    template_name = 'Contato_delete.html'
    success_url = '/Contato/'
