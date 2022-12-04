def main ():
    with open('input1.txt','r') as file:
        data = file.readlines()
    ranges = [((k.split(",")[0].split("-")[0],k.split(",")[0].split("-")[1]),(k.split(",")[1].split("-")[0],k.split(",")[1].split("-")[1][:-1])) for k in data]

    res = [subconjunto(k) for k in ranges]
    res1 = [overlap(k) for k in ranges]
    print(soma(res1))
    print(soma(res))
def overlap(tuple):
    int1 = int(tuple[0][0]),int(tuple[0][1])
    int2 = int(tuple[1][0]),int(tuple[1][1])
    val1 = arrayIncre(int1)
    val2 = arrayIncre(int2)
    if len(val1)< len(val2):
       for k in val1:
            if k in val2:
                return 1
    elif len(val2)<= len(val1):
        for k in val2:
            if k in val1:
                return 1
    return 0
    

def subconjunto(tuple):
    int1 = int(tuple[0][0]),int(tuple[0][1])
    int2 = int(tuple[1][0]),int(tuple[1][1])
    val1 = arrayIncre(int1)
    val2 = arrayIncre(int2)
    flag = True
    if len(val1)< len(val2):
       for k in val1:
            if k not in val2:
                flag=False
                break
    elif len(val2)<= len(val1):
        for k in val2:
            if k not in val1:
                flag=False
                break
    if flag:
        return 1
    else:
        return 0
    

def soma (array):
    soma1=0
    for k in array:
        soma1+=k
    return soma1


def arrayIncre(tuple):
    init = tuple[0]
    array = []
    for k in range(tuple[1]-tuple[0]):
        array.append(k+init)
    array.append(tuple[1])
    return array


if __name__ == "__main__":
    main()