# Classe com a função construtora 
class Fornecedor:
    def __init__(self, codigo, nome, telefone, email):
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.email = email


# Classe para gerenciar a lista de fornecedores e criar uma lista vazia  
class CadastroFornecedores:
    def __init__(self):
        self.fornecedores = []

# Adiciona o metodo para adicionar os fornecedores sempre ao fim da lista 
    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)
        print("Fornecedor adicionado com sucesso.")


# Agora um método para remover um fornecedor, usando um loop para percorrer a lista, identificando pelo código do mesmo, e uma condicional para verificar qual fornecedor será removido    
    def remover_fornecedor(self, codigo):
        for fornecedor in self.fornecedores:
            if fornecedor.codigo == codigo:
                self.fornecedores.remove(fornecedor)
                print("Fornecedor removido com sucesso.")
            else:
        print("Fornecedor não encontrado.")


# metodo para exibir o fornecedor a partir do código
    def exibir_fornecedor(self, codigo):
        for fornecedor in self.fornecedores:
            if fornecedor.codigo == codigo:
                print("Código: ", fornecedor.codigo)
                print("Nome: ", fornecedor.nome)
                print("Telefone: ", fornecedor.telefone)
                print("Email: ", fornecedor.email)
            else:
        print("Fornecedor não encontrado.")

# Agora instanciamos a classe cadastroFornecedores para utilização dos seus atributos e metodos
cadastro = CadastroFornecedores()

# Para criar o menu, usamos o loop while porque não sabemos quantas vezes um fornecedor será adicionado,  
while True:
    print(" MENU ")
    print("1 - Adicionar fornecedor")
    print("2 - Remover fornecedor")
    print("3 - Exibir informações de fornecedor")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

# Por fim, colocamos as condicionais solicitando que o usuário digite as informações necessárias do fornecedor  
    if opcao == "1":
        codigo = input("Digite o código do fornecedor: ")
        nome = input("Digite o nome do fornecedor: ")
        telefone = input("Digite o telefone do fornecedor: ")
        email = input("Digite o email do fornecedor: ")

# Permite que as informações do fornecedor digitadas sejam adicionadas na lista, chamando o método adicionar_fornecedor         
        fornecedor = Fornecedor(codigo, nome, telefone, email)
        cadastro.adicionar_fornecedor(fornecedor)

# agora, criamos as condicionais para remover, exibir e fechar o programa. 
    elif opcao == "2":
        codigo = input("Digite o código do fornecedor a ser removido: ")
        cadastro.remover_fornecedor(codigo)

    elif opcao == "3":
        codigo = input("Digite o código do fornecedor a ser exibido: ")
        cadastro.exibir_fornecedor(codigo)

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")

