

boardvar = ['.', 'P', 'R', 'N', 'B', 'K', 'Q']
notation_letter= ['A','B','C','D','E','F','G','H']
notation_number = ['1', '2', '3', '4', '5', '6', '7','8'] 

class AlgebraicNotation:
    def __init__(self, board, notationletters, notationnumbers, coordobj = '') -> None:
        self.board = board
        self.notationletters = notationletters
        self.notationnumbers = notationnumbers
        self.coordobj = coordobj

    
    def coordinate_positions(self): #create dictionary of coordinates for plain board
        coordinate_list = [] #full list contianing rows (seperate dicts)

        #create a rows as dictionaries
        indexofnotationnum = 0
        while indexofnotationnum < 8:
            row_dict = {}
            for letter in self.notationletters:
                row_dict[letter+self.notationnumbers[indexofnotationnum]] = self.board[0] + '  '
            indexofnotationnum += 1
            coordinate_list.append(row_dict)
            continue

        

        return coordinate_list


class Board(AlgebraicNotation):
    coordobject = AlgebraicNotation(boardvar, notation_letter, notation_number)
    coordobj = coordobject.coordinate_positions()
    def __init__(self, board, notationletters, notationnumbers, coordobj=''):
        super().__init__(board, notationletters, notationnumbers, coordobj)

    def create_row(self): #return plain rows (visual)

        notation_number_string = 8   #notation number counter start
        for row in Board.coordobj: #each element in coordinate_list represents a row of the board
            rowstr = str(notation_number_string) + '   '  #adding notation number at beginning of every row
            for key in row.keys():  #generate plain board
                rowstr +=  row[key]
            print(rowstr)  
            notation_number_string -= 1 #inc notation number

    def notation(self): #visual notation
        notation_letter_string = '    '
        for i in self.notationletters:
            notation_letter_string += i + '  '
        print('\n'+notation_letter_string)

    def create_board(self): #create full visual board from rows made by create_row()
        Board.create_row(Board.coordobj)
        Board.notation(self)

        









 
    

current_game_notation = AlgebraicNotation(boardvar, notation_letter, notation_number)

board = Board(boardvar, notation_letter, notation_number)

board.create_board()