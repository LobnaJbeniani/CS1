#Lobna Jbeniani
#CS1
#March 2020

from cs1lib import *

#defining the vertex class
class Vertex:
    def __init__(self, vertex, adj_list, options):
        self.vertex = vertex
        self.adj_list = adj_list
        self.options=options

    #This method allows to get the options from the vertex class

    def choices(self):
        return self.options

    #This method allows to get the adjacent list from the vertex class
    def get_adj_list(self):
        return self.adj_list
