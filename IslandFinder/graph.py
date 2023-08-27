from island import Island

class Graph:
    
    def __init__(self, coordinates):
        self.coord = coordinates
        self.max_x = len(coordinates[0])
        self.max_y = len(coordinates)
        self.coord_checker = [[0 for i in range(self.max_x)] for j in range(self.max_y)]
        self.islands = []
        
        
    
    def find_islands(self):
        #print(self.coord)
        
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.coord_checker[y][x] == 0:
                    if self.coord[y][x] == 1:
                        #print(f"You found an island at {y},{x}")
                        self.coord_checker[y][x] = 1
                        self.island_tmp = Island(y, x)
                        if self.is_on_border(y, x):
                            self.island_tmp.is_closed = False
                        self.check_perimeter(y, x)
                        self.islands.append(self.island_tmp)
                        #print(f"Island {self.island_tmp.coord}")
                    else:
                        #print(f"No island located {y},{x}")
                        self.coord_checker[y][x] = 1
                #else:
                    #print(f"We have already check coordinate {y} {x}")
            #print(f"{self.coord_checker}")
        self.islands_found()

    def check_perimeter(self, y, x, coming_from="origin"):
        if coming_from == "origin":
            self.get_north(y, x)
            self.get_east(y, x)
            self.get_south(y, x)
            self.get_west(y, x)
        elif coming_from == "west":
            self.get_north(y, x)
            self.get_east(y, x)
            self.get_south(y, x)
        elif coming_from == "north":
            self.get_east(y, x)
            self.get_west(y, x)
            self.get_south(y, x)
        elif coming_from == "east":
            self.get_north(y, x)
            self.get_south(y, x)
            self.get_west(y, x)
        elif coming_from == "south":
            self.get_north(y, x)
            self.get_east(y, x)
            self.get_west(y, x)
        
    def get_north(self, y, x):
        if y == 0:
            #print("You are at the border")
            return
        y = y - 1
        if self.coord[y][x] == 1 and self.coord_checker[y][x] == 0:
            #print("The island continues to the north")
            self.coord_checker[y][x] = 1
            if self.is_on_border(y, x):
                self.island_tmp.is_closed = False            
            self.island_tmp.coord.append([y, x])
            self.check_perimeter(y, x, "south")
 #       else:
            #print("There is water north")

    def get_south(self, y, x):
        if y == (self.max_y - 1):
            #print(f"You are at the southern border {y} < {self.max_y}")
            return
        y = y + 1        
        if self.coord[y][x] == 1 and self.coord_checker[y][x] == 0:
            self.coord_checker[y][x] = 1
            #print(f"The island continues to the South {y} to {self.max_y} {x} to {self.max_x}")
            if self.is_on_border(y, x):
                self.island_tmp.is_closed = False            
            self.island_tmp.coord.append([y, x])
            self.check_perimeter(y, x, "north")

#        else:
            #print("There is water South")   
        
    def get_east(self, y, x):
        #print(f" {x} vs {self.max_x}")
        if x == (self.max_x - 1):
            #print("Your are at the eastern border")
            return    
        x = x + 1      
        if self.coord[y][x] == 1 and self.coord_checker[y][x] == 0:
            #print("The island continues east")
            self.coord_checker[y][x] = 1
            if self.is_on_border(y, x):
                self.island_tmp.is_closed = False
            self.island_tmp.coord.append([y, x])
            self.check_perimeter(y, x, "west")

#        else:
            #print("There is water to the east")
        
    def get_west(self, y, x):
        if x == 0:
            #print("Your are at the western border")
            return    
        x = x - 1        
        if self.coord[y][x] == 1 and self.coord_checker[y][x] == 0:
            #print("The island continues west")
            self.coord_checker[y][x] = 1
            if self.is_on_border(y, x):
                self.island_tmp.is_closed = False
            self.island_tmp.coord.append([y, x])            
            self.check_perimeter(y, x, "east")

        #else:
            #print("There is water to the west")

    def is_on_border(self, y, x):
        if x == 0 or x == self.max_x - 1 or y == 0 or y == self.max_y - 1:
            return True
    def islands_found(self):
        closed_counter = 0
        
        for island in self.islands:
            #print(island)
            print(f"Island coordinates: {island.coord} and is closed {island.is_closed}")
            if island.is_closed:
                closed_counter += 1
        print(f"Islands found {len(self.islands)}") 
        print(f"Islands closed {closed_counter}\n\n\n ")
               
            