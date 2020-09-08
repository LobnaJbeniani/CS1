#Lobna Jbeniani
#Lab 2 Checkpoint
#February 14th, 2020


from cs1lib import *
from body import Body
from math import sqrt

class System:

    def __init__(self, body_list):
        self.body_list=body_list






    #Python did not accept the self.body_list[element] and accepted the element.
    def update(self, timestep):
        for i in self.body_list:
            i.update_position(timestep)


        for n in range (len(self.body_list)):
            ax,ay = self.compute_acceleration(n)
            print(ax, ay)

           # n.update_position(timestep)

            self.body_list[n].update_velocity(ax,ay,timestep)







    def compute_acceleration(self,n):
        g = 6.67384e-11
        ax = 0
        ay = 0
        #totalax=0
       # totalay=0

        for p in range (len(self.body_list)):

            if p != n: #Important note: We have to make that we don't use the same planet here
                r=sqrt(((self.body_list[p].x-self.body_list[n].x)**2+(self.body_list[p].y-self.body_list[n].y)**2))
                #p.mass is equivalent to
                a = (g* self.body_list[p].mass)/(r*r)
                ax=ax+(a*((self.body_list[p].x-self.body_list[n].x)/(r)))
                ay=ay+(a*((self.body_list[p].y-self.body_list[n].y)/(r)))

        return (ax, ay)



    def draw(self, cx, cy, pixels_per_meter):
        for n in self.body_list:
            n.draw(cx,cy,pixels_per_meter)

