'''
Q1- 8 puzzle problem (BEST FIRST SEARCH)

Made By: Gaurav Baweja
'''
import copy as cp

def Show(arr):
    print("------")
    for lis in arr:
        for elm in lis:
            print(elm,end="|")
        print()
    print("------")

def Position(val,arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j] == val):
                return (i,j)

def Swap(i1,j1,i2,j2,arr):
    temp = arr[i1][j1]
    arr[i1][j1] = arr[i2][j2]
    arr[i2][j2] = temp

def MoveUp(i,j,arr):
    if(i < 1):
        return arr
    temp = cp.deepcopy(arr)
    Swap(i,j,i-1,j,temp)
    return temp

def MoveLeft(i,j,arr):
    if(j < 1):
        return arr
    temp = cp.deepcopy(arr)
    Swap(i,j,i,j-1,temp)
    return temp

def MoveRight(i,j,arr):
    if(j > 1):
        return arr
    temp = cp.deepcopy(arr)
    Swap(i,j,i,j+1,temp)
    return temp

def MoveDown(i,j,arr):
    if(i > 1):
        return arr
    temp = cp.deepcopy(arr)
    Swap(i,j,i+1,j,temp)
    return temp

def Compare(arr1, arr2):
    if(arr1 == arr2):
        return True
    return False

def enqueue(que, arr):
    que.append(arr)

def dequeue(que, index):
    if(len(que) != 0):
        del que[index]

def Heuristic(current, goal):
    #To find heuristic value - COST
    cost = 0
    for i in range(3):
        for j in range(3):
            if(current[i][j] != goal[i][j]):
                cost += 1
    return cost

def FindMinCost(que):
    #To find minimum cost value index from the queue
    minIndex = 0
    for i in range(len(que)):
        if que[i][1] < que[minIndex][1]:
            minIndex = i
    return minIndex

def BFS(start, goal):
    itr_count = 0
    queue = []
    visited = []
    H_Value = Heuristic(start, goal)
    enqueue(queue, [start, H_Value])
    while(len(queue) != 0):
        itr_count += 1
        minIndex = FindMinCost(queue)
        temp = queue[minIndex][0]
        Show(temp)
        print("Heuristic value:", queue[minIndex][1])
        dequeue(queue,minIndex)
        visited.append((temp))
        row,col = Position(0,temp) # Check Position of Empty Slide(0)
        for state in range(1,5):
            if(state == 1): #MoveUp
                nextState = MoveUp(row,col,temp)
            if(state == 2): #MoveDown
                nextState = MoveDown(row,col,temp)
            if(state == 3): #MoveLeft
                nextState = MoveLeft(row,col,temp)
            if(state == 4): #MoveRight
                nextState = MoveRight(row,col,temp)
            if(nextState == goal): # Check Goal State
                Show(nextState)
                print("Heuristic value: 0\n")
                print("Achieved Goal State:")
                print("Total Iteration: ", itr_count)
                return True
            H_Value = Heuristic(nextState, goal) #Heuristic Value
            newState = [nextState, H_Value]
            if(nextState not in visited and newState not in queue): #Enqueue 
                enqueue(queue, [nextState, H_Value])
    return False
 
if (__name__ == "__main__"):
    #Start
    StartState = [[2,0,3],
            [1,8,4],
            [7,6,5]]
    GoalState = [[1,2,3],
                [8,0,4],
                [7,6,5]]
    status = BFS(StartState, GoalState)
    print("State Possible: ",end = "")
    if(status):
        print("Yes")
    else:
        print("No")
