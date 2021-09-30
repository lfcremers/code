import numpy as np


def p1(k: int) -> str:
    def factorial(i):
        fact=1
        for x in range(2,(i+1)):
            fact=fact*x
        return fact
    out=""
    for i in reversed(range(1,k+1)):
        out = out + str(factorial(i)) + ","
    return out


def p2_a(x: list, y: list) -> list:
    y=sorted(y)
    del y[-1]
    return y


def p2_b(x: list, y: list) -> list:
    return list(reversed(x))


def p2_c(x: list, y: list) -> list:
    z=x+y
    z=list(set(z))
    z=sorted(z)
    return(z)


def p2_d(x: list, y: list) -> list:
    return [x,y]


def p3_a(x: set, y: set, z: set) -> set:
    union = list(x)+list(y)+list(z)
    union=set(union)
    return union


def p3_b(x: set, y: set, z: set) -> set:
    intersect = [i for i in y if i in x]
    intersect += [i for i in z if i in intersect]
    return set(intersect)


def p3_c(x: set, y: set, z: set) -> set:
    single = [i for i in y if i not in x and i not in z]
    single += [i for i in z if i not in x and i not in y]
    single += [i for i in x if i not in z and i not in y]
    return (set(single))
        
        



def p4_a() -> np.array:
    array=[[1,1,1,1,1],[1,0,0,0,1],[1,0,2,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    board=np.array(array)
    return board

def p4_b(x: np.array) -> list:
    def find_2(x):
        for z in range(0,5):
            for y in range(0,5):
                if x[z,y]==2:
                    return [z,y]
        
    coords = find_2(x)
    returns=[
       (coords[0]-2,coords[1]+1),
       (coords[0]-1,coords[1]+2),
       (coords[0]+1,coords[1]+2),
       (coords[0]+2,coords[1]+1),
       (coords[0]+2,coords[1]-1),
       (coords[0]+1,coords[1]-2),
       (coords[0]-1,coords[1]-2),
       (coords[0]-2,coords[1]-1)
   ]
    i=0
    while i < len(returns):
       
       #remove the indices that are out of scope:
       if returns[i][0] not in range(0,5) or returns[i][1] not in range(0,5):
           del returns[i]
       
       elif x[returns[i][0],returns[i][1]]!=1:
           del returns[i]
           
       else:
           i+=1
           
    return returns


def p5_a(x: dict) -> int:
    isolated=[]
    for val in x.values():
        if len(val)==0:
            isolated.append(val)
        
    return len(isolated)

def p5_b(x: dict) -> int:
    connected=[]
    for val in x.values():
        if len(val)!=0:
            connected.append(val)
    
    return len(connected)

def p5_c(x: dict) -> list:
    used=[]
    uniques=[]
    for key in x.keys():
        for val in x[key]:
            if {val,key} not in used:
                uniques.append((str(key),str(val)))
                used.append({val,key})
    return uniques

def p5_d(x: dict) -> np.array:
            
    index={}
    for y,i in zip(x.keys(),range(len(x))):
        index[y] = i 
    matrix=np.zeros((len(x),len(x)),dtype=int)

    for key in x:
        for item in x[key]:
            matrix[index[key],index[item]]=1
    

    return matrix

class PriorityQueue(object):
    def __init__(self):
        self.queue=[]
        self.ref={"apple":5,"banana":4.5,"carrot":3.3,"kiwi":7.4,"orange":5,"mango":9.1,"pineapple":9.1}

    def push(self, x):
        if self.is_empty():
            self.queue.append(x)
        else:
            position =0
            while position<len(self.queue):
                #if the item to add is larger than the current element being inspected, insert it in front of the current element
                if self.ref[self.queue[position]]<self.ref[x]:
                    self.queue.insert(position,x)
                   
                    return
                
                #if the item to add is smaller than (or equal to) the curent element being inspected, go to the next item:
                elif self.ref[self.queue[position]]>=self.ref[x]:
                    position+=1
                    continue
                
            self.queue.append(x)

    def pop(self):
        item=self.queue[0]
        del self.queue[0]
        return item

    def is_empty(self):
        if len(self.queue)==0:
            return True
        return False


if __name__ == '__main__':
    print(p1(k=8))
    print('-----------------------------')
    print(p2_a(x=[], y=[1, 3, 5]))
    print(p2_b(x=[2, 4, 6], y=[]))
    print(p2_c(x=[1, 3, 5, 7], y=[1, 2, 5, 6]))
    print(p2_d(x=[1, 3, 5, 7], y=[1, 2, 5, 6]))
    print('------------------------------')
    print(p3_a(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print(p3_b(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print(p3_c(x={1, 3, 5, 7}, y={1, 2, 5, 6}, z={7, 8, 9, 1}))
    print('------------------------------')
    print(p4_a())
    print(p4_b(p4_a()))
    print('------------------------------')
    graph = {
        'A': ['D', 'E'],
        'B': ['E', 'F'],
        'C': ['E'],
        'D': ['A', 'E'],
        'E': ['A', 'B', 'C', 'D'],
        'F': ['B'],
        'G': []
    }
    print(p5_a(graph))
    print(p5_b(graph))
    print(p5_c(graph))
    print(p5_d(graph))
    print('------------------------------')
    pq = PriorityQueue()
    pq.push('apple')
    pq.push('kiwi')
    pq.push('orange')
    while not pq.is_empty():
        print(pq.pop())
