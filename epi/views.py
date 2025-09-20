from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento, Emprestimo, Colaborador
from .forms import EquipamentoForm, EmprestimoForm, ColaboradorForm
from django.db.models import Q

def home(request):
    return render(request, 'base.html')

def lista_colaboradores(request):
    query = request.GET.get('q')
    if query:
        colaboradores = Colaborador.objects.filter(Q(nome__icontains=query) | Q(cpf__icontains=query))
    else:
        colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores_list.html', {'colaboradores': colaboradores})

def criar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('colaboradores_list')
    else:
        form = ColaboradorForm()
    return render(request, 'colaboradores_form.html', {'form': form})

def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('colaboradores_list')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'colaboradores_form.html', {'form': form})

def excluir_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('colaboradores_list')
    return render(request, 'confirm_delete.html', {'obj': colaborador})

def lista_equipamentos(request):
    query = request.GET.get('q')
    if query:
        equipamentos = Equipamento.objects.filter(nome__icontains=query)
    else:
        equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos_list.html', {'equipamentos': equipamentos})

def criar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamentos_list')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamentos_form.html', {'form': form})

def editar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('equipamentos_list')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamentos_form.html', {'form': form})

def excluir_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('equipamentos_list')
    return render(request, 'confirm_delete.html', {'obj': equipamento})

def lista_emprestimos(request):
    query = request.GET.get('q')
    if query:
        emprestimos = Emprestimo.objects.filter(colaborador__nome__icontains=query)
    else:
        emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos_list.html', {'emprestimos': emprestimos})

def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprestimos_list')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimos_form.html', {'form': form})

def editar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimos_list')
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimos_form.html', {'form': form})

def excluir_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        emprestimo.delete()
        return redirect('emprestimos_list')
    return render(request, 'confirm_delete.html', {'obj': emprestimo})