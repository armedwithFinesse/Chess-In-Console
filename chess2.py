
board = ['.', 'P', 'R', 'N', 'B', 'K', 'Q']
notation_letter= ['A','B','C','D','E','F','G','H']
notation_number = ['1', '2', '3', '4', '5', '6', '7','8']  



def coordinate_positions(): #create dictionary of coordinates for plain board
    coordinate_list = [] #full list contianing rows (seperate dicts)

    #create a rows as dictionaries
    indexofnotationnum = 0
    while indexofnotationnum < 8:
        row_dict = {}
        for letter in notation_letter:
            row_dict[letter+notation_number[indexofnotationnum]] = board[0] + '  '
        indexofnotationnum += 1
        coordinate_list.append(row_dict)
        continue

    return coordinate_list


def create_row(coordinate_list): #return plain rows (visual)
    notation_number_string = 8   #notation number counter start
    for row in coordinate_list: #each element in coordinate_list represents a row of the baord
        rowstr = str(notation_number_string) + '   '  #adding notation number at beginning of every row
        for key in row.keys():  #generate plain board
            rowstr +=  row[key]
        print(rowstr)  
        notation_number_string -= 1 #inc notation number


def notation(): #visual notation
    notation_letter_string = '    '
    for i in notation_letter:
        notation_letter_string += i + '  '
    print('\n'+notation_letter_string)
    


def create_board(): #create full visual board from rows made by create_row()
    create_row(coordinate_positions())
    notation()





def update_board(): #update the board based on input from the user
    pass

    
   
    
def piece_movement():# how pieces should move. pawn sub function, rook subfunction, etc
    def pawnMovement():
        pass
    def RookMovement():
        pass
    pass



create_board()