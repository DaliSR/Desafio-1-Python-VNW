# Missão 1: Restaurando as Regras Escolares
# O vírus apagou os critérios de aprovação dos alunos!
# Para ajudar o Professor Byte a organizar o sistema,
#  sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6)
# ou reprovado (nota menor ou igual à 5).

nota_do_aluno = float(input("Digite a nota do aluno: "))
if nota_do_aluno >= 6:
    print("Aluno aprovado! Parabéns!")
else:
    print("Aluno reprovado!")


# Missão 2: O Sistema Eleitoral Secreto
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações,
# mas o vírus desativou a verificação de elegibilidade para votar!
#  Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade_do_usuario = int(input("Digite a idade do usuário:"))
if idade_do_usuario >= 16:
    print("Pode votar!")
else:
    print("Não pode votar!")


# Missão 3: Recuperando o Sistema de Notas
# As classificações das provas desapareceram!
#  Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F .
# Antes que o pânico se espalhe,
#  sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."
nota_do_aluno = int(input("Digite a nota do aluno (0-100):"))
if nota_do_aluno >= 90:
    print("Parabéns, você tirou A!")
elif nota_do_aluno >= 80 and nota_do_aluno <= 89:
    print("Muito bem, você tirou B.")
elif nota_do_aluno >= 70 and nota_do_aluno <= 79:
    print("Bom trabalho, você tirou C.")
elif nota_do_aluno >= 60 and nota_do_aluno <= 69:
    print("Fique atento, você tirou D.")
elif nota_do_aluno < 60:
    print("Estude um pouco mais, você tirou F.")


# Missão 4: Restaurando a Identificação de Números
# Os robôs da escola precisam identificar padrões numéricos para resolver
# cálculos e otimizar os sistemas. No entanto, o vírus bagunçou os algoritmos
# e agora eles não conseguem mais somar corretamente!
# Crie um programa que peça dois números ao usuário e exiba a soma deles.
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
soma = num1 + num2
print("a soma dos números é: ", soma)


# Missão 5: Recuperando o Cofre de Segurança
# O cofre da biblioteca guarda códigos raros de programação,
# mas o vírus resetou a senha!
# Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha
# e verifique se ela está correta. A senha correta é "Python123".
senha_correta = "Python123"
senha = input("Digite a senha:")

if senha == senha_correta:
    print("Senha correta! Acesso permitido.")
else:
    print("Senha incorreta. Acesso negado.")


# Missão 6: Reforçando a Segurança e a Contagem do Sistema
# O vírus está comprometendo o sistema de segurança e a contagem de registros!
#  Para restaurar o funcionamento correto,
#  você precisa reforçar as verificações
# e garantir que os dados sejam processados corretamente.
# Exiba os números de 1 a 10 usando um loop while.
numero = 1
while numero <= 10:
    print(numero)
    numero += 1

# Missão 7: Organizando a Lista
# Os números estão misturados e precisam ser organizados!
# Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente.
# Isso ajudará a colocar tudo em ordem corretamente!
numeros = [8, 3, 10, 1, 5]
numeros.sort()
print("Números em ordem crescente:", numeros)


# Missão 8: Acessando os Registros de Alunos
# O sistema de alunos está desordenado!
# Para acessar as informações corretamente,
# você precisa organizar os dados.
# Crie uma tupla com os seguintes nomes:
# Ana, Bruno, Carla, Daniel, Eduardo e exiba  o primeiro e o último nome.
nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print("Primeiro nome:", nomes[0])
print("Último nome:", nomes[-1])


# Missão 9: Calculando Dobro de um Número
# Os alunos precisam de um programa que ajude em cálculos rápidos.
# Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
# Exemplo: dobro(5)
# Saída: "O dobro de 5 é 10"
def dobro(numero):
    return numero * 2


numero = float(input("Digite um numero:"))
resultado = dobro(numero)
print(f"O dobro de {numero} é {resultado}")


# Missão 10: Contando Letras
# O sistema precisa contar quantas letras há em um nome.
# Crie uma função que receba um nome e diga quantas letras esse nome tem.
# Exemplo: contar_letras("Ana")
# Saída:" O nome Ana tem 3 letras"
def contar_letras(nome):
    return len(nome)


nome = input("Digite um nome:")
quantidade_letras = contar_letras(nome)
print(f"O nome {nome} tem {quantidade_letras} letras.")
