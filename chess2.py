
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


def coordinate_positions(startpos, usermove,player):  #create dictionary of coordinates for plain board

    '''Inputs: 'startpos' (bool), 'usermove'(bool), 'player'(keyword)
    This function determines the position of the visual gameboard in relation to the ever updating dictionary definitions of positions'''



    #gives the starting position of a chess game
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
                   
                elif '2' in key:
                    row[key] = board[1] + '  '
                elif '7' in key:
                    row[key] = board[1].lower() + '  '


                

    #indicates that a player will be making a move
    if usermove == True:

        #takes input from player and parses it to be manipulated in the dictionary
        def playermove(player):
            '''Takes the input 'player' (keyword-string) which is the players move (coordinates) and uses it to update coordinates in dictionaries'''


            #these three lines split up user input into respective parts (move to) and (move from)
            player.split()             
            move_from = ''.join(player[0]+player[1])
            #player.split()             
            move_to = ''.join(player[2]+player[3])
            
            #change dictionary values of move from to empty spaces
            for key, val in coordinate_list[8-int(move_from[1])].items():
                if move_from == key:
                    tempcopy = coordinate_list[8-int(move_from[1])][key]
                    coordinate_list[8-int(move_from[1])][key] = board[0]+'  ' #replaces every moved from space with a dot, indicating empty square
            

            #changes dictionary values of move to to move from -- inherent piece capture mechanism
            for key, val in coordinate_list[8-int(move_to[1])].items():
                if move_to == key:
                    coordinate_list[8-int(move_to[1])][key] = tempcopy #coordinate_list[8-int(move_from[1])][move_from]

        playermove(player)

    return coordinate_list #calls the updated dictionary and thus updates the visual board



def give_board(startpos = False, usermove = False, player = False): #create full visual board  
    '''gives default values of all optional parameters'''

    #allows the board to reference the dictionaries containing the positions of the pieces
    x = coordinate_positions(startpos, usermove, player )
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
              

def piece_movement():# how pieces should move. pawn sub function, rook subfunction, etc
    def pawnMovement():
        pass
    def RookMovement():
        pass
    pass



give_board(startpos=True)

while True:
    player_one = str(input('\n'+'Player 1:  ')).upper()
    print('\n')
    give_board(usermove=True, player = player_one)

    player_two = str(input('\n'+'Player 2:  ')).upper()
    print('\n')
    give_board(usermove=True, player = player_two)
