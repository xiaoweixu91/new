# http://www.codeskulptor.org/#user40_AWturr5OFG_44.py
"""
    Clone of 2048 game.
    """

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
    DOWN: (-1, 0),
        LEFT: (0, 1),
            RIGHT: (0, -1)}

def merge(line):
    """
        Function that merges a single row or column in 2048.
        """
    # replace with your code
    # put the non-zero first and zero second,eg.2204 ->2240
    len_line = len(line)
    non_zero = []
    zero = []
    for idx in range(len_line):
        if line[idx] != 0:
            non_zero.append(line[idx])
        else:
            zero.append(line[idx])
    non_zero.extend(zero)
    #print 'inter'+str(non_zero)
    try_to_merge = []
    zero = []
    merge_flag=1
    #merging part
    for index in range(len_line-1):
        if merge_flag :
            if non_zero[index] == non_zero[index+1]:
                non_zero[index]*=2
                non_zero[index+1]=-1
                try_to_merge.append(non_zero[index])
                zero.append(0)
                merge_flag=0
            else:
                try_to_merge.append(non_zero[index])
        elif merge_flag == 0:
            merge_flag = 1
    if non_zero[-1]>=0:
        try_to_merge.append(non_zero[-1])
    try_to_merge.extend(zero)
    
#print zero

            return try_to_merge


class TwentyFortyEight:
    """
        Class to run the game logic.
        """
    
    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._height = grid_height
        self._width = grid_width
        self.reset()
        dir_up=[]
        dir_down=[]
        dir_left=[]
        dir_right=[]
        for index in range(self._width):
            dir_up.append((0,index))
            dir_down.append((self._height-1,index))
        for index in range(self._height):
            dir_left.append((index,0))
            dir_right.append((index,self._width-1))
        self._dir= {UP:dir_up,
            DOWN:dir_down,
                LEFT:dir_left,
                    RIGHT:dir_right}


def reset(self):
    """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
            # replace with your code
            self._grid = [[ 0 for dummy_col in range(self._width)]
                          for dummy_row in range(self._height)]
                self.new_tile()
                    self.new_tile()

#for row in range(self._height):
#   print self._grid[row]

def __str__(self):
    """
        Return a string representation of the grid for debugging.
        """
            # replace with your code
            return str(self._grid)
        
        def get_grid_height(self):
        """
            Get the height of the board.
            """
        # replace with your code
                return self._height

def get_grid_width(self):
    """
        Get the width of the board.
        """
            # replace with your code
            
            return self._width
        
        def move(self, direction):
        """
            Move all tiles in the given direction and add
            a new tile if any tiles moved.
            """
        empty=0
        if direction == UP or direction == DOWN:
            num_step=self._height
            init_num=self._width
            else:
            num_step=self._width
                init_num=self._height
for index in range(init_num):
    list_temp=[]
        for step in range(num_step):
            
            index_x=self._dir[direction][index][0]+step*OFFSETS[direction][0]
                index_y=self._dir[direction][index][1]+step*OFFSETS[direction][1]
                
                list_temp.append(self._grid[index_x][index_y])
            list_temp_new=merge(list_temp)
            if list_temp_new != list_temp:
                empty+=1
        if direction == UP :
            for stepidx in range(num_step):
                self._grid[stepidx][index]=list_temp_new[stepidx]
            elif direction == DOWN:
                list_temp_new.reverse()
                for stepidx in range(num_step):
                    self._grid[stepidx][index]=list_temp_new[stepidx]
        elif direction == LEFT:
            for stepidx in range(num_step):
                self._grid[index][stepidx]=list_temp_new[stepidx]
            elif direction == RIGHT:
                list_temp_new.reverse()
                for stepidx in range(num_step):
                    self._grid[index][stepidx]=list_temp_new[stepidx]
if empty != 0:
    self.new_tile()
    
    
    def new_tile(self):
        """
            Create a new tile in a randomly selected empty
            square.  The tile should be 2 90% of the time and
            4 10% of the time.
            """
        # replace with your codefor row in range(2):
        newlist=[]
        choice_list = [2,2,2,2,2,2,2,2,2,4]
        for row in range(self._height):
            newlist.extend(self._grid[row])
        if min(newlist)>0:
            print "You lose"
        else:
            index_x=random.randrange(0,self._height)
            index_y=random.randrange(0,self._width)
            
            while(self._grid[index_x][index_y] !=0):
                index_x=random.randrange(0,self._height)
                index_y=random.randrange(0,self._width)
            self._grid[index_x][index_y]=random.choice(choice_list)

def set_tile(self, row, col, value):
    """
        Set the tile at position row, col to have the given value.
        """
            
            self._grid[row][col]=value
        
        def get_tile(self, row, col):
        """
            Return the value of the tile at position row, col.
            """
        return self._grid[row][col]









poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


