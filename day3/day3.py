def main ():
    with open('input1.txt','r') as file:
        data = file.readlines()
    split = [(k[:len(k)//2],k[(len(k)//2):-1]) for k in data ] 
    result = 0
    result =[points(k) for k in split]
    print(len(result))
    print(soma(result))
def points(tuple):
    first = tuple[0]
    second = tuple[1]
    equal=[]
    result=0
    for k in first:
        for j in second:
            if k == j and k not in equal:
                equal.append(k)
                
    for k in equal:
        result+=letterToPrio(k)
    return result
    
def soma (array):
    soma1=0
    for k in array:
        soma1+=k
    return soma1

def letterToPrio(char):
    upper = char.isupper()
    if upper:
        return ord(char)-38
    else:
        return ord(char)-96

if __name__ == "__main__":
    main()