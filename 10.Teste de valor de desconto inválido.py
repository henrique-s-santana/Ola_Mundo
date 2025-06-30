def teste_desconto_invalido(): 

    desconto = -10 

     

    if desconto < 0 or desconto > 100: 

        return "Desconto inválido" 

    else: 

        return "Desconto aplicado" 
    
assert teste_desconto_invalido() == 'Desconto aplicado', 'Desconto inexistente'