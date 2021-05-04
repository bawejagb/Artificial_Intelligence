'''
Q2- Water-JUG problem

Made By: Gaurav Baweja
'''
import copy as cp

def TransferTo(cap, cur, j):
    pr = cp.deepcopy(cur)
    if(j == 0):
        if(pr[0]+pr[1] > cap[0]):
            pr[1] -= (cap[0]-pr[0])
            pr[0] = cap[0]
        else:
            pr[0] += pr[1]
    elif(j == 1):
        if(pr[0]+pr[1] > cap[1]):
            pr[0] -= (cap[1]-pr[1])
            pr[1] = cap[1]
        else:
            pr[1] += pr[0]
    return pr

def Fill(cap, cur, j):
    pr = cp.deepcopy(cur)
    if(j <= 1):
        pr[j] = cap[j]
    return pr

def Empty(cur, j):
    pr = cp.deepcopy(cur)
    if(j <= 1):
        pr[j] = 0
    return pr

def enqueue(que, arr):
    que.append(arr)

def dequeue(que):
    if(len(que) != 0):
        del que[0]

def front(que):
    if(len(que) > 0):
        return que[0]

def BFS(cap, start, goal):
    queue = []
    visited = []
    enqueue(queue, start)
    while(len(queue) != 0):
        temp = front(queue)
        dequeue(queue)
        visited.append(temp)
        #print(temp)
        for state in range(1,7):
            if(state == 1): #FILL 1
                nextState = Fill(cap, temp, 0)
            if(state == 2): #FILL 2
                nextState = Fill(cap, temp, 1)
            if(state == 3): #EMPTY 1
                nextState = Empty(temp, 0)
            if(state == 4): #EMPTY 2
                nextState = Empty(temp, 1)
            if(state == 5): #Transfer to 1
                nextState = TransferTo(cap, temp, 0)
            if(state == 6): #Transfer to 2
                nextState = TransferTo(cap, temp, 1)
            if(nextState == goal): # Check Goal State
                print("Achieved Goal State:")
                print(goal)
                return True
            if(nextState != temp and 
                nextState not in visited): #Enqueue
                enqueue(queue, nextState)
    return False

if (__name__ == "__main__"):
    #Start
    J_capacity = [4, 3] #[J1, J2] Max Capacity
    StartState = [0, 0] #[J1, J2] Initial Status
    GoalState  = [2, 0] #[J1, J2] Goal Status
    status = BFS(J_capacity, StartState, GoalState)
    print("State Possible: ",end = "")
    if(status):
        print("Yes")
    else:
        print("No")

