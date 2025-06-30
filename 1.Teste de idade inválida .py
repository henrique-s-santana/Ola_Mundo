def teste_idade_invalida(): 

    idade = -5 

     

    if idade < 0: 

        return "Idade inválida" 

    else: 

        return "Idade válida" 

assert teste_idade_invalida() == 'Idade válida','A idade não existe!'

    
