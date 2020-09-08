#Lobna Jbeniani
#CS1, Dartmouth College
#March 2020


from vertex import Vertex
from cs1lib import*

#Parsing the lines in the file

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


#Loading the story into the dictionary

def load_story(filename):
    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open("mystory.txt", "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

           # print("vertex " + vertex_name)
           # print(" adjacent:  " + str(adjacent_vertices))
            #print(" text:  " + text)

        # YOU WRITE THIS PART
        # create a graph vertex here and add it to the dictionary
        v=Vertex(vertex_name, adjacent_vertices, text)
        vertex_dict[vertex_name]=v
        #in here, you can also write Vertex(vertex_dict[vertex_name]=Vertex(vertex_name, adjacent_vertices, text)

        #Closing the file
    file.close()

    return vertex_dict

#Defining the play function
def playfunc(story_dict):
    next_vertex = "START"
    print("Please enter a letter:")
#setting i=0 for it to be able to loop through the entire story dictionary
    i=0

#Ensuring that i does not pass the length of the story dictionary
    while i<= len(story_dict):
#This line of code accesses
        the_choice=input(story_dict[next_vertex].choices())

#Something to note is that the ord("a") = 97 so instead of having ord(choice)-ord("a") you can
#also write ord(choice)-97 but the first is more explanatory

        index=ord(the_choice)-ord("a")
        next_vertex=story_dict[next_vertex].get_adj_list()[index]
        i=i+1


#Calling the functions
story_dict = load_story("mystory.txt")
playfunc(story_dict)