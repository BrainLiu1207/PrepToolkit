from typing import Iterable, Any

def split(iterable: Iterable[Any], n:int):
    l = len(iterable)
    b = l // n
    
    if b == 0:
        return [[x] for x in iterable]

    else:
        a = l % n
        
        result = [None] * a
        loc = 0
        for i in range(a):
            result[i] = iterable[loc: loc + b + 1]
            loc += b + 1
        for j in range(n-a):
            result += [iterable[loc: loc + b]]
            loc += b
        return result
        

if __name__ =="__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11]
    res = split(test_list, 20)
    print(res)