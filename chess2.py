

board = ['.', 'P', 'R', 'N', 'B', 'K', 'Q']
notation_letter= ['A','B','C','D','E','F','G','H']
notation_number = ['1', '2', '3', '4', '5', '6', '7','8']  

#startpos=True generates starting board for create_board()
#inputformat will be: letternumberletternumber, with the first set indicating the piece the player wants to move and the last set indicating the place the players wants to move that piece



def coordinate_positions(startpos, usermove,player): #create dictionary of coordinates for plain board
    
    coordinate_list = [] #full list contianing rows (seperate dicts

    #create a rows as dictionaries
    for i in reversed(range(8)):
        row_dict = {}
        for letter in notation_letter:
            row_dict[letter+notation_number[i]] = board[0] + '  '
        coordinate_list.append(row_dict)
        continue

    if startpos == True:
        for row in coordinate_list:
            for key in row.keys():
                if '8' in key or '1' in key:
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
                elif '7' in key or '2' in key:
                    row[key] = board[1] + '  '


    if usermove == True:


        def playermove(player):

        
            player.split()              #these three lines split up user input into respective parts
            move_from = ''.join(player[0]+player[1])
            move_to = ''.join(player[2]+player[3])
            

            #change dictionary values
            #print(coordinate_list[8-int(move_from[1])])
            for key, val in coordinate_list[8-int(move_from[1])].items():
                if move_from == key:
                    print('yuh')
                    tempcopy = coordinate_list[8-int(move_from[1])][key]
                    coordinate_list[8-int(move_from[1])][key] =  coordinate_list[8-int(move_to[1])][move_to]
            
    
            #print(coordinate_list[8-int(move_to[1])])
            for key, val in coordinate_list[8-int(move_to[1])].items():
                if move_to == key:
                    print('bih')
                    coordinate_list[8-int(move_to[1])][key] = tempcopy #coordinate_list[8-int(move_from[1])][move_from]



        
        
        



        playermove(player)
    return coordinate_list


def give_board(startpos = False, usermove = False, player = False): #create full visual board  
    x = coordinate_positions(startpos, usermove, player )
    notation_number_string = 8   #notation number counter start
    for row in x: #each element in coordinate_list represents a row of the baord
        rowstr = str(notation_number_string) + '   '  #adding notation number at beginning of every row
        for key in row.keys():  #generate plain board
            rowstr +=  row[key]
        print(rowstr)  
        notation_number_string -= 1 #inc notation number

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
    player_one = str(input('Player 1:  ')).upper()
    give_board(startpos=True, usermove=True, player = player_one)
    player_two = str(input('Player 2:  ')).upper()
    give_board(startpos=True, usermove=True, player = player_two)
