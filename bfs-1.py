#Lobna Jbeniani
#CS1 LAB4
#2020


#Importing deque
from collections import deque

#Defining the BFS function
def breadthfirstsearch(start,goal):
    print('bfs called on', start.name, goal.name)
    queue=deque()
    empty_d={}
    queue.append(start)
    empty_d[start]=None
    #we need to make sure that while the queue is not empty, we pop from the queue
    while len(queue) !=0:
        x=queue.popleft()
        if x==goal:
            break

#when the vertex is in the adjacency list, if the vertex
# is not in the vertex dictionary, we want to append it to the queue
        for vertex in x.adjacency_list:
            if vertex not in empty_d:
                empty_d[vertex]=x
                queue.append(vertex)

#We now create an empty path list, I called it destination
    destination=[]
    while empty_d[x]!=None:
        print('building path')
#we append the value of the key in the dictionary to the destination list
        destination.append(x)
        x=empty_d[x]

    destination.append(x)
#returning the destination or path
    return destination


