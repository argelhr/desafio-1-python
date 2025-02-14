# Missão 1: Restaurando as Regras Escolares 📝
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema,
# sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6)
# ou reprovado (nota menor ou igual à 5).
from string import whitespace

print("Missão 1")
nota = float(input("Digite a nota do aluno: (de 0 a 10)"))

while nota < 0 or nota > 10:
    print("Informe uma nota válida!")
    nota = float(input("Digite a nota do aluno: (de 0 a 10)"))

resultado = "Aprovado" if nota >= 6 else "Reprovado"
print(f"O aluno está {resultado}.")

# Missão 2: O Sistema Eleitoral Secreto 📝
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação
# de elegibilidade para votar!
# Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

print("\nMissão 2")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente.")
        else:
            break
    except ValueError:
        print("Por favor, digite um número válido para a idade.")

print("Pode votar" if idade >= 16 else "Não pode votar")

# Missão 3: Recuperando o Sistema de Notas 📊
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram
# um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e
# imprima sua classificação conforme a escala:
#
# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

print("\nMissão 3")

while True:
    try:
        nota = float(input("informe a nota do aluno: de (0 a 100)"))

        if nota < 0 or nota > 100:
            print("informe uma nota válida")
            continue

        if nota >= 90:
            print("Parabéns, você tirou A!")
        elif nota >= 80:
            print("Muito bem, você tirou B.")
        elif nota >= 70:
            print("Bom trabalho, você tirou C.")
        elif nota >= 60:
            print("Fique atento, você tirou D.")
        else:
            print("Estude um pouco mais, você tirou F.")
        break
    except ValueError:
        print("por favor digite um número válido")

# Missão 4: Restaurando a Identificação de Números ⚖️
# Os robôs da escola precisam identificar padrões numéricos para resolver cálculos e otimizar os sistemas. No entanto,
# o vírus bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!
# Crie um programa que peça dois números ao usuário e exiba a soma deles.

print("\nMissão 4")

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"A soma dos números é: {num1 + num2}")
        break
    except ValueError:
        print("Por favor, digite apenas números válidos.")


# Missão 5: Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha!
# Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

print("\nMissão 5")
senha_secreta = "Python123"

while True:
    senha = input("Informe a senha: ")
    if senha == senha_secreta:
        print("Pode acessar")
        break
    else:
        print("Senha incorreta, tente novamente.")


# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
# O vírus está comprometendo o sistema de segurança e a contagem de registros!
# Para restaurar o funcionamento correto, você precisa reforçar as verificações e garantir que os dados
# sejam processados corretamente.
# Exiba os números de 1 a 10 usando um loop while.

print("\nMissao 6")

i = 1
while i <= 10:
    print(i)
    i += 1


# Missão 7: Organizando a Lista📋
# Os números estão misturados e precisam ser organizados!
# Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5,
# armazená-los em uma lista e depois exibi-los em ordem crescente. Isso ajudará a colocar tudo em ordem corretamente!
print("\nMissão 7")
numeros = [8, 3, 10, 1, 5]
numeros.sort()
print(numeros)

# Missão 8: Acessando os Registros de Alunos 🏷️
# O sistema de alunos está desordenado! Para acessar as informações corretamente, você precisa organizar os dados.
# Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.
print("\nMissão 8")
tupla_com_nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print(f"primeiro:{tupla_com_nomes[0]}")
print(f"ultimo: {tupla_com_nomes[-1]}")


# Missão 9: Calculando Dobro de um Número 🛠️
# Os alunos precisam de um programa que ajude em cálculos rápidos.
# Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
# ➡️ Exemplo: dobro(5)
# ➡️ Saída: "O dobro de 5 é 10"

print("\nMissão 9")

def dobro(numero):
    return numero * 2

while True:
    try:
        numero = input("Digite um número para calcular o dobro: ")
        numero = float(numero)
        break
    except ValueError:
        print("Por favor, digite um número válido.")

print(f"O dobro de {numero} é {dobro(numero)}")

# Missão 10: Contando Letras 🔄
# O sistema precisa contar quantas letras há em um nome.
# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"

print("\nMissão 10")
def contar_letras(palavra):
    return len(palavra)

while True:
    nome = input("Informe um nome: ")
    if nome.strip():
        break
    else:
        print("Por favor, digite um nome válido.")

print(f"O nome {nome} tem {contar_letras(nome)} letras.")
