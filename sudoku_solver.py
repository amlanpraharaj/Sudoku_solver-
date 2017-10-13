
# coding: utf-8

# In[44]:

import numpy as np


# In[45]:

class Sudoku_solver:
    def __init__(self):
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.location = [0,0]
    
    def get_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.location = [i,j]
                    return True
        return False
    
    def solve(self):
        if not self.get_empty():
            return True
        
        row = self.location[0]
        col = self.location[1]
        
        for num in range(1,10):
            if(self.valid_check(row, col,num)):
                self.grid[row][col] = num
                
                if(self.solve()):
                    return True
                
                self.grid[row][col] = 0
        return False
                   
    def used_in_row(self,row,num):
        for i in range(9):
            if(self.grid[row][i] == num):
                return True
        return False

    # in the specified column matches the given number.
    def used_in_col(self,col,num):
        for i in range(9):
            if(self.grid[i][col] == num):
                return True
        return False

    # within the specified 3x3 box matches the given number
    def used_in_box(self,row,col,num):
        for i in range(3):
            for j in range(3):
                if(self.grid[i+row][j+col] == num):
                    return True
        return False

    def valid_check(self,row,col,num):
        return not self.used_in_row(row,num) and not self.used_in_col(col,num) and not self.used_in_box(row - row%3,col - col%3,num)


# In[46]:

#initialize the instance
board = Sudoku_solver()


# In[47]:

#to solve
board.grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]


# In[48]:

board.solve()


# In[49]:

#solution
board.grid


# In[ ]:



