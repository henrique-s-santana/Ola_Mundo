def teste_saldo_insuficiente(): 

    saldo = 100 

    saque = 150 

     

    if saque > saldo: 

        return "Saldo insuficiente" 

    else: 

        return "Saque realizado" 

assert teste_saldo_insuficiente() == 'Saque realizado', 'O saque está acima do saldo'