import random

############## Functions
def stickman(n):
    draw = open("./stickman_model.mdl", "r", encoding='utf-8')

    for i, line in enumerate(draw):
        print(line[0:-1])

        if n == i:
            break

#Quita acentos y mayusculas
def normalize(str):
    str = str[0:-1].casefold()   #Por default devuelve el string con una letra menos.
    str = str.replace('á','a')
    str = str.replace('é','e')
    str = str.replace('í','i')
    str = str.replace('ó','o')
    str = str.replace('ú','u')
    return str

def tilde(str):
    if str == 'a':
        return 'á'
    elif str == 'e':
        return 'é'
    elif str == 'i':
        return 'í'
    elif str == 'o':
        return 'ó'
    elif str == 'u':
        return 'ú' 

################## Variables
words = open("./words.txt", "r")
lines_Q = len(words.readlines())
index = random.randint(0, lines_Q)

fails = 0
unhide = ''
lista = []

#################### File manipulation
for i, line in enumerate(open("./words.txt", "r", encoding='utf-8')):
    if i == index:
        print(line)
        print(normalize(line.casefold()))
        words.close()
        break

for i in range(0,len(line)-1):
    lista.append('__ ')

print(lista)

################## Start game
while fails != 5:

    #################### Draw Game
    if fails == 0:
        stickman(None)
    elif fails == 1:
        stickman(9)
    elif fails == 2:
        stickman(8)
    elif fails == 3:
        stickman(7)
    elif fails == 4:
        stickman(6)

    #''''''''''''''''''''''''''''''''''''''

    for i in range(0,len(line)-1):
        if unhide == normalize(line[i]+'e'):    #la +'e' Es de relleno para la funcion nomalize()
            lista[i] = unhide

    for i in range(0, len(lista)):
        print(lista[i], end="")
    print("\n")

    print("Fails =",fails, "/5\n")

    ##################### Main game logic

    pol = input("Inserta una letra o palabra completa>> ")

    if len(pol) != 1:
        #Mas de una letra
        if pol == normalize(line):
            print("\nLa palabra es correcta\nFelicidades, GANASTE!!\n")
            break
        else:
            fails = fails + 1
    else:
        #Una letra
        if normalize(line).count(pol) >= 1:
            unhide = pol
        else:
            fails = fails + 1

        confirmation = 0
        for i in range(0,len(lista)):
            if lista[i] != '__ ':
                confirmation = confirmation + 1
        
        if confirmation == len(lista)-1:
            print(f"\nLa palabra {line.upper()}es correcta\nFelicidades, GANASTE!!\n")
            break
    
    if fails == 5:
        print("\nFails =",fails, "/5")
        print('Has gastado las oportunidades\nSuerte en la próxima\n')
        break
