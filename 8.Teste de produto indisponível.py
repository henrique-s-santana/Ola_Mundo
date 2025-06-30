def teste_produto_indisponivel(): 

    estoque_produto = 0 

     

    if estoque_produto == 0: 

        return "Produto indisponível" 

    else: 

        return "Produto disponível" 

assert teste_produto_indisponivel() == 'Produto disponível', 'Sem estoque'