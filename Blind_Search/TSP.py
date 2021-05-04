'''
Q3- Travelling Salesman Problem

Made By: Gaurav Baweja
'''

def DFS(AdjMat, start, node, visited=[]):
    visited.append(node)
    cost = []
    if(len(visited) == len(AdjMat)):
        return AdjMat[node][start]
    for p in range(len(AdjMat)):
        if(p not in visited):
            cost.append( AdjMat[node][p] + DFS(AdjMat,start, p, visited.copy()))
    min_cost = cost[0]
    for x in cost:
        if(x < min_cost):
            min_cost = x
    return min_cost

if (__name__ == "__main__"):
    #Start
    AdjMat = [[0,10,15,20],
              [10,0,35,25],
              [15,35,0,30],
              [20,25,30,0]]
    start = int(input("Enter starting node: "))
    if start > 0 and start <= len(AdjMat):
        print(DFS(AdjMat,start-1, start-1))
    else:
        print("Wrong Input!")

