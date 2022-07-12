import random

def mostra_pista(pinos):
    for elemento in pista:
        print(elemento, end = "")
    print()    

pista = ['I', ' ', 'I', ' ', 'I', ' ', 'I', ' ', 'I', '\n', 
' ', 'I', ' ', 'I', ' ', 'I', ' ', 'I', '\n',
' ', ' ', 'I', ' ', 'I', ' ', 'I', '\n',
' ', ' ', ' ', 'I', ' ', 'I', '\n',
' ', ' ', ' ', ' ','I', '\n',
]
 
posiçao_dos_pinos = {
    '1':38,
    '2':32,
    '3':30,
    '4':25,
    '5':23,
    '6':21,
    '7':17,
    '8':15,
    '9':13,
    '10':11,
    '11':8,
    '12':6,
    '13':4,
    '14':2,           
    '15':0              
     
}

mostra_pista(pista)
for pino, posiçao in posiçao_dos_pinos.items():
    #posiçao = posiçao_dos_pinos[pino]
    pista[posiçao] = pino
mostra_pista(pista)  

jogada = []

for pino in jogada:
    posiçao = posiçao_dos_pinos[pino]
    pista[posiçao] = ' '
    
mostra_pista(pista)

def sortear():
    pista = {38,32,30,25,23,21,17,15,13,11,8,6,4,2,0}
    
    random.shuffle(pista)
    posiçao_dos_pinos(str(pista[0]))
    posiçao_dos_pinos(str(pista[1]))
    posiçao_dos_pinos(str(pista[3]))


    

#print(random.randrange(1, 3))       
#