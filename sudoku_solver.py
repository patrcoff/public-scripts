#get sudoku data from somewhere

#for now we hardcode it

puzzle = [[None for y in range(9)]for x in range(9)] # create empty puzzle
puzzle[0][2]=7                                       #now add predefined puzzle values
puzzle[0][4]=6
puzzle[0][5]=8
puzzle[0][6]=9
puzzle[0][7]=1
puzzle[1][5]=2
puzzle[1][6]=6
puzzle[1][7]=8
puzzle[1][8]=7
puzzle[2][2]=3
puzzle[2][3]=1
puzzle[2][7]=5
puzzle[2][8]=4
puzzle[3][0]=7
puzzle[3][1]=6
puzzle[3][2]=4
puzzle[3][3]=2
puzzle[3][7]=3
puzzle[3][8]=8
puzzle[4][0]=5
puzzle[4][6]=1
puzzle[4][7]=6
puzzle[4][8]=2
puzzle[5][0]=1
puzzle[5][6]=4
puzzle[6][5]=6
puzzle[6][8]=5
puzzle[7][0]=3
puzzle[7][4]=5
puzzle[7][5]=1
puzzle[7][6]=7
puzzle[7][8]=6
puzzle[8][2]=6
puzzle[8][3]=4
puzzle[8][4]=7
puzzle[8][6]=8
puzzle[8][7]=9
puzzle[8][8]=1

replacement =  { #replace all None with 0 to print list easier?
    None: 0
}

for i in range(9):
    puzzle[i] = [replacement.get(x,x) for x in puzzle[i]] # I copied this from the web - this iterated through each row i, and replaces each cell with value x (None) in row puzzle[i] with replacement x (0)

#create 9x9 array of lists of possible values pos_vals
pos_vals=[[None for y in range(9)]
           for x in range(9)]
for x in range(9):
    for y in range(9):
        if puzzle[x][y] == 0:
            pos_vals[x][y] = [1,2,3,4,5,6,7,8,9]
        else:
            pos_vals[x][y] = []                            #blank the list
            pos_vals[x][y].append(puzzle[x][y])            #but keep it as an array so as to avoid converting to int

#create 9x9 array last_puzzle_state
for i in range(9):
    last_puzzle_state = [[None for y in range(9)]for x in range(9)]

#for i in range(9):
#    for j in range(9):
#        print(pos_vals[i][j])

for i in range(9):
    print(puzzle[i])



    #for each cell check if value is non zero in puzzle (already answered/confirmed)
    #if cell is zero, check if list of possible values for cell has more than one create entry, if not then single remaining possibel value > puzzle value in cell, but if yes then
    #create row, col and block lists for cell, add all values in row, col and block to removal list, for i in removal list, pos_vals.remove(i)
count = 0

solved = 0
#up to 81 counts per iteration
while count < 1500: #later we will debug how much the possible values lists change within x iterations to see if this number needs increased
    #we increment count at the end of the loop if last_puzzle_state == puzzle i.e. no change to puzzle
    #last_puzzle_state = puzzle # now we've set
    for x in range(9):
        for y in range(9):
            last_puzzle_state[x][y] = puzzle[x][y]
    for y in range(9):
        for x in range(9): #for each cell
            to_remove = []
            row = []
            col = []
            block = [] # these three will be appended with values found in relevant row, col, and block of cell
            diagonal = []
            #we also want a mechanism to test for unique value in pos_vals[x][y] compared to pos_vals[row, col, block..]
            unique_check = []
            #if puzzle[x][y] != 0:
                #here we are saying the puzzle for this cell is solved, ensure pos_vals[x][y]  is correct
                #NOT IMPLEMENTED YET -----------------------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if int(puzzle[x][y]) == 0:  #here we are saying puzzle cell not solved, so we check if value present in lists row, col, block (and diagonal yet to be added!!!!!!)
                #first check row
                for i in range(9): #populating row
                    if int(i)!=int(x): #to avoid counting data from current cell
                        for z in pos_vals[i][y]:  # add all possible values for each cell in row to unique_check
                            unique_check.append(z)
                        if puzzle[i][y] > 0: #add all non 0 values (solved values) from puzzle row to
                            row.append(puzzle[i][y])
                #then check col
                for i in range(9):
                    if int(i)!=int(y):
                        for z in pos_vals[x][i]: #we don't want to set pos_vals[x][y] to an integer ever but rather list of 1 items
                            unique_check.append(z)
                        if int(puzzle[x][i]) > 0:
                            col.append(puzzle[x][i])
                #whilst ading un_unique values to unique_check list
                #now block
                x_start = int(x / 3) * 3  # find the start and end points of the 3x3 block the cell is in#find the start and end points of the 3x3 block the cell is in#find the start and end points of the 3x3 block the cell is in
                x_end = x_start + 2
                y_start = int(y / 3) * 3
                y_end = y_start + 2

                for i in range(x_start, x_end + 1):  # iterate through each value in the block the cell is in
                    for j in range(y_start, y_end + 1):
                        if int(i)!=int(x) and int(j)!=int(y):      #ensure not adding current cell

                            for z in pos_vals[i][j]:
                                unique_check.append(pos_vals[i][j])
                            if puzzle[i][j] != 0:  # if not zero then add to "block" - list of values in block the cell is in
                                block.append(puzzle[i][j])
                print("------------------------")
                #diagonal unique check - the following adds the list of possible values for each cell in the diagonals except the current cell, only if cell is in diagonal
                #--------------Diagonal top left to bottom right---------------------------------------------------------------------------------------------------------------

                #--------------------------------------------------------------------------------------We need to know which diagonal the cell falls in-----------------------
                #--------------------------------------------------------------------------------------And then add known values to the relevant diagonal without adding cell

                #print("Debugging here")
                """
                if int(x)==int(y) or int(x)==int(8-y): #if it is a diagonal entry
                    print("Please note, I think this cell is in a diagonal!")
                    
                    for i in range(9):
                        if i!=x and i!=y: #don't add current cell's data of course
                            for z in pos_vals[i][i]: #Diagonal top left to bottom right
                                unique_check.append(pos_vals[i][i])
                            for z in pos_vals[i][8-i]: #Diagonal bottom left to top right
                                unique_check.append(pos_vals[i][8-i])
                    #-------------Diagonal bottom left to top right ---------------------------------------------------------------------------------------------------------------
                """
                #the above is a depricated method as it did not separate out the two different diagonals which is necessary as only x=4,y=4 is in both diagonals and needs to compare into both their lists of possible values

#the below may still be useful if using a non-standard puzzle where diagonals are required
                """
                if int(x)==int(y):   #this is the top left to bottom right diagonal
                    #do some stuff
                    for i in range(9):
                        if int(i) != int(x) and int(i) != int(y):  # don't add current cell's data of course
                            print("Debug: this isn't the diagonal you are looking for ", x, " ", y, " ", i, " ", i)
                            if puzzle[i][i] != 0:
                                diagonal.append(puzzle[i][i])
                            for z in pos_vals[i][i]:  # Diagonal top left to bottom right
                                unique_check.append(pos_vals[i][i])


                if int(x)==int((8-y)): # bottom left to top right
                    #do other stuff
                    for i in range(9):
                        if int(i) != int(x) and int(i) != int(8-y):  # don't add current cell's data of course
                            print("Debug: this isn't the diagonal you are looking for ",x," ", y," ",  i," ", 8-i)
                            if puzzle[i][(8-i)] != 0:
                                print("Debugging diagonal.append")
                                diagonal.append(puzzle[i][(8-i)])
                            for z in pos_vals[i][(8 - i)]:  # Diagonal bottom left to top right
                                unique_check.append(pos_vals[i][8 - i])
                                print("debug uniique.append")
                """


#LOLOLOLOLOL Just found out regular sudoku doesn't include any diagonal rules so the hardcoded puzzle has duplicates in its diagonal and can't be solved with unique diagonals



                values = []
                for i in pos_vals[x][y]: # list of possible values for cell put into values for iteration
                    values.append(i)     #doing it in a loop keeps it a list and not an int
                for value in values:
                    if (value in row) or (value in col) or (value in block):# or (value in diagonal):               #the diagonal is breaking it......................................................................somehow
                        to_remove.append(value) # list of values to remove from
                print("To remove: ", to_remove)
                for a in to_remove:
                    if a in pos_vals[x][y]:
                        pos_vals[x][y].remove(a) # will this work? not sure, it's not iterating over pos_vals but we are checking it and editing it in same scope? I'm still not sure how this all works in python but we'll se!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                values=[]
                #for i in pos_vals[x][y], if i not in pos_vals[for row, col and block]
                for i in pos_vals[x][y]:  # list of possible values for cell put into values for iteration
                    values.append(i)  # doing it in a loop keeps it a list and not an int

                if count >= 2:
                    for i in values: #WE SHOULD ALSO ADD IN A CHECK THAT THIS ISN'T THE FIRST ITERATION
                        if i not in unique_check: # if no other occurances of i in the possible lists for all other pos_val lists for cell's row,col, block and diagonals
                            pos_vals[x][y] = [] #blank the list
                            pos_vals[x][y].append(i) #then append the list so as not to convert to an int
                print(pos_vals[x][y])
                if len(pos_vals[x][y])==1: #if the pos_vals list  is now one then it is solved for this cell so we add it to the puzzle array
                    print("debug solved for cell")
                    solved += 1
                    puzzle[x][y] = pos_vals[x][y][0]
            if int(puzzle[x][y]) == 0:
                print("x=",x," y=",y," possible, values: ",pos_vals[x][y]," current value: ", puzzle[x][y])#Code not currently getting this far

    #need different way of comparing the bellow, for loops etc to compare


    for x in range(9):
        for y in range(9):

            if (last_puzzle_state[x][y] == puzzle[x][y]):
                count += 1
    #if last_puzzle_state == puzzle:
    #    count+=1
    #    print("Counting ", count)

for i in range(9):
    print(puzzle[i])

print("Solved for ", solved, " entries")

#check if change in puzzle from previous state?

#repeat if yes

#to here, we get through several iterations of elimination until elimination alone cannot suffice
#or maybe we add the below step into the logic of the main iteration above



# TO THIS POINT WE'VE USED ELIMINATION AND UNIQUE POSSIBLE VALUE LOGIC TO SOLVE