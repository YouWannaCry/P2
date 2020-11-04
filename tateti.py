#############################################################################
##### En game.py se puede jugar a otro tateti que hice mientras pensaba #####
#############################################################################
import re
import inspect


class TaTeTi():

    def __init__(self):
        self.board = {"1.1": "1.1", "1.2": "1.2", "1.3": "1.3",
                      "2.1": "2.1", "2.2": "2.2", "2.3": "2.3",
                      "3.1": "3.1", "3.2": "3.2", "3.3": "3.3"}
        self.valid = ["1.1", "1.2", "1.3",
                      "2.1", "2.2", "2.3",
                      "3.1", "3.2", "3.3"]
        self.piece = "x"       

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            Smile = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
        if len(self.valid) == 0:
            Smile = 'Ninguno'
        return Smile

    def win(self):
        GAMEBOard = self.board_to_arr()
        YWCInput = re.compile(" x|o ")
        bool = False
        #Pense un metodo diferente, uno que iba haciendo if
        #entre las 8 posibilidades de ganar(como esta en game.py), 
        #pero no pude hacerlo correr con regex asi que
        #me decante mas por esta
        #Use bastante REGEX en sistemas operativos y para
        #algunas cosas se me hizo util, asi que ahora le doy uso xD
        if (GAMEBOard[0] == GAMEBOard[1] == GAMEBOard[2] and\
                YWCInput.search(GAMEBOard[0])) or\
           (GAMEBOard[3] == GAMEBOard[4] == GAMEBOard[5] and\
                YWCInput.search(GAMEBOard[3])) or\
           (GAMEBOard[6] == GAMEBOard[7] == GAMEBOard[8] and\
                YWCInput.search(GAMEBOard[6])) or\
           (GAMEBOard[0] == GAMEBOard[3] == GAMEBOard[6] and\
                YWCInput.search(GAMEBOard[0])) or\
           (GAMEBOard[1] == GAMEBOard[4] == GAMEBOard[7] and\
                YWCInput.search(GAMEBOard[1])) or\
           (GAMEBOard[2] == GAMEBOard[5] == GAMEBOard[8] and\
                YWCInput.search(GAMEBOard[2])) or\
           (GAMEBOard[0] == GAMEBOard[4] == GAMEBOard[8] and\
                YWCInput.search(GAMEBOard[0])) or\
           (GAMEBOard[2] == GAMEBOard[4] == GAMEBOard[6] and\
                YWCInput.search(GAMEBOard[2])):
            bool = True   
        return bool

    def input_position(self):
        patron = re.compile("^[123]\.[123]$")
        while (inpt := patron.search(input("Ingresar una posición: ")))\
                is None:
            continue
        self.valid = [self.valid[i] for i in range(len(self.valid))
                      if self.valid[i] != inpt.group()]
        inpt = inpt.group()
        return inpt

    def __str__(self):
        string = ""
        GAMEBOard = self.board_to_arr()
        for i in range(len(GAMEBOard)):
            string += GAMEBOard[i] + "|"\
                    if (i+1) % 3 != 0 else GAMEBOard[i]
            if (i+1) % 3 == 0 and (i+1) != 9:
                string += "\n"
                string += "---+---+---"
                string += "\n"
        return string

    def board_to_arr(self):
        return [self.board[key] for key in self.board]

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, piece):
        self._piece = piece

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, valid):
        self._valid = valid

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board


if __name__ == '__main__':
    game = TaTeTi()

    print('Ganó ' + game.game())