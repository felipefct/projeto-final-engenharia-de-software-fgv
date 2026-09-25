class TreeNode:
    def __init__(self, nome, idade, telefone, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def inserir(self, nome, idade, telefone, cidade):
        self.root = self._inserir_recursivo(self.root, nome, idade, telefone, cidade)

    def _inserir_recursivo(self, node, nome, idade, telefone, cidade):
        if node is None:
            return TreeNode(nome, idade, telefone, cidade)
        if nome < node.nome:
            node.left = self._inserir_recursivo(node.left, nome, idade, telefone, cidade)
        elif nome > node.nome:
            node.right = self._inserir_recursivo(node.right, nome, idade, telefone, cidade)
        return node

    def buscar(self, nome):
        return self._buscar_recursivo(self.root, nome)

    def _buscar_recursivo(self, node, nome):
        if node is None or node.nome == nome:
            return node
        if nome < node.nome:
            return self._buscar_recursivo(node.left, nome)
        return self._buscar_recursivo(node.right, nome)

    def min_node(self, node):
        atual = node
        while atual and atual.left is not None:
            atual = atual.left
        return atual

    def max_node(self, node):
        atual = node
        while atual and atual.right is not None:
            atual = atual.right
        return atual

    def descadastrar(self, nome):
        self.root = self._remover_recursivo(self.root, nome)

    def _remover_recursivo(self, node, nome):
        if node is None:
            return node
        if nome < node.nome:
            node.left = self._remover_recursivo(node.left, nome)
        elif nome > node.nome:
            node.right = self._remover_recursivo(node.right, nome)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.min_node(node.right)
            node.nome = temp.nome
            node.idade = temp.idade
            node.telefone = temp.telefone
            node.cidade = temp.cidade
            node.right = self._remover_recursivo(node.right, temp.nome)
        return node

    def obter_todos(self):
        lista = []
        self._inorder(self.root, lista)
        return lista

    def _inorder(self, node, lista):
        if node:
            self._inorder(node.left, lista)
            lista.append(node)
            self._inorder(node.right, lista)

def converter_lista_para_bst(lista_encadeada):
    bst = BST()
    atual = lista_encadeada.head
    while atual:
        bst.inserir(atual.nome, atual.idade, atual.telefone, atual.cidade)
        atual = atual.next
    return bst