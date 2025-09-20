from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Colaboradores
    path('colaboradores/', views.lista_colaboradores, name='colaboradores_list'),
    path('colaboradores/novo/', views.criar_colaborador, name='criar_colaborador'),
    path('colaboradores/<int:id>/editar/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/<int:id>/excluir/', views.excluir_colaborador, name='excluir_colaborador'),

    # Equipamentos
    path('equipamentos/', views.lista_equipamentos, name='equipamentos_list'),
    path('equipamentos/novo/', views.criar_equipamento, name='criar_equipamento'),
    path('equipamentos/<int:id>/editar/', views.editar_equipamento, name='editar_equipamento'),
    path('equipamentos/<int:id>/excluir/', views.excluir_equipamento, name='excluir_equipamento'),

    # Empréstimos
    path('emprestimos/', views.lista_emprestimos, name='emprestimos_list'),
    path('emprestimos/novo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('emprestimos/<int:id>/editar/', views.editar_emprestimo, name='editar_emprestimo'),
    path('emprestimos/<int:id>/excluir/', views.excluir_emprestimo, name='excluir_emprestimo'),
]

