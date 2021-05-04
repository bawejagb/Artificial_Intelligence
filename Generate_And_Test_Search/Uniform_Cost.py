'''
Q5- Shortest path in Graph problem (Uniform Cost search algorithm)

Made By: Gaurav Baweja
'''

def FindMin(queue):
    minIdx = 0
    for i in range(len(queue)):
        if(queue[i][1] < queue[minIdx][1]):
            minIdx = i
    return minIdx

def UCS(Start, Goal, AdjLst):
    queue = []
    queue.append([[Start],0])
    while(len(queue) > 0):
        minIndex = FindMin(queue)
        cur_lst = queue[minIndex]
        del queue[minIndex]
        cur_node = cur_lst[0][-1]
        if(cur_node == Goal):
            print("Shortest Path: ",cur_lst[0])
            print("Cost: ", cur_lst[1])
            return True
        for node in AdjLst[cur_node]:
            if(node not in cur_lst[0]):
                newLst = [cur_lst[0]+[node[0]],cur_lst[1]+node[1]]
                queue.append(newLst)
    return False

if (__name__ == "__main__"):
    AdjLst = {}
    AdjLst['A'] = [['S',1],['G', 10]]
    AdjLst['B'] = [['S',5],['G', 5]]
    AdjLst['C'] = [['S',15],['G', 5]]
    AdjLst['S'] = [['A',1],['B', 5],['C', 15]]
    AdjLst['G'] = [['A',10],['B', 5],['C', 5]]
    if(not UCS('S','G',AdjLst)):
        print("Path doesn't exist!")
