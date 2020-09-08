#Lobna Jbeniani
#CS1, LAB4

#Importing from the Vertex class
from myvertex import Vertex


#This function allows us to load the graph and takes the name as a parameter
def load_graph(name):
    vertex_dict={}
    file=open("dartmouth_graph.txt", "r")
    adjacency_list=[]
    for l in file:
        l=l.strip()
        list1=l.split("; ")

        if len(list1) == 3:
            vertex_name=list1[0].strip()
            # adjacent_vertices=list1[1]
            coordinates=list1[2].split(", ")

#You don't need another for loop here since we
#don't need to loop through the two coordinates
            if len(coordinates)==2:
                x=int(coordinates[0].strip())
                y=int(coordinates[1].strip())

            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)
                #vertex_name=l.strip()
            # YOU WRITE THIS PART
            # create a graph vertex here and add it to the dictionary

        #Passing the Vertex into v and into the vertex dictionary
            v = Vertex(vertex_name, x, y)
            vertex_dict[vertex_name]=(v)


        # in here, you can also write Vertex(vertex_dict[vertex_name]=Vertex(vertex_name, adjacent_vertices, text)
        #close
        #open
    file.close()
    file=open("dartmouth_graph.txt","r")
    adjacency_list=[]
    for j in file:
        list1 = j.split(";")
        if len(list1) == 3:
            vertex_name = list1[0].strip()
            adjacency_list = list1[1].strip()
            neighbors=adjacency_list.split(", ")
            for i in neighbors:
                vertex_dict[vertex_name].adjacency_list.append(vertex_dict[i])
    file.close()

        # Closing the file1
    return vertex_dict




