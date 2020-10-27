from microbit import *
import speech
import random

lengteWoordArray = 3

onderwerp = ["Joost", "Samuel", "Lukas"]
werkwoord = ["Playing games", "Food", "Drinks"]
rest = ["hard", "at school", "coffee"]

def sayTheWords1(word):
    print(word)
    speech.say(word, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)

def sayTheWords2():
    willekeurigGetal = random.randint(0, lengteWoordArray - 1)
    display.show(willekeurigGetal)
    sayTheWords1(onderwerp[willekeurigGetal])
    sayTheWords1(werkwoord[willekeurigGetal])
    sayTheWords1(rest[willekeurigGetal])

smile = Image('09090:'
              '09090:'
              '00000:'
              '90009:'
              '09990:')


while True:
    if button_a.is_pressed():
        display.show("Hello Human")
        sayTheWords1("Hello comrad")
    elif button_b.is_pressed():
        display.show(smile)
        sayTheWords2(")
    elif display.read_light_level() < 40:
        sayTheWords1("Don't cover my eyes!")
    else:
        display.show(smile)
