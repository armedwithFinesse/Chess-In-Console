''' 
    Final Goals for the chess logic

    1) ensure pieces can't capture other pieces belonging to its own side
    2) ensure no piece can travel with it's own side in the way
    3) ensure each piece moves in accordance with its nature as specified by the rules of chess
        (1,2,3) give each piece-type a set of possible moves from its current position and only allow pieces to move there if said possible move is either an emoty space or an enemy piece

    4) ensure checks (and thus unchecks) work
    5) add colorama for checks'''
    
#only 3 pieces of starting information to create the whole game


from re import I


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


#keeps record of pieces with respect to which side they belong to. Important for piece interaction logic
white_dictionary = {}
black_dictionary = {}


def gameplay():
    game = True
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
    possible_move_to_list = []



    '''compare the value of move_from to a piece in the dictionary. If they are the same, then call pieceMovement function. If they are not the same, handle exception'''
    '''or compare move_from literal to a key in the colordict. If they are the same, then call the pieceMOvement function. If not, handle exception'''


    for key, value in colordict.items():
        if key == move_from:
            possible_move_to_list = piece_movement(coordinate_list, colordict, move_from, move_to)
            didpass = True
            break #piece_movement_list should be returned at this point 
        else:
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
        if move_from == key and (board[5] + '  ') in possible_move_to_list:
            tempcopy = board[5] + '  '
            coordinate_list[8-int(move_from[1])][key] = board[0]+'  ' #checks for pawn promotion
            didpass = True
            break
        elif move_from == key and (board[5].lower() + '  ') in possible_move_to_list:
            tempcopy = board[5].lower() + '  '
            coordinate_list[8-int(move_from[1])][key] = board[0]+'  ' #checks for pawn promotion
            didpass = True
            break

        elif move_from == key and ((board[5] + '  ') not in possible_move_to_list or ((board[5].lower() + '  ') in possible_move_to_list)) : #checks for not-pawn promotion
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

        #updates colordict with positions of pieces
        colordict[move_to] = colordict[move_from]
        del colordict[move_from]
        didpass = True
    else:
        coordinate_list[8-int(move_from[1])][move_from]  = tempcopy
        didpass = False

   
        


    





    



    #print(colordict)




    #print(didpass)
    
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


    elif startpos == 'promotion_test':
        for row in coordinate_list:
            for key, value in row.items():
                if "A7" == key:
                    row[key] = board[1] + '  '
                    white_dictionary[key] = board[1] + '  '
                elif 'A2' == key:
                    row [key] = board[1].lower() + '  '
                    black_dictionary[key] = board[1].lower() + '  '


    elif startpos == 'rooktest':
        for row in coordinate_list:
            for key, value in row.items():
                if "A1" == key:
                    row[key] = board[2] + '  '
                    white_dictionary[key] = board[2] + '  '
                elif 'A8' == key:
                    row [key] = board[2].lower() + '  '
                    black_dictionary[key] = board[2].lower() + '  '

        






              
                

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
            return diagdirection

                                    

        possible_move_to_list = []

        

        #a & b
        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
                if movefrom[1] == '2' or movefrom[1] == '7':
                    adder = blackorwhite(2)
                else:
                    adder = blackorwhite(1)
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
                leftdiag = diagcapture(leftdiag ,left_of_current_key)
                rightdiag = ''
                rightdiag = diagcapture(rightdiag, right_of_current_key)


            
                
                               
        #d

        #e
        '''when pawn reaches opposite back rank, it promotes to a piece of the players choosing'''

        '''@@@@@@@@@@@@@@@@@@@@~W.I.P.~@@@@@@@@@@@@@@@@@@@@@@@need to write  test that checks if pawns can be promoted. Also need to finish pawn promotion and en pessant@@@@@@@@@@@@@@@@@@@@~W.I.P~@@@@@@@@@@@@@@@@@@2'''
        def promotion(ranknum, pawntype, promotedpiece):
            for key, value in coordinate_list[ranknum].items():
                if moveto == key and colordict[movefrom] == pawntype:
                    #coordinate_list[0][key] = promotedpiece
                    coordinate_list[ranknum].update({key : promotedpiece})
                    possible_move_to_list.append(coordinate_list[ranknum][key])

                    if pawntype == board[1] + '  ':
                        print('white pawn promoted')
                    elif pawntype == board[1].lower() + '  ':
                        print('black pawn promoted')
                
             
            
            
            return None



        '''for key, value in coordinate_list[0].items():
            if moveto == key and colordict[movefrom] =='P' + '  ':
                coordinate_list[0][key] = 'Q' + '  '
                possible_move_to_list.append(coordinate_list[0][key])
                print('white pawn promoted')
        for key, value in coordinate_list[7].items():
            if moveto == key and colordict[movefrom] =='p' + '  ':
                coordinate_list[7][key] = 'q' + '  '
                print('black pawn promoted')'''

        promoted = promotion(0, (board[1] + '  '), (board[5] + '  '))
        promoted = promotion(7, (board[1].lower() + '  '), (board[5].lower() + '  '))


                

        #f


        print(possible_move_to_list)
    
        return possible_move_to_list #this will get returned eventually back up to where piece_movement was first called

       
    def RookMovement(movefrom, moveto, coordinate_list):
        '''generate a list of avaliable moves given the circumstances
        find all spaces in front of, in back of, to the lft of , to the right of current position that are either empty or contain enemy pieces. 
        These positions are considered valid and put into possible_move_to_list'''

        #a) rook moved infintely vertically and horizantally
        #b) rook cannot jump over pieces
        print('rook moved')

        def blackorwhite(num):
            if colordict == white_dictionary:
                adder = num
            elif colordict == black_dictionary:
                adder = -num
            return adder

        

        possible_move_to_list = []

        #a
        #print(coordinate_list[8-int(movefrom[1])])
        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
            

                #get all possible (read: on board only) vertical moves from current position
                adder = blackorwhite(7)
                while adder != 0:
                    
                    potential_move_counter_filter = int(movefrom[1]) + adder
                    #print(potential_move_counter_filter)

                    #maintains board boundaries during calculation
                    if potential_move_counter_filter > 8 or potential_move_counter_filter < 1:
                        if colordict == white_dictionary:
                            adder -= 1
                        elif colordict == black_dictionary:
                            adder += 1
                        continue

                    
                    newmovefromvert = movefrom[0] + str(potential_move_counter_filter)
                    possible_move_to_list.append(newmovefromvert)
                    if colordict == white_dictionary:
                        adder -= 1
                    elif colordict == black_dictionary:
                        adder += 1
    
                #get all possible (read: on board only) horizantal moves from current position
                for i in notation_letter:
                    asciival = ord(i)
                    newmovefromhoriz = chr(asciival) + movefrom[1]
                    possible_move_to_list.append(newmovefromhoriz)


        #b
        #prune list for moves that can't exist due to piece obstruction 
        
           #if a space is both a canadate move and resides in the players current (colordict) dictionary (meaning said canadate move is occupied by the players own piece),
           #remove the move from possible move list 
        for key, value in colordict.items():
            if key in possible_move_to_list:
                possible_move_to_list.remove(key)
        
            
          

            






            



        
                #vertical increment by 1 (keep key_zero the same and only change key_one) everything chronologically after key should be taken out
           


                


                '''adder = blackorwhite(1)

                for i in range(9):
                    key_one = int(key_one)
                    key_one += adder
                    new_move = key[0] + str(key_one)
                    if new_move in possible_move_to_list:
                        possible_move_to_list.remove(new_move)'''

                #horiantal increment by 1 (keep key_one the same and only change kay-zero) this part doesn't

                '''adder = blackorwhite(1)

                for i in range(9):
                    key_zero = ord(key[0])
                    key_zero += adder
                    new_move = chr(key_zero) + key[1]
                    if new_move in possible_move_to_list:
                        possible_move_to_list.remove(new_move)'''
                    











            


                '''adder = blackorwhite(1)
                for i in range(9):
                    
                    vertical_block = key[0] + str(int(key[1]) + adder)

                    print(vertical_block)
                
                
                    horizantal_block = chr(ord(key[0]) + adder) + key[1]

                    print(horizantal_block)

                    if vertical_block in colordict.keys():
                        if vertical_block in possible_move_to_list:
                            possible_move_to_list.remove(vertical_block)

                    if horizantal_block in colordict.keys():
                        if horizantal_block in possible_move_to_list:
                            possible_move_to_list.remove(horizantal_block)
                

                    adder += 1'''

            
                '''turn key into key[0] and key[1] and then increment by 1 and remove from list.'''

                '''key_zero = key[0]
                key_one = key[1]

                #vertical increment by 1 (keep key_zero the same and only change key_one) this part works
                adder = blackorwhite(1)

                for i in range(9):
                    key_one = int(key_one)
                    key_one += adder
                    new_move = key[0] + str(key_one)
                    if new_move in possible_move_to_list:
                        possible_move_to_list.remove(new_move)

                #horiantal increment by 1 (keep key_one the same and only change kay-zero) this part doesn't

                adder = blackorwhite(1)

                for i in range(9):
                    key_zero = ord(key[0])
                    key_zero += adder
                    new_move = chr(key_zero) + key[1]
                    print(new_move)
                    if new_move in possible_move_to_list:
                        possible_move_to_list.remove(new_move)'''
                    


            #must now remove spaces that would require jumping, as rooks cannot jump pieces

        '''current_key_index = possible_move_to_list.index(key)'''


        
               




        

            

        


    
        
        






    
            
                
                



                


        print(possible_move_to_list)

        return possible_move_to_list
                



        


    def KnightMovement():
        print('knight moved')
    def BishopMovement(movefrom, moveto, coordinate_list):
        print('bishop moved')


        #a) bishop moved infintely diagonally
        #b) bishop cannot jump over pieces

        possible_move_to_list = []
      

        #a
        #print(coordinate_list[8-int(movefrom[1])])
        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
            
                '''get current position and then stairstep spaces from each corner. then prune what is invalid'''

            letter = ord(movefrom[0])
            number = int(movefrom[1])

            direction_list = [1, -1]

            while direction_list[0] < 9:
                for i in direction_list:

                    newletter = letter + i
                    newnumber = number + i
                    newmove = chr(newletter) + str(newnumber)


                    for row in coordinate_list:
                        for key in row.keys():
                            if newmove == key and newmove not in possible_move_to_list:

                                possible_move_to_list.append(newmove)
                    
                    newletter = letter - i
                    newnumber = number + i
                    newmove = chr(newletter) + str(newnumber)

                    
                    for row in coordinate_list:
                        for key in row.keys():
                            if newmove == key and newmove not in possible_move_to_list:

                                possible_move_to_list.append(newmove)

                    

                    direction_list[0] += 1
                    direction_list[1] += 1

                


    #prune invalid spaces that i) are occupied by sides own pieces
       
        for key, value in colordict.items():
            if key in possible_move_to_list:
                possible_move_to_list.remove(key)
            



        #b
        #and ii) would require jumping to get to, as bishops don't jump over pieces.\ WIP################

    
        print(possible_move_to_list)  

        return possible_move_to_list                      





                     

                    

                        






    def KingMovement(movefrom, moveto, coordinate_list):
        print('king moved')

        def blackorwhite(num):
            if colordict == white_dictionary:
                adder = num
            elif colordict == black_dictionary:
                adder = -num
            return adder

        possible_move_to_list = []


        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
                adder = blackorwhite(1)
                while adder != 0:
                    potential_move_counter_filter = int(movefrom[1]) + adder
                    newmovefrom = movefrom[0] + str(potential_move_counter_filter)
                    possible_move_to_list.append(newmovefrom)
                    
                    if colordict == white_dictionary:
                        adder -= 1
                    elif colordict == black_dictionary:
                        adder += 1


                letter = ord(movefrom[0])
                number = int(movefrom[1])

                direction_list = [1, -1]

                for i in direction_list:

                    newletter = letter + i
                    newnumber = number + i
                    newmove = chr(newletter) + str(newnumber)


                    for row in coordinate_list:
                        for key in row.keys():
                            if newmove == key and newmove not in possible_move_to_list:

                                possible_move_to_list.append(newmove)
                    
                    newletter = letter - i
                    newnumber = number + i
                    newmove = chr(newletter) + str(newnumber)

                    
                    for row in coordinate_list:
                        for key in row.keys():
                            if newmove == key and newmove not in possible_move_to_list:

                                possible_move_to_list.append(newmove)

                    


            #prune invalid spaces that i) are occupied by sides own pieces
       
        for key, value in colordict.items():
            if key in possible_move_to_list:
                possible_move_to_list.remove(key)

        print(possible_move_to_list)

        return possible_move_to_list


    def QueenMovement(movefrom, moveto, coordinate_list):
        print('queen moved')

        def blackorwhite(num):
            if colordict == white_dictionary:
                adder = num
            elif colordict == black_dictionary:
                adder = -num
            return adder


        possible_move_to_list = []
      

        #a
        #print(coordinate_list[8-int(movefrom[1])])
        for key in coordinate_list[8-int(movefrom[1])]:
            if movefrom == key:
            
                '''get current position and then stairstep spaces from each corner. then prune what is invalid'''

            letter = ord(movefrom[0])
            number = int(movefrom[1])

            direction_list = [1, -1]

            while direction_list[0] < 9:
                for i in direction_list:

                    newletter = letter + i
                    newnumber = number + i
                    newmove = chr(newletter) + str(newnumber)


                    for row in coordinate_list:
                        for key in row.keys():
                            if newmove == key and newmove not in possible_move_to_list:

                                possible_move_to_list.append(newmove)
                    
                    newletter = letter - i
                    newnumber = number + i
                    newmove = chr(newletter) + str(newnumber)

                    
                    for row in coordinate_list:
                        for key in row.keys():
                            if newmove == key and newmove not in possible_move_to_list:

                                possible_move_to_list.append(newmove)

                    

                    direction_list[0] += 1
                    direction_list[1] += 1




                      #get all possible (read: on board only) vertical moves from current position
                adder = blackorwhite(7)
                while adder != 0:
                    
                    potential_move_counter_filter = int(movefrom[1]) + adder
                    #print(potential_move_counter_filter)

                    #maintains board boundaries during calculation
                    if potential_move_counter_filter > 8 or potential_move_counter_filter < 1:
                        if colordict == white_dictionary:
                            adder -= 1
                        elif colordict == black_dictionary:
                            adder += 1
                        continue

                    
                    newmovefromvert = movefrom[0] + str(potential_move_counter_filter)
                    possible_move_to_list.append(newmovefromvert)
                    if colordict == white_dictionary:
                        adder -= 1
                    elif colordict == black_dictionary:
                        adder += 1
    
                #get all possible (read: on board only) horizantal moves from current position
                for i in notation_letter:
                    asciival = ord(i)
                    newmovefromhoriz = chr(asciival) + movefrom[1]
                    possible_move_to_list.append(newmovefromhoriz)


                


    #prune invalid spaces that i) are occupied by sides own pieces
       
        for key, value in colordict.items():
            if key in possible_move_to_list:
                possible_move_to_list.remove(key)
            



        #b
        #and ii) would require jumping to get to, as queens don't jump over pieces.\ WIP################

    
        print(possible_move_to_list)  

        return possible_move_to_list                      


                



   #validates the piece that the player wants to move
    print(colordict[movefrom])
    if colordict[movefrom] =='P' + '  ' or colordict[movefrom] == 'p' + '  ':
        possible_move_to_list = pawnMovement(movefrom, moveto, coordinate_list)
    elif colordict[movefrom] == 'R'+ '  'or colordict[movefrom] == 'r' + '  ':
        possible_move_to_list = RookMovement(movefrom, moveto, coordinate_list)
    elif colordict[movefrom] == 'N'+ '  'or colordict[movefrom] == 'n' + '  ':
        KnightMovement()
    elif colordict[movefrom] == 'B'+ '  'or colordict[movefrom] == 'b' + '  ':
        possible_move_to_list = BishopMovement(movefrom, moveto, coordinate_list)
    elif colordict[movefrom] == 'K'+ '  'or colordict[movefrom] == 'k' + '  ':
        possible_move_to_list = KingMovement(movefrom, moveto, coordinate_list)
    elif colordict[movefrom] == 'Q'+ '  'or colordict[movefrom] == 'q' + '  ':
        possible_move_to_list = QueenMovement(movefrom, moveto, coordinate_list)
    else:
        print('something went wrong')


        


   
    return possible_move_to_list

    

    

def errorHandling():
    '''This function will take piece properties and apply them to the game. Checks, unchecks, etc'''
    pass



give_board(startpos=True) #'promotion_test', True, False, 'rooktest'



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