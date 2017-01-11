from flask import Flask, render_template, request

app = Flask(__name__)

class HangmanGame:
    MAX_FAILS = 5

    def __init__(self, word):
        self.word = ""
        self.word_so_far = []
        self.guessed_letters = []
        self.remaining_guesses = HangmanGame.MAX_FAILS

        self.setNewWord(word)

    def setNewWord(self, word):
        self.word = word.lower()
        self.word_so_far = list("_" * len(self.word))
        self.guessed_letters = []
        self.remaining_guesses = HangmanGame.MAX_FAILS

    def guessletter(self, letter):
        # TODO
        pass

    def wonGame(self):
        # TODO
        pass

    def lostGame(self):
        #TODO
        pass

    def getFormatWordSoFar(self):
        return " ".join(self.word_so_far)

    def getLettersGuessed(self):
        return ", ".join(self.guessed_letters)


my_game = HangmanGame("hangman")


@app.route('/newgame', methods=['GET', 'POST'])
def newgame_page():
    if my_game.wonGame() or my_game.lostGame():
        if request.method == 'GET':
            return render_template("makenewgame.html")
        else:
            newword = request.form.get('word')
            my_game.setNewWord(newword)
            return "A new game was made!"
    else:
        return "A game is in progress!"



@app.route('/',methods=['GET','POST'])
def index_page():
    if request.method=='POST':
        my_guess = request.form.get('guess')
        lowercase_guess = my_guess.lower()
        for letter in lowercase_guess:
            my_game.guessletter(letter)
    word_to_show = my_game.getFormatWordSoFar()
    letters_guessed = my_game.getLettersGuessed()
    failed_guesses = my_game.remaining_guesses
    real_word = my_game.word
    did_we_win = my_game.wonGame()
    did_we_lose = my_game.lostGame()

    return render_template('maingame.html',
                           hangman_word=word_to_show,
                           hangman_letters=letters_guessed,
                           hangman_step=failed_guesses,
                           hangman_real_word=real_word,
                           game_won=did_we_win,
                           game_lost=did_we_lose)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)
