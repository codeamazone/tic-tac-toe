import random


class TicTacToe:

    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.coordinates = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3],
                            [3, 1], [3, 2], [3, 3]]
        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.column1 = []
        self.column2 = []
        self.column3 = []
        self.diagonal1 = []
        self.diagonal2 = []
        self.winner = 'no'
        self.state = 'X'

    def create_field(self):
        print('---------')
        for i in self.field:
            print(f'| {i[0]} {i[1]} {i[2]} |')
        print('---------')

    def rows_of_three(self):
        self.row1 = self.field[0]
        self.row2 = self.field[1]
        self.row3 = self.field[2]
        self.column1 = [row[0] for row in self.field]
        self.column2 = [row[1] for row in self.field]
        self.column3 = [row[2] for row in self.field]
        self.diagonal1 = [self.field[0][0], self.field[1][1], self.field[2][2]]
        self.diagonal2 = [self.field[0][2], self.field[1][1], self.field[2][0]]

    def set_state(self):
        if self.state == 'X':
            self.state = 'O'
        elif self.state == 'O':
            self.state = 'X'

    def define_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def check_win(self):
        self.rows_of_three()
        if self.row1[1:] == self.row1[:-1] and ' ' not in self.row1:
            print(f"{self.row1[0]} wins")
            self.winner = 'yes'
        elif self.row2[1:] == self.row2[:-1] and ' ' not in self.row2:
            print(f"{self.row2[0]} wins")
            self.winner = 'yes'
        elif self.row3[1:] == self.row3[:-1] and ' ' not in self.row3:
            print(f"{self.row3[0]} wins")
            self.winner = 'yes'
        elif self.column1[1:] == self.column1[:-1] and ' ' not in self.column1:
            print(f"{self.column1[0]} wins")
            self.winner = 'yes'
        elif self.column2[1:] == self.column2[:-1] and ' ' not in self.column2:
            print(f"{self.column2[0]} wins")
            self.winner = 'yes'
        elif self.column3[1:] == self.column3[:-1] and ' ' not in self.column3:
            print(f"{self.column3[0]} wins")
            self.winner = 'yes'
        elif self.diagonal1[1:] == self.diagonal1[
                                   :-1] and ' ' not in self.diagonal1:
            print(f"{self.diagonal1[0]} wins")
            self.winner = 'yes'
        elif self.diagonal2[1:] == self.diagonal2[
                                   :-1] and ' ' not in self.diagonal2:
            print(f"{self.diagonal2[0]} wins")
            self.winner = 'yes'
        if self.winner == 'yes':
            return True

    def check_draw(self):
        if self.winner != 'yes':
            cells = [i for row in self.field for i in row]
            if ' ' not in cells:  # no empty cells left
                print('Draw')
                return True

    def play_game(self):
        self.create_field()
        while True:
            self.player1.move()
            self.set_state()
            self.create_field()
            # self.check_win()
            if self.check_win():
                break
            elif self.check_draw():
                break
            self.player2.move()
            self.set_state()
            self.create_field()
            # self.check_win()
            if self.check_win():
                break
            elif self.check_draw():
                break

    def start(self, *choices):
        if choices[1] == 'user':
            user = Person(self)
            if choices[2] == 'user':
                self.define_players(user, user)
            elif choices[2] == 'easy':
                computer_easy = ComputerEasy(self)
                self.define_players(user, computer_easy)
            elif choices[2] == 'medium':
                computer_medium = ComputerMedium(self)
                self.define_players(user, computer_medium)
        elif choices[1] == 'easy':
            computer_easy = ComputerEasy(self)
            if choices[2] == 'user':
                user = Person(self)
                self.define_players(computer_easy, user)
            elif choices[2] == 'easy':
                self.define_players(computer_easy, computer_easy)
            elif choices[2] == 'medium':
                computer_medium = ComputerMedium(self)
                self.define_players(computer_easy, computer_medium)
        elif choices[1] == 'medium':
            computer_medium = ComputerMedium(self)
            if choices[2] == 'user':
                user = Person(self)
                self.define_players(computer_medium, user)
            elif choices[2] == 'easy':
                computer_easy = ComputerEasy(self)
                self.define_players(computer_medium, computer_easy)
            elif choices[2] == 'medium':
                self.define_players(computer_medium, computer_medium)
        else:
            print('Bad parameters!')
        self.play_game()


class Player:

    def __init__(self, ttt):
        self.ttt = ttt


class Person(Player):

    def move(self):
        while True:
            user_coordinates = input('Enter the coordinates: ').split()
            string_check = [x for x in user_coordinates if not x.isdigit()]
            digit_check = [x for x in user_coordinates if x.isdigit()]
            if len(string_check) > 0 or len(digit_check) != 2:
                print('You should enter numbers!')
                continue
            elif len(digit_check) == 2:
                if int(user_coordinates[0]) not in range(1, 4) or int(
                        user_coordinates[1]) not in range(1, 4):
                    print('Coordinates should be from 1 to 3!')
                    continue
                else:
                    user_coordinates = [int(x) for x in user_coordinates]
                    if self.ttt.field[user_coordinates[0] - 1][
                            user_coordinates[1] - 1] != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        self.ttt.field[user_coordinates[0] - 1][
                            user_coordinates[1] - 1] = self.ttt.state
                        self.ttt.coordinates.remove(user_coordinates)
                        break


class Computer(Player):

    def __init__(self, ttt):
        super().__init__(ttt)
        self.opponent = None

    def define_opponent(self):
        if self.ttt.state == 'X':
            self.opponent = 'O'
        elif self.ttt.state == 'O':
            self.opponent = 'X'

    def basic_move(self):
        computer_coordinates = random.choice(self.ttt.coordinates)
        self.ttt.field[computer_coordinates[0] - 1][
            computer_coordinates[1] - 1] = self.ttt.state
        self.ttt.coordinates.remove(computer_coordinates)


class ComputerEasy(Computer):
    def move(self):
        print('Making move level "easy"')
        self.basic_move()


class ComputerMedium(Computer):

    def move(self):
        print('Making move level "medium"')
        self.define_opponent()
        if ((self.ttt.row1.count(self.ttt.state) == 2 or self.ttt.row1.count(
                self.opponent) == 2)) and ' ' in self.ttt.row1:
            self.ttt.coordinates.remove([1, self.ttt.row1.index(' ') + 1])
            self.ttt.field[0][self.ttt.row1.index(' ')] = self.ttt.state
        elif ((self.ttt.row2.count(self.ttt.state) == 2 or self.ttt.row2.count(
                self.opponent) == 2)) and ' ' in self.ttt.row2:
            self.ttt.coordinates.remove([2, self.ttt.row2.index(' ') + 1])
            self.ttt.field[1][self.ttt.row2.index(' ')] = self.ttt.state
        elif ((self.ttt.row3.count(self.ttt.state) == 2 or self.ttt.row3.count(
                self.opponent) == 2)) and ' ' in self.ttt.row3:
            self.ttt.coordinates.remove([3, self.ttt.row3.index(' ') + 1])
            self.ttt.field[2][self.ttt.row3.index(' ')] = self.ttt.state
        elif ((self.ttt.column1.count(self.ttt.state) == 2 or self.ttt.column1.count(
                self.opponent) == 2)) and ' ' in self.ttt.column1:
            self.ttt.coordinates.remove([self.ttt.column1.index(' ') + 1, 1])
            self.ttt.field[self.ttt.column1.index(' ')][0] = self.ttt.state
        elif ((self.ttt.column2.count(self.ttt.state) == 2 or self.ttt.column2.count(
                self.opponent) == 2)) and ' ' in self.ttt.column2:
            self.ttt.coordinates.remove([self.ttt.column2.index(' ') + 1, 2])
            self.ttt.field[self.ttt.column2.index(' ')][1] = self.ttt.state
        elif ((self.ttt.column3.count(self.ttt.state) == 2 or self.ttt.column3.count(
                self.opponent) == 2)) and ' ' in self.ttt.column3:
            self.ttt.coordinates.remove([self.ttt.column3.index(' ') + 1, 3])
            self.ttt.field[self.ttt.column3.index(' ')][2] = self.ttt.state
        elif ((self.ttt.diagonal1.count(self.ttt.state) == 2 or self.ttt.diagonal1.count(
                self.opponent) == 2)) and ' ' in self.ttt.diagonal1:
            self.ttt.coordinates.remove([self.ttt.diagonal1.index(' ') + 1, self.ttt.diagonal1.index(' ') + 1])
            self.ttt.field[self.ttt.diagonal1.index(' ')][
                self.ttt.diagonal1.index(' ')] = self.ttt.state
        elif ((self.ttt.diagonal2.count(self.ttt.state) == 2 or self.ttt.diagonal2.count(
                self.opponent) == 2)) and ' ' in self.ttt.diagonal2:
            if self.ttt.diagonal2.index(' ') == 0:
                self.ttt.coordinates.remove([1, 3])
                self.ttt.field[0][2] = self.ttt.state
            elif self.ttt.diagonal2.index(' ') == 1:
                self.ttt.coordinates.remove([2, 2])
                self.ttt.field[1][1] = self.ttt.state
            else:
                self.ttt.coordinates.remove([3, 1])
                self.ttt.field[2][0] = self.ttt.state
        else:
            self.basic_move()


while True:
    game = TicTacToe()
    user_input = input('Input command: ').split()
    if len(user_input) > 0:
        if user_input[0] == 'exit':
            break
        elif len(user_input) == 3 and user_input[0] == 'start':
            game.start(*user_input)
        else:
            print('Bad parameters!')
    else:
        print('Bad parameters!')
