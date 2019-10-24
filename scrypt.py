alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

chave = 3
mensagem = input('O que você deseja criptografar?: ')
mensagem = mensagem.lower()
# Tamanho lista alfabeto
# n = len(alfabeto)
# Tamanho tabela ASCII
n = len(alfabeto)

cifrada = ''
for letra in mensagem:
    indice = ord(letra)
    indice = alfabeto.index(letra)
    nova_letra = chr((indice + chave)%n)
    cifrada = cifrada + nova_letra

print(mensagem)    
print(cifrada)
