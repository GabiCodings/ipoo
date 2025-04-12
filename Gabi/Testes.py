livros = [
    "DOM CASMURRO",
    "O GUARANI",
    "MEMÓRIAS PÓSTUMAS DE BRÁS CUBAS",
    "A MORENINHA",
    "VIDAS SECAS",
    "O CORTIÇO",
    "CAPITÃES DA AREIA",
    "A HORA DA ESTRELA",
    "IRACEMA",
    "O PRIMO BASÍLIO"
]

#separando a view
def exibir_mensagem(mensagem):
    
    print(mensagem)

def obter_entrada(mensagem):
    return input(mensagem)

#separando a model
def adicionar_livro(livro, lista_livros):
    livro = livro.upper()
    if livro not in lista_livros:
        lista_livros.append(livro)
        return True
    return False

#separado comtroller
def cadastrar_livro_controller():
    livro_novo = obter_entrada("Digite nome do livro: ")

    if adicionar_livro(livro_novo, livros):
        exibir_mensagem("Livro cadastrado com sucesso!")
    else:
        exibir_mensagem("Livro já cadastrado")

    exibir_mensagem(list(reversed(livros)))

#model
def pesquisar_livro(livro):
    livro = livro.upper()
    if livro in livros:
        return True
    else:
        return False
    
#controller
def pesquisar_livro_controller():
    livro = obter_entrada("informe o titulo do livro: ")
    if pesquisar_livro(livro) in livros:
        exibir_mensagem("Livro encontrado: ", pesquisar_livro(livro))
    else:
        exibir_mensagem("Livro não encontrado")

#model
def excluir_livro(livro):
    livro = livro.upper()
    if livro in livros:
        return True
    else:
        return False
    
#controller
def excluir_livro_controller():
    livro = obter_entrada("informe o livro: ").opper()
    if excluir_livro(livro) in livros:
        exibir_mensagem("livro excluido com sucesso", excluir_livro(livro))
    else:
        exibir_mensagem("livro não encontrado")
#model
def modificar_livro(antigo_valor,novo_valor):
    i = livros.index(antigo_valor)
    try:
        livros[i] = novo_valor
        return True
    except ValueError:
        return False

def modificar_livro_controller():
    antigo_valor = obter_entrada("informe o livro: ").opper()
    novo_valor = obter_entrada("informe o novo valor: ").opper()
    if modificar_livro in livros:
        exibir_mensagem("modificado com sucesso", modificar_livro(antigo_valor,novo_valor))
    else:
        exibir_mensagem("livro não encontrado")
