import math

class Calcmap:

    def __init__(self,x,y,cell_width,cell_height):
        self.grid = range(int(y/cell_height))
        self.width = x
        self.height = y
        self.cell_width = cell_width
        self.cell_height = cell_height
        for z in range(len(self.grid)):
            self.grid[z] = range(int(math.floor(x/cell_width)))

            for a in range(len(self.grid[z])):
                self.grid[z][a]=1

    def consume (self,x,y,appetite=0.05):
        try:
          self.grid[int(math.floor(y/self.cell_height))][int(math.floor(x/self.cell_width))] -= appetite
          if self.grid[int(math.floor(y/self.cell_height))][int(math.floor(x/self.cell_width))] < 0:
              self.grid[int(math.floor(y/self.cell_height))][int(math.floor(x/self.cell_width))] = 0
        except:
          pass

    #def pollute (self,x,y,toxin_type,toxin_strength):
    #    try:
    #      for a  in range(-1,2):
    #        for b in range(-1,2):
    #          self.grid[int(math.floor(y/self.cell_height))+a][int(math.floor(x/self.cell_width))+b][toxin_type+1] += toxin_strength
    #      if self.grid[int(math.floor(y/self.cell_height))][int(math.floor(x/self.cell_width))][toxin_type+1] < 0:
    #          self.grid[int(math.floor(y/self.cell_height))][int(math.floor(x/self.cell_width))][toxin_type+1] = 0
    #    except:
    #      pass



    def select (self,x,y):
        try:
          return self.grid[int(math.floor(y/self.cell_height))][int(math.floor(x/self.cell_width))]
        except IndexError:
          return 0

    def regrow(self,speed=0.1):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.grid[y][x] += speed

                if (self.grid[y][x] > 1):
                    self.grid[y][x] = 1
