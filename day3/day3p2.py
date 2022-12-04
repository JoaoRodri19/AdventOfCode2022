def main ():
    with open('input1.txt','r') as file:
        data = file.readlines()
    split1 = split(data)
    result =[points(k) for k in split1]
    print(soma(result))

def split (data):
    split1 = []
    i=0
    rucksack=[]
    for k in data:
        rucksack.append(k)
        i+=1
        if i == 3:  
            split1.append((rucksack[0][:-1],rucksack[1][:-1],rucksack[2][:-1]))
            rucksack.clear()
            i=0
    return split1


def points(tuple):
    first = tuple[0]
    second = tuple[1]
    third = tuple[2]
    equal=[]
    result=0
    for k in first:
        for j in second:
            for z in third:
                if (k == j==z) and k not in equal:
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