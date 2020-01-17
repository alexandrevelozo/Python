ALFABETO = 'abcdefghijklmnopqrstuvwxyzß¶§þÐ╬╩┴¥©ÑƒøÿâÅ£Øª¿▓▒░■§yÆæø¼║¢Ã¤ÐÏ¦*-+/?°:' #vetor de strings
ADD = 26 #constante de soma

def titulo(msg):
  tam = len(msg) + 7
  print('=' * tam)
  print(f'   {msg}')
  print('=' * tam)

def criptografar(message):
    c = ''
    for letra in message:
        
        if letra in ALFABETO:  
            letra_index = ALFABETO.index(letra)#indice da letra no vetor de strings
            c += ALFABETO[(letra_index + ADD)% 70]#primeiro processo da criptografia           
        else:
            c += letra
            
    return c

def descriptografar(message):
    c = ''
    for letra in message:
        
        if letra in ALFABETO:  
            letra_index = ALFABETO.index(letra)#indice da letra no vetor de strings
            c += ALFABETO[(letra_index - ADD)% 70]#primeiro processo da criptografia           
        else:
            c += letra  
                   
    return c 
