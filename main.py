import random
from atribuicoes_secretario import ListaEncadeada, carregar_cidades
from atribuicoes_diretor import converter_lista_para_bst
from atribuicoes_assistente import carregar_grafo

def menu_secretario():
    lista = ListaEncadeada()
    cidades_disponiveis = carregar_cidades("cidades_vizinhas.csv")
    
    print("-------- Olá, Secretário(a)! --------")
    while True:
        print("\nVocê deseja:")
        print("(1) Cadastrar nova pessoa na lista de espera.")
        print("(2) Consultar pessoa cadastrada.")
        print("(3) Ver quantidade de pessoas cadastradas.")
        print("(4) Finalizar execução.")
        opcao = input("Digite sua opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome da pessoa: ")
            idade = input("Digite a idade: ")
            telefone = input("Digite o telefone: ")
            cidade = random.choice(cidades_disponiveis) if cidades_disponiveis else "Desconhecida"
            lista.inserir(nome, idade, telefone, cidade)
            print(f"Nome: {nome} | Idade: {idade} | Telefone: {telefone} | Cidade: {cidade}")
        elif opcao == '2':
            nome = input("Digite o nome da pessoa: ")
            pessoa = lista.buscar(nome)
            if pessoa:
                print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
            else:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
        elif opcao == '3':
            qtd = lista.quantidade()
            print(f"São {qtd} pessoas na lista de espera.")
        elif opcao == '4':
            print("Fim das atividades sob responsabilidade do(a) Secretário(a).\n")
            return lista
        else:
            pass

def menu_diretor(lista_encadeada):
    bst = converter_lista_para_bst(lista_encadeada)
    print("-------- Olá, Diretor(a)! --------")
    
    while True:
        print("\nVocê deseja:")
        print("(1) Alterar nome, idade ou telefone de pessoa cadastrada.")
        print("(2) Descadastrar pessoa.")
        print("(3) Obter informações da primeira pessoa em ordem alfabética de nome.")
        print("(4) Obter informações da última pessoa em ordem alfabética de nome.")
        print("(5) Confirmar validade da lista de espera e finalizar execução.")
        opcao = input("Digite sua opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome da pessoa que você quer editar: ")
            pessoa = bst.buscar(nome)
            if pessoa:
                print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
                edit_op = input("O que você quer editar? Digite 1 para nome, 2 para idade ou 3 para telefone: ")
                if edit_op == '1':
                    novo_nome = input("Digite o novo nome: ")
                    idade, telefone, cidade = pessoa.idade, pessoa.telefone, pessoa.cidade
                    bst.descadastrar(nome)
                    bst.inserir(novo_nome, idade, telefone, cidade)
                    print("Dados atualizados com sucesso.")
                elif edit_op == '2':
                    nova_idade = input("Digite a nova idade: ")
                    pessoa.idade = nova_idade
                    print("Dados atualizados com sucesso.")
                elif edit_op == '3':
                    novo_tel = input("Digite o novo telefone: ")
                    pessoa.telefone = novo_tel
                    print("Dados atualizados com sucesso.")
            else:
                print("Pessoa não cadastrada. Tem certeza que o nome está certo?")
        elif opcao == '2':
            nome = input("Digite o nome da pessoa que você quer descadastrar: ")
            pessoa = bst.buscar(nome)
            if pessoa:
                print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
                confirm = input(f"Tem certeza que deseja descadastrar {pessoa.nome}? Digite S ou N: ").upper()
                if confirm == 'S':
                    bst.descadastrar(nome)
                    print(f"{nome} descadastrado com sucesso.")
            else:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
        elif opcao == '3':
            min_node = bst.min_node(bst.root)
            if min_node:
                print(f"Nome: {min_node.nome} | Idade: {min_node.idade} | Telefone: {min_node.telefone} | Cidade: {min_node.cidade}")
        elif opcao == '4':
            max_node = bst.max_node(bst.root)
            if max_node:
                print(f"Nome: {max_node.nome} | Idade: {max_node.idade} | Telefone: {max_node.telefone} | Cidade: {max_node.cidade}")
        elif opcao == '5':
            print("Fim das atividades sob responsabilidade do(a) Diretor(a).\n")
            return bst

def menu_assistente(bst):
    grafo = carregar_grafo("cidades_vizinhas.csv")
    print("-------- Olá, Assistente! --------")
    
    while True:
        print("\nVocê deseja:")
        print("(1) Ver a menor distância entre a cidade da escola e a cidade de uma pessoa.")
        print("(2) Ver a menor distância da cidade da escola até a cidade da pessoa passando por uma cidade específica.")
        print("(3) Ver dados da(s) pessoa(s) que mora(m) na cidade mais perto da cidade da escola (incluindo distância).")
        print("(4) Finalizar execução.")
        opcao = input("Digite sua opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ")
            pessoa = bst.buscar(nome)
            if pessoa:
                print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
                dist, caminho = grafo.dijkstra('Guarujá')
                cidade_destino = pessoa.cidade
                if cidade_destino in caminho:
                    print(f"Menor caminho = {caminho[cidade_destino]} com custo {int(dist[cidade_destino])}")
            else:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
        
        elif opcao == '2':
            nome = input("Digite o nome da pessoa cuja cidade te interessa: ")
            pessoa = bst.buscar(nome)
            if pessoa:
                print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade} | Telefone: {pessoa.telefone} | Cidade: {pessoa.cidade}")
                dist_g, caminho_g = grafo.dijkstra('Guarujá')
                dist_i, caminho_i = grafo.dijkstra('Indaiatuba')
                cidade_destino = pessoa.cidade
                
                if 'Indaiatuba' in caminho_g and cidade_destino in caminho_i:
                    custo_total = dist_g['Indaiatuba'] + dist_i[cidade_destino]
                    caminho_total = caminho_g['Indaiatuba'] + caminho_i[cidade_destino][1:] 
                    print(f"Menor caminho = {caminho_total} com custo {int(custo_total)}")
            else:
                print("Pessoa não cadastrada ou lista de espera vazia. Tem certeza que o nome da pessoa está certo?")
                
        elif opcao == '3':
            pessoas = bst.obter_todos()
            if pessoas:
                dist, _ = grafo.dijkstra('Guarujá')
                cidades_com_moradores = {p.cidade for p in pessoas if p.cidade != 'Guarujá'}
                cidade_mais_proxima = None
                menor_dist = float('inf')
                
                for c in cidades_com_moradores:
                    if c in dist and dist[c] < menor_dist:
                        menor_dist = dist[c]
                        cidade_mais_proxima = c
                        
                if cidade_mais_proxima:
                    print(f"A cidade mais próxima à cidade da escola que tem moradores na lista de espera (ver abaixo) é {cidade_mais_proxima}. Distância = {int(menor_dist)}")
                    for p in pessoas:
                        if p.cidade == cidade_mais_proxima:
                            print(f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | Cidade: {p.cidade}")
        
        elif opcao == '4':
            break

if __name__ == "__main__":
    lista = menu_secretario()
    bst = menu_diretor(lista)
    menu_assistente(bst)