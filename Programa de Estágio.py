import os
os.system('cls')

print("\n")
print("=" * 100)
print("                           Seleção para Programa de Estágio ")
print("=" * 100)
print("\n")

def formacao (a,b,c):

    if  a.upper()!="SIM"  and  b.upper()!="SIM" and  c.upper()!="SIM":

        return "Infelizmente vc não possui todos os requisitos exigidos da vaga!"

    else:

        return "Parabéns você foi aprovado para a vaga!"
#A
while True:
    fa=str(input("Você possui formação na área de T.I? "))
    if fa.lower()=='sim' or 'não':
        break

print("\n")
print("=" * 100)
print("\n")

#B
clp=str(input("Você possui conhecimento das linguagens Python, Java e C++? "))

print("\n")
print("=" * 100)
print("\n")

#C
de=str(input("Você possui disponibilidade para trabalhar pelo menos 20 horas por semana? "))

print("\n")
print("=" * 100)
print("\n")

print(f"{formacao(fa,clp,de)}")
print("\n")