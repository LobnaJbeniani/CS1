#myvertex file
#Lobna Jbeniani
#CS1, LAB4
from cs1lib import *
from math import *

#Defining the vertex class
class Vertex:

    def __init__(self, name, x, y):
        self.name=name
        self.x=x
        self.y=y
        self.adjacency_list=[]
        self.next=None

#This method allows us to append to the list of neighbors
    def append_adjacent_list(self, appendlist):
        self.adjacency_list.append(appendlist)

#defining the string method
    def __str__(self):
        newstring=""
        for i in self.adjacency_list:
            newstring= newstring + "," + i.name
#we're returning what we would like to see showcased in the file
        return (str(self.name)+ "; "+"Location: "+str(self.x)+", "+str(self.y)+"; Adjacent vertices: "+newstring)

    def draw_vertex(self, r=0, g=0, b=1):
        #for i in self.adjacency_list:
        disable_stroke()
        set_fill_color(r,g,b)
        draw_circle(self.x, self.y,7)
        enable_stroke()

    def draw_all_edges(self, othervertex, r=0, g=0, b=1):
        for any in range (0,len(self.adjacency_list)):
            set_fill_color(r,g,b)
            set_stroke_color(0,0,1)
            set_stroke_width(2)
            draw_line(self.x,self.y,self.adjacency_list[any].x, self.adjacency_list[any].y)

    def draw_adj_edges(self,r=0,g=0,b=1):
        for i in range(0, len(self.adjacency_list)-1):
            set_fill_color(r,g,b)
            #set_stroke_color(r,g,b)
            set_stroke_width(2)
            draw_line(self.adjacency_list[i].x, self.adjacency_list[i].y, self.adjacency_list[i+1].x, self.adjacency_list[i+1].y)
    def draw_edge(self, other):
        set_fill_color(1,1,1)
        set_stroke_color(1,0,0)
        draw_line(self.x,self.y,other.x,other.y)

      #  if is_mouse_pressed():
        #    self.r=1
    def smallest_square(self, x, y):
        if ((self.x-x<=7) and (x-self.x<=7) and ((self.y-y<=7) and (y-self.y)<=7)):
            return True
        else:
            return False








    #def (self, x, y):
        #return <=x<= and <=y<=