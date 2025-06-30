def teste_formato_telefone_invalido(): 

    telefone = "12345" 

     

    if len(telefone) != 10: 

        return "Formato de telefone inválido" 

    else: 

        return "Telefone válido" 

assert teste_formato_telefone_invalido() == 'Telefone válido', 'Números Insuficientes'