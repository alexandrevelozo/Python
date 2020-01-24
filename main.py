from os import system
from time import sleep
import getpass
from users import user
import criptografia

def main():
      
    while(True):
        system('cls')
        criptografia.titulo('    Login    ')
        name = input('User: ')
        senha = getpass.getpass(('Password: '))
        x = criptografia.criptografar((senha))

        if ((name in user.keys()) and (x in user.values())):
            print(f'Bem vindo {name}')
            print('Tecle ENTER para iniciar..')
            input()
            break
        else:
            print('User or Password Incorrect')
            input()               
main() 

    # Menu
while(True):
    system('cls')
    criptografia.titulo('Sistema de Criptografia')
    print('1 - Criptografar')
    print('2 - Descriptografar')
    print('3 - Sair')
        
    op = int(input('Digite a opção escolhida: '))

    while( (op<1) or (op>3) ):
        print('Opção inválida!')
        op = int(input('Digite a opção escolhida: '))
    if (op == 1):
        text = str(input('Digite o texto a ser criptografado: '))
        print('Processando...')
        sleep(1)
        print('Aguarde..')
        sleep(2)
        print('Mensagem criptografada: ', criptografia.criptografar(text))
        input()
    elif (op == 2):
        text = str(input('Digite o texto a ser descriptografado: '))
        print('Processando...')
        sleep(1)
        print('Aguarde..')
        sleep(2)
        print('Mensagem descriptografada: ', criptografia.descriptografar(text))
        input()
    elif (op == 3):
        break                       
 