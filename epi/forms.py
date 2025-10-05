from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Colaborador, Equipamento, Emprestimo

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cpf', 'email', 'senha']
        widgets = {'senha': forms.PasswordInput()}

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'descricao', 'quantidade_equipamento']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'equipamento', 'data_entrega',
                  'data_prevista_devolucao', 'data_devolucao', 'status', 'observacao_devolucao']
        widgets = {
            'data_entrega': forms.DateInput(attrs={'type': 'date'}),
            'data_prevista_devolucao': forms.DateInput(attrs={'type': 'date'}),
            'data_devolucao': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['equipamento'].queryset = Equipamento.objects.all()
        self.fields['colaborador'].queryset = Colaborador.objects.all()

        # Lógica para campos de devolução (em casos de criação)
        if 'instance' not in kwargs:
            self.fields['data_devolucao'].required = False
            self.fields['observacao_devolucao'].required = False

    def clean(self):
        cleaned_data = super().clean()
        data_entrega = cleaned_data.get('data_entrega')
        data_prevista_devolucao = cleaned_data.get('data_prevista_devolucao')

        # Validação para garantir que a data de entrega não é no futuro
        if data_entrega and data_entrega > date.today():
            self.add_error('data_entrega', "A data de entrega não pode ser no futuro.")
        
        # Validação para garantir que a data prevista de devolução é posterior à data de entrega
        if data_entrega and data_prevista_devolucao and data_prevista_devolucao < data_entrega:
            self.add_error('data_prevista_devolucao', "A data de devolução deve ser posterior à data de entrega.")
            
        return cleaned_data
    
