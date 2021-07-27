import random
import time
import sys

# ----------- selection es la parte del código en el que la computadora elige entre piedra, papel o tijera y a su vez te imprime el dialogo que en la vida real las personas tienen cuando juegan este juego --------------------------------------

def selection():
    global comp_choice
    comp_choice = random.choice(["Piedra", "Papel", "Tijera"])
    time.sleep(0.5)
    print("Piedra")
    time.sleep(0.5)
    print("Papel")
    time.sleep(0.5)
    print("o Tijera")
    time.sleep(0.5)
    print("YA!")
    time.sleep(0.5)
    print("(La compu eligió " + comp_choice + ")")

# ---------- Todas estas funciones son para indicar que hacer si la pc selecciona una u otra palabra ---------------------

def comp_pie():
    global comp_choice
    global user_choice
    if comp_choice == "Piedra" and user_choice.capitalize() == "Piedra":
        print("Empatamos! Había elegido " + comp_choice)
        game()

    if comp_choice == "Piedra" and user_choice.capitalize() == "Papel":
        print("Me ganaste! Había elegido " + comp_choice)
        time.sleep(1)
        print("Queres volver a jugar? (Y) o (N)")
        replay = input()
        if replay.upper() == "Y":
            game()
        elif replay.upper() == "N":
            exit_game()

    if comp_choice == "Piedra" and user_choice.capitalize() == "Tijera":
        print("Gané, había elegido " + comp_choice)
        print("Queres volver a jugar? (Y) o (N)")
        replay = input()
        if replay.upper() == "Y":
            game()
        elif replay.upper() == "N":
            exit_game()
        
def comp_pap():
    global comp_choice
    global user_choice
    if comp_choice == "Papel" and user_choice.capitalize() == "Papel":
            print("Empatamos! Había elegido " + comp_choice)
            game()

    if comp_choice == "Papel" and user_choice.capitalize() == "Tijera":
        print("Me ganaste! Había elegido " + comp_choice)
        time.sleep(1)
        print("Queres volver a jugar? (Y) o (N)")
        replay = input()
        if replay.upper() == "Y":
            game()
        elif replay.upper() == "N":
            exit_game()

    if comp_choice == "Papel" and user_choice.capitalize() == "Piedra":
        print("Gané, había elegido " + comp_choice)
        print("Queres volver a jugar? (Y) o (N)")
        replay = input()
        if replay.upper() == "Y":
            game()
        elif replay.upper() == "N":
            exit_game()


def comp_tij():
    global comp_choice
    global user_choice
    if comp_choice == "Tijera" and user_choice.capitalize() == "Tijera":
        print("Empatamos! Había elegido " + comp_choice)
        game()

    if comp_choice == "Tijera" and user_choice.capitalize() == "Piedra":
        print("Me ganaste! Había elegido " + comp_choice)
        time.sleep(1)
        print("Queres volver a jugar? (Y) o (N)")
        replay = input()
        if replay.upper() == "Y":
            game()
        elif replay.upper() == "N":
            exit_game()

    if comp_choice == "Tijera" and user_choice.capitalize() == "Papel":
        print("Gané, había elegido " + comp_choice)
        print("Queres volver a jugar? (Y) o (N)")
        replay = input()
        if replay.upper() == "Y":
            game()
        elif replay.upper() == "N":
            exit_game()

# ---------------------------------------- exit es para el if N ----------------------------------------------------------

def exit_game():
    global name
    print("Bueno " + name.capitalize() + ", Adios!")
    sys.exit()

# ---------------------------------------- game es el juego per se -------------------------------------------------------

def game():
    global comp_choice
    global user_choice
    selection()
    user_choice = input()
    if comp_choice == "Piedra":
        comp_pie()
    if comp_choice == "Papel":
        comp_pap()
    if comp_choice == "Tijera":
        comp_tij()

# --------------------------------------- a partir de aca se ejecuta -----------------------------------------------------

comp_choice = None
user_choice = None
print("Hola! Como te llamas?")
name = input()
print("Hola " + name.capitalize() + "! Queres jugar al Piedra, Papel o Tijera?  (Y) o (N)")
play = input()
if play.upper() == "Y":
    print("Bueno, entonces preparate!")
    game()

elif play.upper() == "N":
    print("Bueno " + name.capitalize() + ", Adios!")
