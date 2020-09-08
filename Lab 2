#Lobna Jbeniani
#Lab2 Checkpoint
#Solar System, February 13, 2019


from cs1lib import*

class Body :
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b)

        #Setting up the mass
        self.mass=mass #in kg

        #Setting up the coordinates
        self.x=x
        self.y=y

        #Setting up the velocities
        self.vx=vx
        self.vy=vy
        self.pixel_radius=pixel_radius

        #Setting up the color variables
        self.r=r #determines the amount of Red in the color
        self.g=g #determines the amount of Green in the color
        self.b=b #determines the amount of Blue in the color

    def update_position(self, timestep)
        #This determines the change in position over time or velocity, V=d(D)
        self.x= self.x + self.vx * timestep
        self.y= self.y + self.vy * timestep


    def update_velocity(self, ax, ay, timestep)
        #This determines the change in velocity over time or acceleration , a=d(V)
        self.ax = self.vx+ ax *timestep
        self.ay = self.vy+ ay *timestep



    def draw(self, cx, cy, pixels_per_meter)
        clear()
        set_fill_color(self.r, self.g, self.b)
        #pixels per meter:
        cx = WINDOW_Y / 2
        cy = WINDOW_X / 2

        self.cx= cx
        self.cy= cy


    draw_circle(self.x*pixels_per_meter+self.cx,self.y*pixels_per_meter+self.cy,self.pixel_radius)

