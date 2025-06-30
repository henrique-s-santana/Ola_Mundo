def teste_cpf_invalido(): 

    cpf = "12345678900" 

     

    if len(cpf) != 11: 

        return "CPF inválido" 

    else: 

        return "CPF válido" 

assert teste_cpf_invalido() == 'CPF válido', 'CPF completo'