import random
from turtle import Screen
import turtle
import pandas
from tkinter import messagebox
import sys

screen = Screen()
screen.title('African Countries')
screen.setup(height=720, width=720)


colors = ['blue', 'black', 'brown', 'purple', 'orange', 'green', 'red']
random.shuffle(colors)

image = 'africa_map .gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('african_countries.csv')
countries = data.title.to_list()
messagebox.showinfo(title='Info', message='WELCOME TO AFRICAN STATES GAME.\n  \n Type in exit to quit game in text '
                                          'entry.\n \nPress OK to continue to game.')
known_countries = []
while len(known_countries) < 58:

    user_guess = screen.textinput(title=f'{len(known_countries)}/58'
                                        f' countries guessed.', prompt='Guess a country.\n(Use full, official country '
                                                                       'name.)').title()
    if user_guess in countries:

        if user_guess in known_countries:
            messagebox.showinfo(title=f'{user_guess}', message='Country already guessed')
        else:
            known_countries.append(user_guess)
            the_turtle = turtle.Turtle()
            the_turtle.hideturtle()
            the_turtle.penup()
            country = data[data.title == user_guess]
            the_turtle.goto(int(country.x), int(country.y))
            the_turtle.color(random.choice(colors))
            the_turtle.write(country.title.item(), font=('Courier', 10, 'bold'))
    elif user_guess == 'Exit':

        states_to_learn = [countrie for countrie in countries if countrie not in known_countries]
        unknown_states = pandas.DataFrame(states_to_learn).to_csv('unknown_countries.csv')
        sys.exit()

    elif len(user_guess.strip()) == 0:
        messagebox.showerror(title='Empty field', message='Guess a country')

    elif user_guess not in countries:
        messagebox.showinfo(title=f'Incorrect', message='Incorrect Spelling or not an African country.\nTry Again')

screen.exitonclick()
