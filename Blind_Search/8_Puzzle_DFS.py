'''
Q1- 8 puzzle problem

Made By: Gaurav Baweja, 102097005, CSE4
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

def dequeue(que):
    if(len(que) != 0):
        del que[-1]

def front(que):
    if(len(que) > 0):
        return que[0]

def end(que):
    if(len(que) > 0):
        return que[-1]

def DFS(start, goal):
    itr_count = 0
    queue = []
    visited = []
    enqueue(queue, start)
    while(len(queue) != 0):
        itr_count += 1
        temp = end(queue)
        #Show(temp)
        dequeue(queue)
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
                print("Achieved Goal State:")
                print("Total Iteration: ", itr_count)
                Show(nextState)
                return True
            if(nextState not in queue and 
                nextState not in visited): #Enqueue 
                enqueue(queue, nextState)
    return False
 
if (__name__ == "__main__"):
    #Start
    """ StartState = [[2,0,3],
            [1,8,4],
            [7,6,5]]
    GoalState = [[1,2,3],[8,0,4],[7,6,5]] """
    StartState = [[2,0,3],
            [1,8,4],
            [7,6,5]]
    GoalState = [[1,2,3],
                [8,0,4],
                [7,6,5]]
    status = DFS(StartState, GoalState)
    print("State Possible: ",end = "")
    if(status):
        print("Yes")
    else:
        print("No")
