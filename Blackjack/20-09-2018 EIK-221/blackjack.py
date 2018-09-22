import random

print("Tere!")

# name = input("Mis su nimi on?")
def game(last_games=[]):
    kasutaja_punktid = 0
    arvuti_punktid = random.randint(0, 21)


    while True:
        sisend = input("Kas tahad võtta uue kaardi? (Y/N)")

        if sisend in ("Y", "y"):
            print("Võtsid kaardi!")
            kasutaja_punktid += random.randint(2, 10)
        elif sisend in ("N", "n"):
            print("Olgu nii.")
            break
        else:
            print("Ma ei saanud aru.")

        print(f"Sul on {kasutaja_punktid} punkti.")

    if kasutaja_punktid > 21 or kasutaja_punktid < arvuti_punktid:
        print("Sa oled kaotanud!")
        last_games.append(False)
    elif kasutaja_punktid > arvuti_punktid:
        print("Sa oled võitnud!")
        last_games.append(True)
    else:
        print("Jäid viiki!")
        last_games.append(None)

    print(f"Sul oli {kasutaja_punktid} punkti, arvutil oli {arvuti_punktid} punkti.")

    if last_games:
        print(f"Võite: {last_games.count(True)}, kaotusi: {last_games.count(False)}, viike: {last_games.count(None)}")
    new_game = input("Uus mäng?")

    if new_game == "Y":
        game(last_games)

game()
