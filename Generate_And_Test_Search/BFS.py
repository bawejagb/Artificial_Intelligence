'''
Q2- Block Word problem (BFS algorithm)

Made By: Gaurav Baweja
'''
import copy as cp

def GenerateState(state):
    psState = []
    for i in range(len(state)):
        pr = state[i]
        if(len(pr)):
            elm = pr[-1]
            for j in range(len(state)):
                temp = cp.deepcopy(state)
                temp[i].pop()
                temp[j].append(elm)
                if(temp != state and temp not in psState):
                    psState.append(temp)
    return psState


def Compare(state, lst):
    for cmp in lst:
        count = 0
        for x in cmp:
            if(x in state):
                count += 1
        
        if(count == len(state)):
            #print(count)
            return True
    return False


def DFS(start, goal):
    count = 0
    queue = [start]
    visited = []
    while(len(queue) > 0):
        count += 1
        cur_state = queue[0]
        del queue[0]
        visited.append(cur_state)
        print(cur_state)
        if(Compare(cur_state, [goal])):
            print("Achieved Goal State!")
            print("Iteration Count: ", count)
            return True
        newStates = GenerateState(cur_state)
        for state in newStates:
            if(not Compare(state, visited) and not Compare(state, queue)):
                queue.append(state)
    return False
    
 
if (__name__ == "__main__"):
    #Start
    StartState = [['A'], ['B','C'], []]
    GoalState = [['A','B','C'], [], []]
    status = DFS(StartState, GoalState)
    print("State Possible: ",end = "")
    if(status):
        print("Yes")
    else:
        print("No")
