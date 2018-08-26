#Collaborators- Harsimar Singh, Subhranil Bagchi, Anurag Banerjee

#In this module we will find the weak link and then make it a strong
#link in the graph and it is similar to the increasing influence
#of a newly created website.

import networkx as nx
import matplotlib.pyplot as plt


#this method has been taken from  the leader.py file in this repository
def find_the_leader(G,threshold):
    
    
    nodes=list(G.nodes())
    edges=list(G.edges())
    length= len(nodes)

    #Maintaining Two separate Lists for the Markov_Chain

    #List containing all the 1's at the beginning which we will upadate in each itiration(basically these are the weights of the node in beggining)
    prev_val=[1.0 for i in range(0,length,1)]
    next_val=[0.0 for i in range(0,length,1)]
    flag = 0

    #Iterating through each node and then after getting all his neigbours we are flowing the current weight of that node equally to other neighbours of the node doing this unless we reach our threshold
    while(True):
        pos1 = 0
        pos2 = 0
        for i in range(0,length,1):
            node = nodes[i]
            pos1 = i
            connected = [m for m in G[node]]
            l = len(connected)
            for j in range(0,l,1):
                con = connected[j]
                for k in range(0,length,1):
                    if (con == nodes[k]):
                        pos2 = k
                        break
                next_val[pos2] = next_val[pos2] + float(prev_val[pos1]/l)
        for l in range(0,length,1):
            diff = abs(next_val[l] - prev_val[l])
            if ( diff > threshold ):
                flag = 1
                break

        #You can uncomment these lines to get the list of distribution of weight
        #print(next_val)
        #print(sum(next_val))
        if (flag == 1):
            prev_val = [next_val[x] for x in range(0,length,1)]
            next_val = [0.0 for i in range(0,length,1)]
            flag = 0
        else:
            break

    max_val = next_val[0]
    max_pos = 0

    #Finding the Position of the Max weight in the List
    for i in range(0,length,1):
        if (next_val[i] > max_val):
            max_val = next_val[i]
            max_pos = i

    #Printing the max weight and node number (position)
    #print("MAXIMUM VALUE : "+str(max_val))
    #print("LEADER NODE : "+str(nodes[max_pos]))
    return nodes[max_pos]


G=nx.read_adjlist(r"DATASET/pagerank.txt",create_using=nx.DiGraph(),nodetype=int)
lead=find_the_leader(G,.5)
C=nx.reverse(G) #cunning way to use duality
weak=find_the_leader(C,.5)
neighbour=[]
neighbour=G.neighbors(lead)
for i in neighbour:
    G.add_edge(i,weak)
print(find_the_leader(G,.5))
