def cadastrar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso!")
    return
    
def ver_contato(contatos):
    print("_____________________")
    print("\nLista de Contatos: ")
    print("_________________________________________________________________________")
    for indice, contato in enumerate(contatos, start=1):
        status = "[favorito]" if contato["favorito"] else ""
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. {status} Nome: {nome_contato}\n       Telefone: {telefone_contato}\n       Email: {email_contato}\n")
        print("_________________________________________________________________________")
    return



def atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email
        print(f"Contato {indice_contato} atualizada para {novo_nome}, Telefone: {novo_telefone}, email: {novo_email}")
    else:
        print("Índice contato inválido.")
    return contatos

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} marcado como favorito")
    return

def ver_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato["favorito"]]
    
    if favoritos:
        print("\nContatos Favoritos:")
        for indice, contato in enumerate(favoritos, start=1):
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(f"{indice}. Nome: {nome_contato}\n   Telefone: {telefone_contato}\n   Email: {email_contato}\n")
    else:
        print("\nNenhum contato marcado como favorito.")
            
def deletar_contato(contatos):
    ver_contato(contatos)
    indice_remover = int(input("Qual contato deseja remover? ")) - 1
    
    if indice_remover >= 0 and indice_remover < len(contatos):
        contatos.pop(indice_remover)
        print("Contato Deletado.")
    else:
        print("Índice inválido, nenhum contato foi removido.")

    return contatos

def remover_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    
    if 0 <= indice_contato_ajustado < len(contatos):
        if contatos[indice_contato_ajustado]["favorito"]:
           contatos[indice_contato_ajustado]["favorito"] = False
           print(f"Contato {indice_contato} removido dos favoritos.")
        else:
            print(f"O contato {indice_contato} não estava marcado como favorito.")
    else:
        print("Índice de contato inválido.")
    
    return contatos

contatos = []
    
while True:    
    print("\nMenu do Gerenciador de contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Adicionar contato aos favoritos")
    print("5. Ver apenas contatos favoritos")
    print("6. Deletar contato")
    print("7. Retirar contato dos favoritos")
    print("8. Sair")
    
    escolha = input("Digite a sua escolha:")
    
    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone do contato: ")
        email_contato = input("Digite o email do contato: ")
        cadastrar_contato(contatos ,nome_contato, telefone_contato, email_contato)

    elif escolha == "2":
        ver_contato(contatos)
            
    elif escolha == "3":
            ver_contato(contatos)
            indice_contato = input("Digite o número do contato que deseja atualizar: ")
            novo_nome = input("Digite o novo nome do contato: ")
            novo_telefone = input("Digite o novo telefone do contato: ")
            novo_email = input("Digite o novo email do contato: ")
            contatos = atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)                   
        
    elif escolha == "4":
            ver_contato(contatos)
            indice_contato = input("Qual contato deseja favoritar: ")
            favoritar_contato(contatos, indice_contato)
            
    elif escolha == "5":
        ver_favoritos(contatos)
        
    elif escolha == "6":
            deletar_contato(contatos)
            ver_contato(contatos)
            
    elif escolha == "7":
        ver_favoritos(contatos)
        indice_contato = input("Digite o número do contato que deseja remover dos favoritos: ")
        contatos = remover_favorito(contatos, indice_contato)
        
    elif escolha == "8":
        break
    

print("Programa finalizado")