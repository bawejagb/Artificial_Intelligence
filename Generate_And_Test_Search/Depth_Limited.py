'''
Q3- Block Word problem (Depth Limited Search algorithm)

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


def DFS(start, goal, depth):
    count = 0
    stack = [[start,0]]
    visited = []
    while(len(stack) > 0):
        count += 1
        cur_state = stack.pop()
        visited.append(cur_state[0])
        print(cur_state)
        if(Compare(cur_state[0], [goal])):
            print("Achieved Goal State!")
            print("Iteration Count: ", count)
            return True
        if(cur_state[1] < depth):
            newStates = GenerateState(cur_state[0])
            for state in newStates:
                if(not Compare(state, visited)):
                    stack.append([state, cur_state[1]+1])
    return False
    
 
if (__name__ == "__main__"):
    #Start
    StartState = [['A'], ['B','C'], []]
    GoalState = [['A','B','C'], [], []]
    depth = 1
    status = DFS(StartState, GoalState, depth)
    print("State Possible: ",end = "")
    if(status):
        print("Yes")
    else:
        print("No")
