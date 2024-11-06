from itertools import permutations
import math

def prime(num):
    if num<=1:
        return False
    for i in range(2,int(math.sqrt(num)+1)):
        if(num%i==0):
            return False
    return True

def solution(numbers):
    answer = 0
    
    arr=[i for i in numbers]
    case=[]
    for i in range(1,len(numbers)+1):
        case+=list(permutations(arr,i))
    
    cases=[int(''.join(i)) for i in case]
    
    cases=list(set(cases))
    for i in cases:
        if prime(i)==True:
            answer+=1
            
    return answer