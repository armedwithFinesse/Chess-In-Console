''' 
    Final Goals for the chess logic

    1) ensure pieces can't capture other pieces belonging to its own side
    2) ensure no piece can travel with it's own side in the way
    3) ensure each piece moves in accordance with its nature as specified by the rules of chess
        (1,2,3) give each piece-type a set of possible moves from its current position and only allow pieces to move there if said possible move is either an emoty space or an enemy piece

    4) ensure checks (and thus unchecks) work
    5) add colorama for checks'''
    
#only 3 pieces of starting information to create the whole game



board = ['.', 'P', 'R', 'N', 'B','Q','K']
notation_letter= ['A','B','C','D','E','F','G','H']
notation_number = ['1', '2', '3', '4', '5', '6', '7','8']  

#startpos=True generates starting board for create_board()
#inputformat will be: letternumberletternumber, with the first set indicating the piece the player wants to move and the last set indicating the place the players wants to move that piece

'''This creates an empty board by default'''
coordinate_list = [] #full list contianing rows (seperate dicts)
#global didpass
#didpass = True

#create a rows as dictionaries
for i in reversed(range(8)):
    row_dict = {}
    for letter in notation_letter:
        row_dict[letter+notation_number[i]] = board[0] + '  '
    coordinate_list.append(row_dict)
    continue


#keeps record of pieces with respect to which side they belong to. Important for piece interaction logic
white_dictionary = {}
black_dictionary = {}


def gameplay():
    game = True
    #global didpass
    while game == True:
        while True:
            player_one = str(input('\n'+'Player 1:  ')).upper()
            print('\n')
            didpass = give_board(usermove=True, player = player_one, colordict=white_dictionary) #bool returning None
            print(didpass)

            if didpass == False:
                print('Please enter a valid move')
                continue
            elif didpass == True:
                break
            
        while True:
            player_two = str(input('\n'+'Player 2:  ')).upper()
            print('\n')
            didpass = give_board(usermove=True, player = player_two, colordict=black_dictionary)
            if didpass == False:
                print('Please enter a valid move', end='')
                continue
            elif didpass == True:
                break
                


 #takes input from player and parses it to be manipulated in the dictionary
def playermove(player, colordict):
    '''Takes the input 'player' (keyword-string) which is the players move (coordinates) and uses it to update coordinates in dictionaries'''

    #these three lines split up user input into respective parts (move to) and (move from)
    player.split()             
    move_from = ''.join(player[0]+player[1])
    #player.split()             
    move_to = ''.join(player[2]+player[3])
    #possible_move_to_list = []



    '''compare the value of move_from to a piece in the dictionary. If they are the same, then call pieceMovement function. If they are not the same, handle exception'''
    '''or compare move_from literal to a key in the colordict. If they are the same, then call the pieceMOvement function. If not, handle exception'''


    for key, value in colordict.items():
        if key == move_from:
            possible_move_to_list = piece_movement(coordinate_list, colordict, move_from, move_to)
            didpass = True
            break #piece_movement_list should be returned at this point 
        else:
            possible_move_to_list = []
            didpass = False #needs to return to player input to give another attempt

    '''for key, value in coordinate_list[0]: #8th rank #do not delete, en pessant checker (is it neccessary?)
        if key == move_to:
            piece_movement(coordinate_list, colordict, move_from, move_to)
            break
        else:
            print('invalid')
    for key, value in coordinate_list[7]: #1st rank
        if key == move_to:
            piece_movement(coordinate_list, colordict, move_from, move_to)
            break
        else:
            print('invalid')'''
        



    #change dictionary values of move from to empty spaces
    for key, val in coordinate_list[8-int(move_from[1])].items():
        if move_from == key:
            tempcopy = coordinate_list[8-int(move_from[1])][key] 
            coordinate_list[8-int(move_from[1])][key] = board[0]+'  ' #replaces every moved from space with a dot, indicating empty square
            didpass = True
            break
        else:
            tempcopy = ''
            didpass = False
    #print(didpass)
    #changes dictionary values of move to to move from -- inherent piece capture mechanism
    '''for key, val in coordinate_list[8-int(move_to[1])].items():
        if move_to == key:
            coordinate_list[8-int(move_to[1])][key] = tempcopy #coordinate_list[8-int(move_from[1])][move_from]'''



    if move_to in possible_move_to_list:
        coordinate_list[8-int(move_to[1])][move_to] = tempcopy
        didpass = True
    elif move_to not in possible_move_to_list:
        coordinate_list[8-int(move_from[1])][move_from]  = tempcopy
        didpass = False

            

    print(didpass)
    
    return didpass


        
def coordinate_positions(startpos, usermove,player, colordict):  #create dictionary of coordinates for plain board

    '''Inputs: 'startpos' (bool), 'usermove'(bool), 'player'(keyword)
    This function determines the position of the visual gameboard in relation to the ever updating dictionary definitions of positions'''

    #gives the starting position of a chess game and updates dictionaries relating to property and position of pieces

    if startpos == True:
        for row in coordinate_list:
            for key in row.keys():
                if '1' in key:
                    if 'A' in key or 'H' in key:
                        row[key] = board[2] + '  '
                    elif 'B' in key or 'G' in key:
                        row[key] = board[3] + '  '
                    elif 'C' in key or 'F' in key:
                        row[key] = board[4] + '  '
                    elif 'D' in key:
                        row[key] = board[5] + '  '
                    elif 'E' in key:
                        row[key] = board[6] + '  '
                    white_dictionary[key] = (row[key])
                elif '8' in key:
                    if 'A' in key or 'H' in key:
                        row[key] = board[2].lower() + '  '
                    elif 'B' in key or 'G' in key:
                        row[key] = board[3].lower() + '  '
                    elif 'C' in key or 'F' in key:
                        row[key] = board[4].lower() + '  '
                    elif 'D' in key:
                        row[key] = board[5].lower() + '  '
                    elif 'E' in key:
                        row[key] = board[6].lower() + '  '
                    black_dictionary[key] = (row[key])
                   
                elif '2' in key:
                    row[key] = board[1] + '  '
                    white_dictionary[key] = (row[key])

                elif '7' in key:
                    row[key] = board[1].lower() + '  '
                    black_dictionary[key] = (row[key])



                

    #indicates that a player will be making a move
    didpass = ''
    if usermove == True:
        didpass = playermove(player, colordict)
    return coordinate_list, didpass #calls the updated dictionary and thus updates the visual board 



def give_board(startpos = False, usermove = False, player = False, colordict = white_dictionary): #create full visual board  
    '''gives default values of all optional parameters'''

    #allows the board to reference the dictionaries containing the positions of the pieces
    x = coordinate_positions(startpos, usermove, player, colordict)
    notation_number_string = 8   #notation number counter start
    for row in x[0]: #each element in coordinate_list represents a row of the baord
        rowstr = str(notation_number_string) + '   '  #adding notation number at beginning of every row
        for key in row.keys():  #generate plain board
            rowstr +=  row[key]

         #denotes white and black
        if notation_number_string == 7:
            print(rowstr + '      '+'Black: lowercase')
        elif notation_number_string == 6:
            print(rowstr + '      '+'White: UPPERCASE')
        else:
            print(rowstr)  

        notation_number_string -= 1 #inc notation number

    #adds notation letters to the bottom of the board
    notation_letter_string = '    '
    for i in notation_letter:
        notation_letter_string += i + '  '
    print('\n'+notation_letter_string)
 
   
    didpass = x[1]
    return didpass


def update_board(player_one='', player_two=''):
    pass
              

def piece_movement(coordinate_list, colordict, movefrom, moveto):# how pieces should move. pawn sub function, rook subfunction, etc
    '''takes current position of a piece and assesses it for future avaliable moves'''
    '''(1,2,3) give each piece-type a set of possible moves from its current position and
     only allow pieces to move there if said possible move is either an empty space or an enemy piece'''


    print('piece_movement has been successfully called!')



    #these functions should save the avaliable moves for any given position for every piece. The return value will be compared to the players move-to
    #back in the player_move function and if they match the game will proceed. If not, the input will be marked invalid and player will be given another
    #chance to input a valid move
    def pawnMovement(movefrom, moveto, coordinate_list): #WIP
        '''generate a list of avaliable moves given the circumstances'''
        print('pawn moved')
        #a) max 2 space headstart when leaving home rank
        #b) 1 space movement patten
        #c) 1 space diagonal capture
        #d) en pessant
        #e) promotion
        #f) can't move over own side

        def blackorwhite(num):
            if colordict == white_dictionary:
                adder = num
            elif colordict == black_dictionary:
                adder = -num
            return adder


        def diagcapture(diagdirection, side_key):
            adder = blackorwhite(1)
            diagdirection = list(key_list[side_key])
            for i in diagdirection:
                if i == diagdirection[1]:
                    diag_num = int(diagdirection[1]) + adder
                    diagdirection = diagdirection[0] + str(diag_num)
                    possible_move_to_list.append(diagdirection)
            return None

                                    

        possible_move_to_list = []

        #a & b
        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
                adder = blackorwhite(2)
                while adder != 0:
                    potential_move_counter_filter = int(movefrom[1]) + adder
                    newmovefrom = movefrom[0] + str(potential_move_counter_filter)
                    possible_move_to_list.append(newmovefrom)
                    if colordict == white_dictionary:
                        adder -= 1
                    elif colordict == black_dictionary:
                        adder += 1


        #c
        key_list = []
        value_list = []
        for row in coordinate_list:
            for key, value in row.items():
                key_list.append(key)
                value_list.append(value) 

        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
                current_key = key_list.index(key)
                adder = blackorwhite(1)
                left_of_current_key = current_key - adder
                right_of_current_key = current_key + adder

                leftdiag = ''
                diagcapture(leftdiag ,left_of_current_key)
                rightdiag = ''
                diagcapture(rightdiag, right_of_current_key)
            
                
                               
        #d

        #e
        '''when pawn reaches opposeite back rank, it promotes to a piece of the players choosing'''


        def enpessant(ranknum, pawntype, promotedpiece):
            for key, value in coordinate_list[ranknum].items():
                if moveto == key and colordict[movefrom] == pawntype:
                    coordinate_list[0][key] = promotedpiece
                    if pawntype == 'P' + '  ':
                        print('white pawn promoted')
                    elif pawntype == 'p' + '  ':
                        print('black pawn promoted')
            return None




        '''for key, value in coordinate_list[0].items():
            if moveto == key and colordict[movefrom] =='P' + '  ':
                coordinate_list[0][key] = 'Q' + '  '
                print('white pawn promoted')
        for key, value in coordinate_list[7].items():
            if moveto == key and colordict[movefrom] =='p' + '  ':
                coordinate_list[7][key] = 'q' + '  '
                print('black pawn promoted')'''

        enpessant(0," 'P' + '  ' ", "'Q' + '  '")
        enpessant(7, "'p' + '  '", "'q' + '  '")


                



            
        '''for key, value in coordinate_list[0].items(): #8th rank of board
            if colordict == white_dictionary  and coordinate_list[0][key] == 'P' + '  ':
                print('white pawn ready for promotion')
                #coordinate_list[key] = 'Q' + '  '''


        '''for i in coordinate_list[0]: #tests
            print(coordinate_list[0][i])'''




    

        #f

        return possible_move_to_list #this will get returned eventually back up to where piece_movement was first called

       
    def RookMovement():
        print('rook moved')
    def KnightMovement():
        print('knight moved')
    def BishopMovement():
        print('bishop moved')
    def KingMovement():
        print('king moved')
    def QueenMovement():
        print('queen moved')

   #validates the piece that the player wants to move
    if colordict[movefrom] =='P' + '  ' or colordict[movefrom] == 'p' + '  ':
        possible_move_to_list = pawnMovement(movefrom, moveto, coordinate_list)
    elif colordict[movefrom] == 'R'+ '  'or colordict[movefrom] == 'r' + '  ':
        RookMovement()
    elif colordict[movefrom] == 'N'+ '  'or colordict[movefrom] == 'n' + '  ':
        KnightMovement()
    elif colordict[movefrom] == 'B'+ '  'or colordict[movefrom] == 'b' + '  ':
        BishopMovement()
    elif colordict[movefrom] == 'K'+ '  'or colordict[movefrom] == 'k' + '  ':
        KingMovement()
    elif colordict[movefrom] == 'Q'+ '  'or colordict[movefrom] == 'q' + '  ':
        QueenMovement()
    else:
        print('something went wrong')


        


   
    return possible_move_to_list

    

    

def errorHandling():
    '''This function will take piece properties and apply them to the game. Checks, unchecks, etc'''
    pass


give_board(startpos=True)



#print(coordinate_list)
#print(white_dictionary)
#print(black_dictionary)


'''while True:
    player_one = str(input('\n'+'Player 1:  ')).upper()
    print('\n')
    give_board(usermove=True, player = player_one, colordict=white_dictionary)

    player_two = str(input('\n'+'Player 2:  ')).upper()
    print('\n')
    give_board(usermove=True, player = player_two, colordict=black_dictionary)'''

gameplay()