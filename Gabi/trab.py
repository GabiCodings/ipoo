
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

def obter_entrada_int(mensagem):
    return int(input(mensagem))

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
    return menu_entrada()

#Model Pesquisa de Livros
def pesquisar_livro(livro):
    livro = livro.upper()
    if livro in livros:
        return True
    return False

#Controll Pesquisa Livros

def pesquisa_livro_controller():
    exibir_mensagem("Para voltar digite 'MENU'")

    livro_pesquisa = obter_entrada("Qual Livro Você quer Pesquisar Hoje? ").upper()

    if livro_pesquisa in livros:
        posicao = livros.index(livro_pesquisa)
        exibir_mensagem(f"Livro: {livro_pesquisa} Encontrado! Na posição {posicao + 1}")
        exibir_mensagem(list(livros)) 
        return pesquisa_livro_controller()
    elif livro_pesquisa == 'MENU':
        return menu_entrada()
    
    else:
        exibir_mensagem("Livro não encontrado!")
        return pesquisa_livro_controller()



#Model Excluir Livros

def excluir_livro(livro):
    livro = livro.upper()
    if livro in livros:
        return True
    return False

#Controller Excluir Livro

def excluir_livros_controller():
    exibir_mensagem("Para voltar digite 'MENU'")

    livro_excluir = obter_entrada("Qual o titulo do livro que você deseja excluir? ").upper()
    
    if livro_excluir in livros:
        livros.remove(livro_excluir)
        exibir_mensagem("Livro Excluido!")
        exibir_mensagem(list(reversed(livros)))
        return excluir_livros_controller()
    elif livro_excluir == 'MENU':
        return menu_entrada()
    else:
        exibir_mensagem("Livro não encontrado.")
        return excluir_livros_controller()
    
    


#Model Modificar Livro

def modificar_livro_model(livro):
    livro = livro.upper()
    if livro in livros:
        return True
    return False

#Controller Modificar Livro

def modificar_livro_controller():
    exibir_mensagem("Para voltar digite 'MENU'")
    modificar_livro = obter_entrada("Qual Livro você deseja modificar? ").upper()
    

    if modificar_livro in livros:

        novo_valor = obter_entrada("Qual o novo titulo do livro? ").upper()
        i = livros.index(modificar_livro)
        livros[i] = novo_valor
        exibir_mensagem(list(livros))
        return modificar_livro_controller()
    
    elif modificar_livro == 'MENU':
        return menu_entrada()
    else:
        exibir_mensagem("Livro não encontrado para modificação")
        return modificar_livro_controller()

    

    

def menu_entrada():
        exibir_mensagem("MENU DE ENTRADA:\n 1. Adicionar um Livro\n 2. Pesquisar Livro \n 3. Excluir Livro \n 4. Modificar Livro")
        valor = obter_entrada_int("O que você deseja fazer? \n")

        if valor == 1:
            cadastrar_livro_controller_v3()

        elif valor == 2:
            pesquisa_livro_controller()

        elif valor == 3:
            excluir_livros_controller()

        elif valor == 4:
            modificar_livro_controller()
            
        else:
            exibir_mensagem("Não temos essa funcão ainda...")
            return menu_entrada()


menu_entrada()
