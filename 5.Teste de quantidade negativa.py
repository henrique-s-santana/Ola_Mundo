def teste_quantidade_negativa(): 

    quantidade = -10 

     

    if quantidade < 0: 

        return "Quantidade inválida" 

    else: 

        return "Quantidade válida"
    
assert teste_quantidade_negativa() == 'Quantidade válida', 'Quantidade menor que 0!'