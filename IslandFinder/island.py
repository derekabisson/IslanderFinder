
class Island:
    def __init__(self, y, x,):
        self.coord = [[y, x]]
        self.is_closed = True
        self.base_coord = []
        self.size = 0
        
    def set_base_coorinates(self):
        y_base = self.coord[0][0]
        x_base = self.coord[0][1]
        for y, x in self.coord:
            self.base_coord.append([(y-y_base),(x-x_base)])
        #print(f"base coord: ")
        #self.print_2d(self.base_coord)
        self.size = len(self.base_coord)
        
            
        
    def print_2d(self, d_array):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in d_array]))