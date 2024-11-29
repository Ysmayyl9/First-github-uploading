import tkinter as tk
import random

class Hagman :
    def __init__(self, root) :
        
        self.root = root
        self.words = ['elon', 'fettullah', 'taip', 'galileo', 'faraday', 'larry']
        self.attempt = 6
        self.has_crt = ''
        self.len_ = []
    
    def opening(self) :
        
        self.canvas = tk.Canvas(root, width = 900, height = 900)
        self.canvas.pack()
        self.canvas.create_line(380, 220, 380, 480, fill = 'black', width = 7)
        self.canvas.create_line(440, 220, 380, 270, fill = 'black', width = 5)
        self.canvas.create_line(380, 220, 530, 220, fill = 'black', width = 7)
        self.canvas.create_line(500, 220, 500, 260, fill = 'black', width = 6)

        self.open_button = tk.Button(root, text = 'Begin', command = self.begin_)
        self.button_window = self.canvas.create_window(450, 575, window = self.open_button)

    def begin_(self) :

        self.secret_word = random.choice(self.words)

        self.clue_()

        self.open_button.destroy()

        print(self.secret_word)

        self.index_word = ['']
        for i in range(len(self.secret_word)) :
            self.index_word.append('_  ')
        self.res_index = ''.join(self.index_word)
        self.label = tk.Label(root, text = self.res_index, font = ('Arial', 24))
        self.label_window = self.canvas.create_window(450, 160, window = self.label)

        self.entry = tk.Entry(root)
        self.entry_window = self.canvas.create_window(450, 525, window = self.entry)
        
        self.send_button = tk.Button(root, text = 'Send', command = self.send_)
        self.button_window = self.canvas.create_window(450, 575, window = self.send_button)
        
        self.word_box = self.canvas.create_rectangle(0, 200, 3000, 130, fill = '', outline = 'gray')
        
        self.reset_button = tk.Button(root, text = 'Reset', command = self.reset_)
        self.reset_window = self.canvas.create_window(40, 40, window = self.reset_button)

    def send_(self) : 
        self.user_in = self.entry.get().lower()

        self.len_.clear()

        if self.user_in not in self.has_crt :
            self.has_crt += self.user_in

        self.sum = []
        for crt in self.secret_word :
            if crt in self.has_crt :
                self.sum.append(crt + '  ')
                self.len_.append(crt)
            else :
                self.sum.append('_  ')
                
        self.label.config(text = ''.join(self.sum))

        self.error_message()

        self.game_status_()
        
    def error_message(self) :

        if len(self.user_in) > 1 :
            self.error_label = tk.Label(root, text = 'You can write only one character', fg = 'red')
            self.error_label_window = self.canvas.create_window(450, 620, window = self.error_label)
        self.entry.delete(0, tk.END)
        
    def reset_(self) :
        self.index_word.clear()
        self.res_index = ''
        self.label.config(text = '')
        
        self.has_crt = ''
        self.sum = []

        self.info_label.config(text = '')

        self.len_.clear()

        if self.attempt == 0  :
            self.canvas.delete(self.head)
            self.canvas.delete(self.body)
            self.canvas.delete(self.left_hand)
            self.canvas.delete(self.right_hand)
            self.canvas.delete(self.right_neieve)
            self.canvas.delete(self.left_neieve)
        elif self.attempt == 1 :
            self.canvas.delete(self.head)
            self.canvas.delete(self.body)
            self.canvas.delete(self.left_hand)
            self.canvas.delete(self.right_hand)
            self.canvas.delete(self.left_neieve)
        elif self.attempt == 2 :
            self.canvas.delete(self.head)
            self.canvas.delete(self.body)
            self.canvas.delete(self.left_hand)
            self.canvas.delete(self.right_hand)
        elif self.attempt == 3 :
            self.canvas.delete(self.head)
            self.canvas.delete(self.body)
            self.canvas.delete(self.right_hand)
        elif self.attempt == 4 :
            self.canvas.delete(self.head)
            self.canvas.delete(self.body)
        elif self.attempt == 5 :
            self.canvas.delete(self.head)

        if self.res_game == False :
            self.victory_label.config(text = '')
            not self.res_game

        if self.attempt < 1 :
            self.lose_label.config(text = '')
            
        if self.attempt < 6 :
            self.attempt = 6
        print(self.attempt)
        self.clue_()

        self.begin_()

    def clue_(self) :

        self.info_label = tk.Label(root, text = '', font = ('Arial', 14), width = 50)
        self.canvas.create_window(450, 60, window = self.info_label)

        if self.secret_word == 'elon' :
            self.info_label.config(text = 'He is ingineer and billioner')
        
        if self.secret_word == 'fettullah' :
            self.info_label.config( text = 'He is was boss of FETO')
        
        if self.secret_word == 'taip' :
            self.info_label.config(text = 'He is politicant')

        if self.secret_word == 'larry' :
            self.info_label.config(text = 'He is Oracle of bulider')
        
        if self.secret_word == 'galileo' :
            self.info_label.config(text = 'He is physyc of father')

        if self.secret_word == 'faraday' :
            self.info_label.config(text = 'He is finded the magnetic compass')

    def game_status_(self) :

        self.res_game = True
    
        if len(self.len_) == len(self.secret_word) :
            self.victory_label = tk.Label(root, text = "You win", font = ('Arial', 30), fg = 'red')
            self.res_game = not self.res_game
            self.canvas.create_window(450, 340, window = self.victory_label)
            self.reset_button.config(bg = 'yellow', fg = 'red')
            self.send_button.destroy()
            self.entry.destroy()

        if self.user_in not in self.secret_word :
            self.attempt -= 1

        print(self.attempt)
        
        if self.attempt == 6 : 
            pass

        elif self.attempt == 5 :
            self.head = self.canvas.create_oval(480, 250, 520, 295, fill = 'black', outline = '')

        elif self.attempt == 4 :
            self.body = self.canvas.create_line(500, 295, 500, 385, fill = 'black', width = 10)

        elif self.attempt == 3 :
            self.right_hand = self.canvas.create_line(500, 300, 535, 350, fill = 'black', width = 10) 

        elif self.attempt == 2 : 
            self.left_hand = self.canvas.create_line(500, 300, 465, 350, fill = 'black', width = 10)

        elif self.attempt == 1 : 
            self.left_neieve = self.canvas.create_line(500, 380, 470, 420, fill = 'black', width = 10)

        elif self.attempt == 0 : 
            self.right_neieve = self.canvas.create_line(500, 380, 530, 420, fill = 'black', width = 10)
            self.send_button.destroy()
            self.entry.destroy()
            self.lose_label = tk.Label(root, text = "Dead", font = ('Arial', 30), fg = 'red')
            self.canvas.create_window(450, 340, window = self.lose_label)
            self.reset_button.config(bg = 'yellow', fg = 'red')

        elif self.attempt == 4 :
                self.papyon = self.canvas.create_oval(500, 310, 500, 310, outline = 'red', width = 10)

root = tk.Tk()
root.title('Hagman')
game = Hagman(root)
game.opening()

root.mainloop()