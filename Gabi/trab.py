
#Model
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


#View

def exibir_mensagem(mensagem):
    print(mensagem)

def obter_entrada(mensagem):
    return input(mensagem)

#Model Cadastro de Livros

def cadastro_livros(livro, lista_livros):
    livro = livro.upper()
    if livro not in lista_livros:
        lista_livros.append(livro)
        return True
    return False

#Controller Cadastro de Livros

def cadastrar_livro_controller_v3():
    livros_para_cadastrar = [ ]
    while True:
        livro_novo = obter_entrada("Digite o nome do livro (ou 'FINALIZAR' para encerrar): ")
        if livro_novo == 'FINALIZAR':
            break
        livros_para_cadastrar.append(livro_novo)

    for livro in livros_para_cadastrar:
        if cadastro_livros(livro, livros):
            exibir_mensagem(f"Livro '{livro}' cadastrado com sucesso!")
        else:
            exibir_mensagem(f"Livro '{livro}' já cadastrado")

    exibir_mensagem(list(reversed(livros)))

#Model Pesquisa de Livros
def pesquisar_livro(livro):
    livro = livro.upper()
    if livro in livros:
        return True
    return False

#Controll Pesquisa Livros

def pesquisa_livro_controller():
    livros = obter_entrada("Qual Livro Você quer Pesquisar Hoje? ")

    if livros in livros:
        exibir_mensagem(f"Livro {livros} Encontrado!")
    else:
        exibir_mensagem("Livro não encontrado!")

pesquisa_livro_controller()

#lapidar as coisas