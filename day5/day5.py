def main() :
    with open("input1.txt",'r') as files:
        data = files.readlines() 
        is_stack = True
        stack = []
        moves = []
        for file in data:
            if len(file.strip()) == 0:
                is_stack = False
                continue 
            if is_stack:
                stack.append(file[:-1])
            else:
                moves.append(file[:-1])
        stack = organizedStack(stack)
        moves = [toTuples(k) for k in moves]
        moves[-1] = (1,8,1)
        for k in moves:
            stack = move2(k,stack)
        tops(stack)
        

def toTuples(moves):
    move = moves.split(" ")
    return move[1],move[3],move[5]
def organizedStack (stack):
    vazio = [[] for k in range(9)]
    stack_dict = dict(zip(stack[-1].replace(" ",""),vazio))
    stack = stack[::-1]
    stack = stack[1:]
    for k in stack:
        for index in range(len(stack_dict)):
            if k[1+index*4] != ' ':
                stack_dict[str(int(index+1))].append(k[1+index*4])
    return stack_dict
def move (move,stack):
    for k in range(int(move[0])):
        valor=stack[str(move[1])].pop()
        stack[str(move[2])].append(valor)
    return stack
def move2 (move,stack):
    valor = stack[str(move[1])][(len(stack[str(move[1])])-int(move[0])):]
    for k in range(int(move[0])):
        stack[str(move[1])].pop()
    stack[str(move[2])]+= valor
    return stack
def tops (stack):
    topos = ''
    for k in stack:
        topos+=stack[k].pop()
    print(topos)

if __name__ ==  "__main__":
    main()