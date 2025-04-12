
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


#Controller

def exibir_mensagem(mensagem):
    print(mensagem)

def obter_entrada(mensagem):
    return input(mensagem)

def cadastro_controller (livros, livro_novo):
    obter_entrada("Qual livro você quer cadastrar? ")
    if obter_entrada not in livros:
        livros.append(livro_novo.upper())
        exibir_mensagem("Cadastrado com sucesso!")
    else:
        exibir_mensagem("Livro já cadastrado")

#View
cadastro_controller(livros, livro_novo)
