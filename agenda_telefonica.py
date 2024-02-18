def adicionar_contato(agenda, contato):
    agenda.append(contato)
    print("Contato adicionado com sucesso!")
    return

def visualizar_agenda(agenda):
    for indice, contato in enumerate(agenda):
        posicao = indice + 1
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = "⭐️" if contato["favorito"] else ""
        print(f"{posicao}{favorito}. Nome: {nome} - Telefone: {telefone} - E-mail: {email}")
    return

def editar_contato(agenda, posicao, contato):
    indice = posicao - 1
    agenda[indice]["nome"] = contato["nome"]
    agenda[indice]["telefone"] = contato["telefone"]
    agenda[indice]["email"] = contato["email"]
    print("Contato editado com sucesso!")
    return

def alterar_favorito_contato(agenda, posicao):
    indice = posicao - 1
    agenda[indice]["favorito"] = False if agenda[indice]["favorito"] else True
    if agenda[indice]["favorito"]:
        print("Contato favoritado com sucesso!")
    else:
        print("Contato desfavoritado com sucesso!")
    return

def visualizar_favoritos(agenda):
    for indice, contato in enumerate(agenda):
        if contato["favorito"]:
            posicao = indice + 1
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{posicao}⭐️. Nome: {nome} - Telefone: {telefone} - E-mail: {email}")
    return

def apagar_contato(agenda, posicao):
    indice = posicao - 1
    agenda.pop(indice)
    print("Contato excluído com sucesso!")
    return

agenda = []
while True:
    print("\nAgenda telefônica\n" 
          "1. Adicionar contato\n"
          "2. Visualizar agenda\n"
          "3. Editar contato\n"
          "4. Favoritar/desfavoritar contato\n"
          "5. Ver contatos favoritos\n"
          "6. Apagar contato\n"
          "7. Sair")

    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            contato = {"favorito": False}
            contato["nome"] = input("Digite o nome: ")
            contato["telefone"] = input("Digite o telefone: ")
            contato["email"] = input("Digite o e-mail: ")
            adicionar_contato(agenda, contato)
        elif opcao == 2:
            visualizar_agenda(agenda)
        elif opcao == 3:
            visualizar_agenda(agenda)
            posicao = int(input("Digite o código do contato: "))
            contato = {}
            contato["nome"] = input("Digite o nome: ")
            contato["telefone"] = input("Digite o telefone: ")
            contato["email"] = input("Digite o e-mail: ")
            editar_contato(agenda, posicao, contato)
        elif opcao == 4:
            visualizar_agenda(agenda)
            posicao = int(input("Digite o código do contato: "))
            alterar_favorito_contato(agenda, posicao)
        elif opcao == 5:
            visualizar_favoritos(agenda)
        elif opcao == 6:
            visualizar_agenda(agenda)
            posicao = int(input("Digite o código do contato: "))
            apagar_contato(agenda, posicao)
        elif opcao == 7:
            print("Até mais! 👋")
            break
    except Exception as e:
        print("Ah, ocorreu um erro! Vamos tentar novamente.")