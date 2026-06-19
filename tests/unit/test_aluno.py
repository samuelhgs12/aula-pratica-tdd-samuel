import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno
from aluno.aluno import contar_aprovados
from aluno.aluno import situacao_final

# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================
def test_calcular_media():
    aluno = Aluno(nome = "Samuel", notas = [7, 8, 9], faltas = 8)
    assert aluno.calcular_media() == 8.0

def test_situacao_aluno_aprovado():
    aluno = Aluno(nome = "Paulo", notas = [7, 4, 7], faltas = 1)
    assert aluno.situacao() == "Aprovado"

def test_situacao_aluno_reprovado():
    aluno = Aluno(nome = "Maria", notas = [5, 4, 3], faltas = 2)
    assert aluno.situacao() == "Reprovado"

def test_menor_nota():
    aluno = Aluno(nome = "Gustavo", notas = [2, 4, 9], faltas = 8)
    assert aluno.menor_nota() == 2

def test_maior_nota():
    aluno = Aluno(nome = "Gustavo", notas = [2, 4, 9], faltas = 8)
    assert aluno.maior_nota() == 9

def test_calcular_media_arredondada():
    aluno = Aluno(nome = "José", notas = [5, 6, 6, 6], faltas = 4)
    assert aluno.calcular_media_arredondada() == 6
# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função
def test_contar_todos_aprovados():
    alunos = [
        Aluno(nome = "Samuel", notas = [7, 8, 9], faltas = 8),
        Aluno(nome = "Paulo", notas = [7, 4, 7], faltas = 1),
        Aluno(nome = "Maria", notas = [10, 10, 3], faltas = 2)
    ]
    assert contar_aprovados(alunos) == 3

def test_contar_todos_reprovados():
    alunos = [
        Aluno(nome = "Samuel", notas = [5, 4, 3], faltas = 8),
        Aluno(nome = "Paulo", notas = [5, 4, 3], faltas = 1),
        Aluno(nome = "Maria", notas = [5, 4, 3], faltas = 2)
    ]
    assert contar_aprovados(alunos) == 0

def test_contar_mistos():
    alunos = [
        Aluno(nome = "Samuel", notas = [5, 4, 3], faltas = 8),
        Aluno(nome = "Paulo", notas = [7, 4, 7], faltas = 1),
        Aluno(nome = "Maria", notas = [10, 10, 3], faltas = 2)
    ]
    assert contar_aprovados(alunos) == 2

def test_contar_lista_vazia():
    alunos = []
    assert contar_aprovados(alunos) == 0
# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método
def test_situacao_final_reprovado_com_faltas():
    aluno = Aluno(nome = "Lucas", notas = [7, 8, 9], faltas = 20)
    assert aluno.situacao_final(total_aulas=40) == "Reprovado"

def test_situacao_final_aprovado():
    aluno = Aluno(nome = "Ana", notas = [7, 8, 9], faltas = 10)
    assert aluno.situacao_final(total_aulas=40) == "Aprovado"

# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
