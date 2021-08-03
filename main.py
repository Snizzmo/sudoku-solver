import numpy as np
import time, random
from tqdm import tqdm 

def main():
    '''
    from '1 million sudoku boards' on Kaggle
    link: https://www.kaggle.com/bryanpark/sudoku
    '''
    quizzes = np.zeros((1000000, 81), np.int32)
    solutions = np.zeros((1000000, 81), np.int32)
    for i, line in enumerate(tqdm(open('sudoku.csv', 'r').read().splitlines()[1:],desc='Loading 1,000,000 sudoku boards and solutions')):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    quizzes = quizzes.reshape((-1, 9, 9))
    solutions = solutions.reshape((-1, 9, 9))

    #pick a random board from the 1,000,000 options
    n = random.randint(0,1000000-1)
    board=quizzes[n]
    solution=solutions[n]
    
    print(board)
    print('board n =',n)
    t1 = time.time()
    solve(board)
    t2=time.time()
    print(board)
    print("solution took {:.3f} seconds".format(t2-t1))

# Recursive solution
def solve(board):
    '''
    Solve sudoku with backtracking.
    board: list of list of ints, forming 9x9 board
    returns solution board
    '''
    #print("solving\n{}".format(board))
    pos=False # (0,0) to (8,8); keeps track of position in form of (row, col) starting with 0,0 upper left
    
    pos = find_empty(board)
    
    if not pos:
        return(True)

    for i in range(1, 10): 
        if valid(board, pos, i):
            board[pos] = i

            if solve(board): 
                return(True)

            board[pos] = 0

    return(False) 

def find_empty(board):
    '''
    finds the next empty position 
    ''' 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i,j] == 0: 
                return (i,j)
    return(None)

def valid(board, pos, num):
    '''
    returns if the attempted move is valid
    ''' 
    for i in range(0, len(board)): 
        if board[pos[0],[i]] == num: 
            return(False)
    # check col
    for j in range(0, len(board)): 
        if board[[j],pos[1]] == num:
            return(False)

    # check box
    box = (pos[1]//3, pos[0]//3) # (box x, box_y)

    for i in range(box[1]*3, box[1]*3+3):
        for j in range(box[0]*3, box[0]*3+3):
            if board[i,j] == num:
                return(False)
    
    return(True)

if __name__ == "__main__":
    main()