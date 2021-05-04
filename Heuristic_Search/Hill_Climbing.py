'''
Q2- 8 puzzle problem (Hill Climbing searching algorithm)

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

def Heuristic(current, goal):
    cost = 0
    for i in range(3):
        for j in range(3):
            if(current[i][j] != goal[i][j]):
                cost += 1
    return cost

def BFS(start, goal):
    itr_count = 0
    visited = []
    H_min = Heuristic(start, goal)
    newState = start
    while(1):
        itr_count += 1
        temp = newState
        Show(temp)
        print("Heuristic value:", H_min)
        visited.append(temp)
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
            if(nextState != temp and 
                nextState not in visited): 
                H_Value = Heuristic(nextState, goal) #Heuristic Value
                #print(H_Value, end="|")
                if(H_min >= H_Value):
                    H_min = H_Value
                    newState = nextState
        if(newState != temp):
                temp = newState
        else:
            break
                
    return False
 
if (__name__ == "__main__"):
    #Start
    StartState = [[2,8,3],
            [1,5,4],
            [7,6,0]]
    GoalState = [[1,2,3],
                [8,0,4],
                [7,6,5]]
    status = BFS(StartState, GoalState)
    print("\nState Possible: ",end = "")
    if(status):
        print("Yes")
    else:
        print("No")
