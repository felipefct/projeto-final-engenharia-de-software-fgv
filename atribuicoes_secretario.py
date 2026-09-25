import csv
import random

class Node:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, nome, idade, telefone, cidade):
        novo = Node(nome, idade, telefone, cidade)
        if not self.head:
            self.head = novo
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = novo

    def buscar(self, nome):
        atual = self.head
        while atual:
            if atual.nome == nome:
                return atual
            atual = atual.next
        return None

    def quantidade(self):
        count = 0
        atual = self.head
        while atual:
            count += 1
            atual = atual.next
        return count

def carregar_cidades(nome_arquivo):
    cidades = set()
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as f:
            linha = f.readline()
            f.seek(0)
            sep = ';' if ';' in linha else ','
            reader = csv.reader(f, delimiter=sep)
            for row in reader:
                if len(row) >= 2:
                    cidades.add(row[0].strip())
                    cidades.add(row[1].strip())
    except FileNotFoundError:
        print("Erro: Arquivo cidades_vizinhas.csv não encontrado.")
    return list(cidades)