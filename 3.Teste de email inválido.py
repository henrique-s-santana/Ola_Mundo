def teste_email_invalido(): 

    email = "usuarioatividade.com" 

     

    if "@" not in email: 

        return "Email inválido" 

    else: 

        return "Email válido" 

assert teste_email_invalido() == 'Email válido', 'Faltou o @!'