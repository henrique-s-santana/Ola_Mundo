def teste_senha_muito_curta(): 

    senha = "123" 

     

    if len(senha) < 6: 

        return "Senha muito curta" 

    else: 

        return "Senha válida" 

assert teste_senha_muito_curta() == 'Senha válida', 'Caracteres insuficientes'