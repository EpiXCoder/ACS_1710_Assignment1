
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'
    

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    return f'Today I saw {adjective} {noun} on my way to work. I have known {noun} for a few years but I did not know that he had gotten {adjective} in the past few weeks.'

@app.route('/multiply/<number1>/<number2>')
def multiply_numbers(number1, number2):
    if number1.isdigit() and number1.isdigit():
        total = int(number1)*int(number2)
        return f'{number1} times {number2} is {total}.'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    if n.isdigit():
        string = word
        for x in range(int(n)-1):
            string += ' ' + word
        return string
    else:
        return f'Invalid input. Please try again by entering a word and a number!'

@app.route('/dicegame')
def dice_game():
    random_roll = random.randint(1, 6)
    if random_roll == 6:
        return f'You rolled a {random_roll}. You won!'
    else: 
        return f'You rolled a {random_roll}. You lost!'


if __name__ == '__main__':
    app.run(debug=True)