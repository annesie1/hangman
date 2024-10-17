import random
def figure1():
    print(" 0 ")

def figure2():
    print(" 0 ")
    print(" | ")

def figure3():
    print(" 0 ")
    print(" | ")
    print(" | ")

def figure4():
    print(" 0 ")
    print(" | ")
    print(" | ")
    print("/  ")

def figure5():
    print(" 0 ")
    print(" | ")
    print(" | ")
    print("/ \\")

def figure6():
    print(" 0 ")
    print("\| ")
    print(" | ")
    print("/ \\")

def figure7():
    print(" 0 ")
    print("\|/")
    print(" | ")
    print("/ \\")

figure1()
figure2()
figure3()
figure4()
figure5()
figure6()
figure7()

plik_latwe = open("countries-latwe.txt", "r", encoding="utf-8")
plik_trudne = open("countries-trudne.txt", "r", encoding="utf-8")


def choose_word_latwe():
    latwe = plik_latwe.readlines()
    if input == latwe
return random.choice(latwe).lower()

def choose_word_trudne():
    trudne = plik_trudne.readlines()
    if input == trudne
return random.choice(trudne).lower()

def display_hangman():

def display_game_state(word, revealed_letters):
    game_state = ''.join(letter if letter in revealed_letters else '_' for letter in word)
    print("Stan gry:", game_state)

def main():
    word =         # Wybrane słowo
    revealed_letters = []

    print("Początkowy stan gry:")
    display_game_state(word, revealed_letters)

def play_game():
    print("Witaj w grze w odgadywanie słów!")
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = set()

    # Osłanianie liter
    while True:
        litera= input("Podaj literę: (lub 'exit' aby zakończyć): ").lower()
        if litera == 'exit':
            print("Dziękujemy za grę!")
            break
        elif litera in word and litera not in revealed_letters:
            revealed_letters.append(litera)
            print(f"Litera '{litera}' odsłonięta!")
        elif litera in revealed_letters:
            print(f"Litera '{litera}' już została odsłonięta!")
        else:
            print(f"Litera '{litera}' nie występuje w słowie.")

        display_game_state(word, revealed_letters)


# Uruchom grę
if __name__ == "__main__":
    play_game()




input("Wprowadz litere:")