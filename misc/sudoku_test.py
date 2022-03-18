#this is the wrong file, where is the finished script?
#this was one of my first Python scripts in modern times while I was starting to think about a career move...I know it's not good but it was a start and it made me happy
#well, the finished version did but I can't seem to find it lol
arr=[[None for y in range(9)]
           for x in range(9)]

#for a in range(9):
#    print(a)

#ar = numpy.empty([9][9], dtype=object)
#needs numpy imported but is just a short hand for this but as far as I can tell only does 1 dimension?


#create a multidemensional array of 9x9x2 with value null for each
#we will use the 9x9x[0] for list of possible values (yes another array) and the 9x9x[1] as a boolean for whether answer is locked (as long as only one value in array)

#for x in range(1,10):
#    print(x)
#    arr[x-1] = [None]*9

#for x in range(1,10):
#    print(x)
#    for i in range(1,10):
#        print(i)
#        arr[x-1][i-1] = [None]*2


for x in range(9):
    for y in range(9):
        arr[x][y]=[1,2,3,4,5,6,7,8,9]

#arr[x][y].remove(value) this is how we remove the first occurence of a value in a list 
#print(arr)

#init example starter puzzle for working, long term will use reading from a csv
example_puzzle = [[None for y in range(9)]for x in range(9)]
example_puzzle[0][2]=7
example_puzzle[0][4]=6
example_puzzle[0][5]=8
example_puzzle[0][6]=9
example_puzzle[0][7]=1
example_puzzle[1][5]=2
example_puzzle[1][6]=6
example_puzzle[1][7]=8
example_puzzle[1][8]=7
example_puzzle[2][2]=3
example_puzzle[2][3]=1
example_puzzle[2][7]=5
example_puzzle[2][8]=4
example_puzzle[3][0]=7
example_puzzle[3][1]=6
example_puzzle[3][2]=4
example_puzzle[3][3]=2
example_puzzle[3][7]=3
example_puzzle[3][8]=8
example_puzzle[4][0]=5
example_puzzle[4][6]=1
example_puzzle[4][7]=6
example_puzzle[4][8]=2
example_puzzle[5][0]=1
example_puzzle[5][6]=4
example_puzzle[6][5]=6
example_puzzle[6][8]=5
example_puzzle[7][0]=3
example_puzzle[7][4]=5
example_puzzle[7][5]=1
example_puzzle[7][6]=7
example_puzzle[7][8]=6
example_puzzle[8][2]=6
example_puzzle[8][3]=4
example_puzzle[8][4]=7
example_puzzle[8][6]=8
example_puzzle[8][7]=9
example_puzzle[8][8]=1

#so, now we have example_puzzle with the values of a starter puzzle and arr with all possible values in each cell (1-9)

replacement =  { #replace all None with 0 to print list easier?
    None: 0
}


for i in range(9):
    example_puzzle[i] = [replacement.get(x,x) for x in example_puzzle[i]] # 
    
    
    
#for i in range(9):
    #print(example_puzzle[i])



for x in range(9):
    for y in range(9):
        #this is where we want to process each cell and check for eliminations
        #print("cell value is: ",example_puzzle[x][y])
        #print(arr[x][y])
        values = [1,2,3,4,5,6,7,8,9] # for later processes we could populate
        #values list with smaller or individual entries and use same logic bellow
        #to remove from arr[x][y] possible values cells
        if example_puzzle[x][y] != 0: #as long as not 0
            #print("should delete")
            for z in values:         #iterate through
                if z != example_puzzle[x][y]:
                    #print(z)
                    arr[x][y].remove(z) #note, while iterating over z in list
                    #and then conditionally removing z from same list - remove
                    #func seems to cause skipping of next z iteration in list
                    #resulting in removing only half the required items??
                    #solution is to populate list of numbers to remove and then
                    #iterate z of separate list and conditionally remove z from
                    #main list (arr[x][y]) per iteration
                    #summary, don't  iterate over a list and cause changes to
                    #same list inside iterations of itself.... at least not with
                    #remove function
            
        #print(arr[x][y])

for i in range(9):
    #for z in range(9):
    #print(example_puzzle[i][z])
    print(arr[i])



#so, now we have an array with lists of possible values and the starting known values as sole entries in such lists

#we can try implementing the first logical process, of going through each cell in the array and looking for a matched known value in the same row,column,block or diagonal

for x in range(9):
    for y in range(9):#here we would go through each cell



        #algorythm

        to_remove = []
        
        #get row in new list
        row = []
        for i in example_puzzle[x]:
            if i > 0:
                row.append(i)
        
        #get column in new list

        col = []

        for i in range(9):
            col.append(example_puzzle[x][i])
        
        #get block
        block = []
        #what do we need to do to get the block around x,y

        x_start = int(x/3)*3 #find the start and end points of the 3x3 block the cell is in#find the start and end points of the 3x3 block the cell is in#find the start and end points of the 3x3 block the cell is in
        x_end = x_start+2
        y_start = int(y/3)*3
        y_end = y_start + 2

        for i in range(x_start,x_end+1):  #iterate through each value in the block the cell is in
            for j in range(y_start,y_end+1):
                if example_puzzle[i][j] != 0:        #if not zero then add to "block" - list of values in block the cell is in
                    block.append(example_puzzle[i][j])
        
        #this is proved to work between here
        values = arr[x][y]
        removed_values =[]
        if len(values) > 1: #if not already solved for cell
            print("Values list of current cell(",x,",",y,"): ",values)
            for value in values: #for each possible value in arr[x][y] list - 
                #print("Value ",value," in values")
                if (value in row) or (value in col) or (value in block): #if value is a solved answer in row x, col y or block
                    #print("removing ", value, " from values ", values, " --- ", arr[x][y])
                    removed_values.append(value) #we add this value to the list of removals (removal happens outside of this loop)
                    #arr[x][y].remove(value)


            for a in removed_values:   # now remove the values from possible list of values for current cell
                arr[x][y].remove(a)    # THIS WORKS HAZAAA!!! Because python uses reference not assignment I needed to append values to list to then remove that separate list from main list outside of loop due to voodoo
                                        #basically don't change object being used for iteration inside of iteration
                
        #Diagonal check? ----------------------------------------------------------------------------------------------
    
        #now check if cell is solved?
        if len(arr[x][y])==1 and example_puzzle[x][y] == 0:
            example_puzzle[x][y] = arr[x][y][0] #and change the 0 to remaining 1 value from possible values list for this cell arr[x][y]
            #because we used the fact there is only one entry in the possible values list for this cell we don't need to update arr array at all at this point




for i in range(9):
    #for z in range(9):
    #print(example_puzzle[i][z])
    print(arr[i])

for i in range(9):
    print(example_puzzle[i])





