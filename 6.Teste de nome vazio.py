def teste_nome_vazio(): 

    nome = "" 

     

    if not nome: 

        return "Nome obrigatório" 

    else: 

        return "Nome válido" 

assert teste_nome_vazio() == 'Nome válido', 'Nome não digitado!'