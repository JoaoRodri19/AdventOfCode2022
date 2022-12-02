def main():
    with open("input1.txt","r") as file:
        data= file.readlines()
    #print(data[1][:-1].split(" ")[1])
    jogadas = [k[:-1].split(" ") for k in data]
    jogadasPontos = [pontos(k) for k in jogadas]
    jogadasPontos1 = [pontos2(k) for k in jogadas]
    print(soma(jogadasPontos))#ex1
    print(soma(jogadasPontos1))#ex2
def soma (array):
    soma1=0
    for k in array:
        soma1+=k
    return soma1
def pontos(array):
    pontos =0
    player1 = array[0]
    player2 = array[1]
    if player1 == 'A' and player2 =="X" or player1 == 'B' and player2 =="Y" or player1 == 'C' and player2 =="Z":
        pontos+=3
    if player1 == 'A' and player2 =='Y':
        pontos+=6
    if player1 == 'B' and player2 =='Z':
        pontos+=6
    if player1 == 'C' and player2 =='X':
        pontos+=6
    if player2 == 'X':
        pontos+=1
    if player2 == 'Y':
        pontos+=2
    if player2 == 'Z':
        pontos+=3
    return pontos

def pontos2(array):
    pontos =0
    player1 = array[0]
    choice = array[1]
    if player1 == 'A' and choice == 'X':
        pontos+= 3
    if player1 == 'A' and choice == 'Y':
        pontos+= 1
    if player1 == 'A' and choice == 'Z':
        pontos+= 2
    
    if player1 == 'B' and choice == 'X':
        pontos+= 1
    if player1 == 'B' and choice == 'Y':
        pontos+= 2
    if player1 == 'B' and choice == 'Z':
        pontos+= 3
    
    if player1 == 'C' and choice == 'X':
        pontos+= 2
    if player1 == 'C' and choice == 'Y':
        pontos+= 3
    if player1 == 'C' and choice == 'Z':
        pontos+= 1
    
    if choice == 'X':
        pontos+=0
    if choice == 'Y':
        pontos+=3
    if choice == 'Z':
        pontos+=6
    return pontos
        

if __name__ == "__main__" :
    main()