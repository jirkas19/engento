import random

print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------

Příklad hry s číslem 2017:

Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------""")


def cislo():
    y = random.randrange(1, 9)
    uni = [y]  # první číslo bez nuly
    while len(uni) < 4:  # zbylá tři čísla
        y = random.randrange(9)
        if y not in uni:  # ověření duplicity cifer
            uni.append(y)
    return uni


def uzivatel():
    vstup = input()
    return vstup


def overeni_cisla(vstup: str) -> object:
    if vstup.isnumeric():
        return True
    else:
        print("your input is not numeric")
        return False


def overeni_poctu_cislic(vstup: str) -> object:
    if len(vstup) == 4:
        return True
    else:
        print("you didnt write 4 digit number")
        return False


def overeni_duplicity(vstup: str) -> object:
    mnozina = []
    for i in vstup:
        if i not in mnozina:
            mnozina.append(i)
        else:
            print("you have duplicite digits in your number")
            return False
    else:
        return True


def zacatek_cisla(vstup: str) -> object:
    if int(vstup[0]) == 0:
        print("first digit in your number is 0")
        return False
    else:
        return True


def uhodnute_cislo(vstup, hadane_cislo):
    kravicky = 0
    bejci = 0
    for i, j in enumerate(hadane_cislo):
        if str(j) in str(vstup):  # pokud je číslo zadané uživatelem v hádaném čísle
            if int(j) == int(vstup[i]):  # pokud je poloha čísla zadaného čísla na stejném místě jako u hádaného čísla
                bejci += 1
            else:
                kravicky += 1
    if bejci == 4:
        print("Correct, you've guessed the right number")  # kompletní výhra
        return 1
    else:
        print(f"cows={kravicky},bulls={bejci}")  # výpis výsledků kola
        return 0


def hadej_hadej_hadaci(hadane_cislo: list) -> object:
    i = 0
    while i == 0:
        vstup = uzivatel()
        a = overeni_cisla(vstup)
        b = overeni_poctu_cislic(vstup)
        c = overeni_duplicity(vstup)
        if a and b and c:  # ověření spravnosti vstupu
            d = zacatek_cisla(vstup)
            if d:
                i = uhodnute_cislo(vstup, hadane_cislo)
        else:
            i = 0


def main():
    hadane_cislo = cislo()
    hadej_hadej_hadaci(hadane_cislo)


if __name__ == "__main__":
    main()
