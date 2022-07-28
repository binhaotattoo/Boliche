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
print('Esta é a pista pronta para sua jogada ')
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
print( 'Esta é a sequência numérica dos pinos')
for pino, posiçao in posiçao_dos_pinos.items():
    posiçao = posiçao_dos_pinos[pino]
    pista[posiçao] = pino

mostra_pista(pista)  

jogada = ['3','5','9','11']

for pino in jogada:
    posiçao = posiçao_dos_pinos[pino]
    pista[posiçao] = ' '
mostra_pista(pista)  
print('Não foi desta vez, você só derrubou 4 pinos')
print()
    
