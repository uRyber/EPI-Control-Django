from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade_equipamento = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ("Emprestado", "Emprestado"),
        ("Em uso", "Em uso"),
        ("Fornecido", "Fornecido"),
        ("Devolvido", "Devolvido"),
        ("Danificado", "Danificado"),
        ("Perdido", "Perdido"),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_entrega = models.DateField()
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    observacao_devolucao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.colaborador.nome} - {self.equipamento.nome} ({self.status})"
