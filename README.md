# Projeto Final - Estrutura de dados - Felipe de Carvalho - FGV
Sistema de cadastro de reserva escolar em Python, focado em estruturas de dados reais: Lista Encadeada para inclusões da secretaria, Árvore Binária de Busca (BST) para edições da diretoria, e Grafos com Dijkstra para o assistente calcular as menores distâncias entre as cidades.

## Estruturas de Dados Utilizadas
O projeto foi dividido para atender três perfis de funcionários de uma escola no Guarujá/SP, cada um utilizando uma estrutura de dados específica para otimizar suas tarefas:

- **Secretário(a):** Utiliza **Listas Encadeadas Simples** para cadastrar novas pessoas na lista de espera, com associação aleatória de cidades.
- **Diretor(a):** Utiliza **Árvore Binária de Busca (BST)** (onde a chave é o nome) para buscar, editar e descadastrar pessoas de forma eficiente.
- **Assistente:** Utiliza **Grafos Ponderados e Não-Direcionados** juntamente com o **Algoritmo de Dijkstra** para calcular rotas e as menores distâncias entre cidades.

## Como executar o projeto

1. Certifique-se de ter o Python instalado na sua máquina (No MacBook utilizamos o `python3`).
2. Clone o repositório ou baixe os arquivos.
3. No terminal, navegue até a pasta do projeto.
4. Execute o arquivo principal:
   ```bash
   python3 main.py