from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Equipamento
from .models import Colaborador
from datetime import date, timedelta

from .models import Equipamento, Colaborador, Emprestimo


# TESTES DE USUÁRIO

class ColaboradorModelTest(TestCase):

    # CT-USR-001 - Criar novo usuário com dados inválidos
    def test_CT_USR_001_criar_usuario_valido(self):
        colaborador = Colaborador.objects.create(nome='joao', email='joao@ex.com', senha='senha123', cpf="12345678911")
        self.assertEqual(colaborador.nome, 'joao')
        self.assertTrue(colaborador.senha,'senha123')
   
   #CT-USR-002 - Tentar criar usuário com email existente
    def test_CT_USR_002_email_duplicado(self):
        Colaborador.objects.create(nome='maria', email='maria@ex.com', senha='senha123', cpf="12345678911")
        with self.assertRaises(IntegrityError):
            Colaborador.objects.create(nome='outra', email='maria@ex.com', senha='outrasenha', cpf="12345678911")

    #CT-USR-003 -  Editar dados de usuário
    def test_CT_USR_003_editar_usuario(self):
        colaborador = Colaborador.objects.create(nome='carlos', email='carlos@ex.com', senha='senha123', cpf="12345678911")
        colaborador.email = 'novo@ex.com'
        colaborador.save()
        c2 = Colaborador.objects.get(nome='carlos')
        self.assertEqual(c2.email, 'novo@ex.com')


# TESTES DE EPI


class EquipamentoModelTest(TestCase):

    # CT-EPI-001 - Criar EPI válido
    def test_CT_EPI_001_criar_epi_valido(self):
        epi = Equipamento.objects.create(
            nome="Capacete de Segurança",
            quantidade_equipamento=3,
            descricao="Capacete para uso em obras"
        )
        self.assertEqual(epi.nome, "Capacete de Segurança")
        self.assertEqual(epi.quantidade_equipamento, 3)

    # CT-EPI-002 - Tentar criar EPI com dados inválidos (ex: nome vazio)
    def test_CT_EPI_002_dados_invalidos(self):
        epi = Equipamento(
            nome="",  
            quantidade_equipamento=5,
            descricao="Faltando nome"
        ) 
        with self.assertRaises(ValidationError):
            epi.full_clean()  
            epi.save()

    # CT-EPI-003 - Deletar EPI existente
    def test_CT_EPI_003_deletar_epi(self):
        epi = Equipamento.objects.create(
            nome="Luva Térmica",
            quantidade_equipamento=10,
            descricao="Proteção contra calor"
        )
        epi_id = epi.id
        epi.delete()
        self.assertFalse(Equipamento.objects.filter(id=epi_id).exists())

class EmprestimoModelTest(TestCase):

    def setUp(self):
        self.colaborador = Colaborador.objects.create(
            nome="João da Silva",
            email="joao@empresa.com",
            senha="123456",
            cpf="12345678900"
        )
        self.equipamento = Equipamento.objects.create(
            nome="Capacete de Segurança",
            quantidade_equipamento=5,
            descricao="Capacete de proteção"
        )


    # CT-CTRL-001 — Criar um empréstimo válido
    def test_CT_CTRL_001_criar_emprestimo_valido(self):
        emprestimo = Emprestimo.objects.create(
            colaborador=self.colaborador,
            equipamento=self.equipamento,
            data_entrega=date.today(),
            data_prevista_devolucao=date.today() + timedelta(days=7),
            status="Emprestado"
        )

        self.assertEqual(emprestimo.colaborador.nome, "João da Silva")
        self.assertEqual(emprestimo.equipamento.nome, "Capacete de Segurança")
        self.assertEqual(emprestimo.status, "Emprestado")
        self.assertIsNone(emprestimo.data_devolucao)
        self.assertEqual(Emprestimo.objects.count(), 1)


    # CT-CTRL-002 — Impedir empréstimo com estoque insuficiente
  
    def test_CT_CTRL_002_impedir_emprestimo_estoque_insuficiente(self):
        self.equipamento.quantidade_equipamento = 0
        self.equipamento.save()

      
        with self.assertRaises(Exception):
            Emprestimo.objects.create(
                colaborador=self.colaborador,
                equipamento=self.equipamento,
                data_entrega=date.today(),
                data_prevista_devolucao=date.today() + timedelta(days=5),
                status="Emprestado"
            )
