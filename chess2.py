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

#create a rows as dictionaries
for i in reversed(range(8)):
    row_dict = {}
    for letter in notation_letter:
        row_dict[letter+notation_number[i]] = board[0] + '  '
    coordinate_list.append(row_dict)
    continue


#keeos record of pieces with respect to which side they belong to. Important for piece interaction logic
white_dictionary = {}
black_dictionary = {}


def gameplay():
    while True:
        player_one = str(input('\n'+'Player 1:  ')).upper()
        print('\n')
        give_board(usermove=True, player = player_one, colordict=white_dictionary)

        player_two = str(input('\n'+'Player 2:  ')).upper()
        print('\n')
        give_board(usermove=True, player = player_two, colordict=black_dictionary)


 #takes input from player and parses it to be manipulated in the dictionary
def playermove(player, colordict):
    '''Takes the input 'player' (keyword-string) which is the players move (coordinates) and uses it to update coordinates in dictionaries'''


    #these three lines split up user input into respective parts (move to) and (move from)
    player.split()             
    move_from = ''.join(player[0]+player[1])
    #player.split()             
    move_to = ''.join(player[2]+player[3])




    '''compare the value of move_from to a piece in the dictionary. If they are the same, then call pieceMovement function. If they are not the same, handle exception'''
    '''or compare move_from literal to a key in the colordict. If they are the same, then call the pieceMOvement function. If not, handle exception'''


    for key, value in colordict.items():
        if key == move_from:
            piece_movement(coordinate_list, colordict, move_from, move_to)
            break
        else:
            print('invalid') 
            #needs to return to player input to give another attempt



    #change dictionary values of move from to empty spaces
    for key, val in coordinate_list[8-int(move_from[1])].items():
        if move_from == key:
            tempcopy = coordinate_list[8-int(move_from[1])][key] 
            coordinate_list[8-int(move_from[1])][key] = board[0]+'  ' #replaces every moved from space with a dot, indicating empty square

    #changes dictionary values of move to to move from -- inherent piece capture mechanism
    for key, val in coordinate_list[8-int(move_to[1])].items():
        if move_to == key:
            coordinate_list[8-int(move_to[1])][key] = tempcopy #coordinate_list[8-int(move_from[1])][move_from]
        
              
    
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
    if usermove == True:

        playermove(player, colordict)

    return coordinate_list #calls the updated dictionary and thus updates the visual board



def give_board(startpos = False, usermove = False, player = False, colordict = white_dictionary): #create full visual board  
    '''gives default values of all optional parameters'''

    #allows the board to reference the dictionaries containing the positions of the pieces
    x = coordinate_positions(startpos, usermove, player, colordict )
    notation_number_string = 8   #notation number counter start
    for row in x: #each element in coordinate_list represents a row of the baord
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
    def pawnMovement(movefrom, moveto, coordinate_list):
        '''generate a list of avaliable moves given the circumstances'''
        print('pawn moved')
        #a) max 2 space headstart when leaving home rank
        #b) 1 space movement patten
        #c) 1 space diagonal capture
        #d) en pessant
        #e) promotion
        #f) can't move over own side
        possible_move_to_list = []

        #a
        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
                potential_move_counter_filter = int(movefrom[1]) + 2
                movefrom = movefrom[0] + str(potential_move_counter_filter)
                possible_move_to_list.append(movefrom) 

        
        #b
        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
                potential_move_counter_filter = int(movefrom[1]) + 1
                movefrom = movefrom[0] + str(potential_move_counter_filter)
                possible_move_to_list.append(movefrom) 


        #c #current WIP
        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
                #and(some code to calculate all foreward diagonals from current position) is equal to piece from opposite color dictionary:
                '''find the files directly next to the one where the current position sits and find the rank that is equal 
                to the current position on aforementioned files and then increase (or decrease in the cae of black) the 
                aforementioned file-rank coordinates by 1 such that the returned coordinates are in line with themselves 
                and diagonal to the current position'''

                potential_move_counter_filter = int(movefrom[1]) + 1
                movefrom = movefrom[0] + str(potential_move_counter_filter)
                possible_move_to_list.append(movefrom) 

        #d
        #e

        print(possible_move_to_list)
       
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
        pawnMovement(movefrom, moveto, coordinate_list)
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


        


   
    #return movefrom

    

    

def errorHandling():
    '''This function will take piece properties and apply them to the game. Checks, unchecks, etc'''
    pass


give_board(startpos=True)

#print(coordinate_list)
print(white_dictionary)
print(black_dictionary)


'''while True:
    player_one = str(input('\n'+'Player 1:  ')).upper()
    print('\n')
    give_board(usermove=True, player = player_one, colordict=white_dictionary)

    player_two = str(input('\n'+'Player 2:  ')).upper()
    print('\n')
    give_board(usermove=True, player = player_two, colordict=black_dictionary)'''

gameplay()