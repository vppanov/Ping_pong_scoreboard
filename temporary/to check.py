from tkinter import *

#screen dimensions
winsize = 500 
gridwidth = 2 
symbol = winsize/12 
symsize = 0.5
#colors of players
player_x = 'black'
player_o = 'gray'
#screen colors
screencolor = 'red'
gridcolor = 'black'
bg_color = 'white'


player_one = 1 
sizeof_cell = winsize / 3

screen_title = 0
turn_x = 1
turn_o = 2
gameover = 3
score_x = 0
score_o = 0
zero = 0
X = 1
O = 2


class Game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.canvas = Canvas(
            height=winsize, width=winsize,
            bg=bg_color)
        self.canvas.pack()
        self.bind('<x>', self.exit)
        self.canvas.bind('<Button-1>', self.mouse)
        self.gamestate = screen_title
        self.title_screen()
        self.board = [
            [zero, zero, zero],
            [zero, zero, zero],
            [zero, zero, zero]]
#ADD HIGH SCORE    
    def display_score(score):
        score = 0
        if score(grid):
            score += 1  





#creating title screen 
    def title_screen(self):

        self.canvas.delete('all') 
        self.canvas.create_rectangle(
            0, 0,
            winsize, winsize,
            fill='black',
            outline='black')

        self.canvas.create_rectangle(
            int(winsize/15), int(winsize/15),
            int(winsize*14/15), int(winsize*14/15),
            width=int(winsize/20),
            outline='black')    

        self.canvas.create_rectangle(
            int(winsize/10), int(winsize/10),
            int(winsize*9/10), int(winsize*9/10),
            fill='black',
            outline='black')

#adding names, R number, intructions
        self.canvas.create_text(
            winsize/2,
            winsize/3,
            text='TIC TAC TOE', fill='white',
            font=('Calibri', int(-winsize/10), 'bold'))

        self.canvas.create_text(
            winsize/2,
            winsize/2,
            text='Game By: Yanely Ramos (R11529473)', fill='white',
            font=('Arial', int(-winsize/25)))

        self.canvas.create_text(
            winsize/2,
            winsize/1.8,
            text='& Maria Tan de Castro (R11512696)', fill='white',
            font=('Arial', int(-winsize/25)))

        self.canvas.create_text(
            winsize/2,
            winsize/1.3,
            text='Directions: Players take turn putting marks on empty' + '\n' + 'squares first player to get 3 in a row is a winner.' + "\n" + 'If all 9 squares are full and there is no winner, it is a draw.', fill='white',
            font=('Times New Roman', int(-winsize/35)))

        self.canvas.create_text(
            int(winsize/2),
            int(winsize/2.5),
            text='[Click here to play]', fill='white',
            font=('Arial', int(-winsize/25)))

#clicking of the game using the mouse
    def mouse(self, event):

        x = self.pixel_grid(event.x)
        y = self.pixel_grid(event.y)

        if self.gamestate == screen_title:
            self.new_gameboard()
            self.gamestate = player_one

        elif (self.gamestate == turn_x and
                self.board[y][x] == zero):
            self.next_shift(X, x, y)

            if self.winner(X):
                self.gamestate = gameover
                self.gameover_title('X WINS')

            elif self.game_draw():
                self.gamestate = gameover
                self.gameover_title('DRAW')

            else:
                self.gamestate = turn_o

        elif (self.gamestate == turn_o and
                self.board[y][x] == zero):
            self.next_shift(O, x, y)

            if self.winner(O):
                self.gamestate = gameover
                self.gameover_title('O WINS')

            elif self.game_draw():
                self.gamestate = gameover
                self.gameover_title('DRAW')

            else:
                self.gamestate = turn_x

        elif self.gamestate == gameover:
            self.new_gameboard()
            self.gamestate = player_one

 #starting new game  
    def new_gameboard(self):

        self.canvas.delete('all')
        self.board = [
            [zero, zero, zero],
            [zero, zero, zero],
            [zero, zero, zero]]


        for n in range(1, 3):

            self.canvas.create_line(
                sizeof_cell*n, 0,
                sizeof_cell*n, winsize,
                width=gridwidth, fill=gridcolor)

            self.canvas.create_line(
                0, sizeof_cell*n,
                winsize, sizeof_cell*n,
                width=gridwidth, fill=gridcolor)

#what pops up when the game ends
    def gameover_title(self, outcome):

        self.canvas.delete('all')

        if outcome == 'X WINS':
            wintext = 'X wins'
            wincolor = player_x

        elif outcome == 'O WINS':
            wintext = 'O wins'
            wincolor = player_o

        elif outcome == 'DRAW':
            wintext = 'Draw'
            wincolor = screencolor

        self.canvas.create_rectangle(
            0, 0,
            winsize, winsize,
            fill=wincolor, outline='')

        self.canvas.create_text(
            int(winsize/2), int(winsize/2),
            text=wintext, fill='white',
            font=('Calibri', int(-winsize/6), 'bold'))

        self.canvas.create_text(
                int(winsize/2), int(winsize/1.65),
                text='[click to play again]', fill='white',
                font=('Arial', int(-winsize/25)))

#next players turn  
    def next_shift(self, player, grid_x, grid_y):

        if player == X:
            self.drawx(grid_x, grid_y)
            self.board[grid_y][grid_x] = X

        elif player == O:
            self.drawo(grid_x, grid_y)
            self.board[grid_y][grid_x] = O

#creating X player
    def drawx(self, grid_x, grid_y):

        x = self.grid_pixel(grid_x)
        y = self.grid_pixel(grid_y)
        delta = sizeof_cell/1.5*symsize

        self.canvas.create_line(
            x-delta, y-delta,
            x+delta, y+delta,
            width=symbol, fill='red')

        self.canvas.create_line(
            x+delta, y-delta,
            x-delta, y+delta,
            width=symbol, fill='red')

#creating O player
    def drawo(self, grid_x, grid_y):

        x = self.grid_pixel(grid_x)
        y = self.grid_pixel(grid_y)
        delta = sizeof_cell/1.5*symsize

        self.canvas.create_oval(
            x-delta, y-delta,
            x+delta, y+delta,
            width=symbol, outline='black')
#how to win
    def winner(self, symbol):
        for y in range(3):
            if self.board[y] == [symbol, symbol, symbol]:
                return True
        for x in range(3):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] == symbol:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True
        return False
#if 9 squares fill up, go to draw screen
    def game_draw(self):
        for row in self.board:
            if zero in row:
                return False   
        return True

    def grid_pixel(self, grid_coord):

        pixel_coord = grid_coord * sizeof_cell + sizeof_cell / 2
        return pixel_coord

    def pixel_grid(self, pixel_coord):

        if pixel_coord >= winsize:
            pixel_coord = winsize - 1    

        grid_coord = int(pixel_coord / sizeof_cell)
        return grid_coord

    def exit(self, event):
        self.destroy()

def main():
    root = Game()
    root.mainloop()
    root.title('TIC TAC TOE')