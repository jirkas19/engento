'''
author = Jiří Sedlo
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]

prihlaseni = {"bob": "123", "ann": "pass123",
              "mike": "password123", "liz": "pass123"}
jmeno = input("username:")
heslo = input("password:")
odstavec = ""
statistika = {"titulek": 0, "velka_pismena": 0, "mala_pismena": 0,
              "suma": 0, "pocet_cisel": 0, "pocet_slov": 0}
delka_slov = {}
delka_slov_list = []

# ------------------------------------------------------------------------------

if jmeno in prihlaseni.keys():
    if prihlaseni[jmeno] == heslo:
        print("-" * 79)
        print(f"Welcome to the app, {jmeno}"
              "\nWe have 3 texts to be analyzed.")
        print("-" * 79)
        vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
        print("-" * 79)
        if vyber_textu.isnumeric():
            vyber_textu = int(vyber_textu)
            if vyber_textu in range(1, len(TEXTS) + 1):
                odstavec = TEXTS[vyber_textu - 1]
                oddel_slov = odstavec.split()
                cisty_lis = []
                for i in oddel_slov:
                    slovo = i.strip(",.")
                    cisty_lis.append(slovo)
                for i in cisty_lis:
                    if i.isnumeric():
                        statistika["pocet_cisel"] += 1
                        statistika["suma"] += int(i)
                    if i.islower():
                        statistika["mala_pismena"] += 1
                    if i != "":
                        if i[0].isupper():
                            statistika["titulek"] += 1
                            if i.isupper():
                                statistika["velka_pismena"] += 1
                    else:
                        cisty_lis.remove(i)
                statistika["pocet_slov"] = len(cisty_lis)
                for i in cisty_lis:
                    if len(i) not in delka_slov.keys():
                        delka_slov[len(i)] = 1
                    else:
                        delka_slov[len(i)] += 1

                print(f"There are {statistika['pocet_slov']} words in the selected text."
                      f"\nThere are {statistika['titulek']} titlecase words."
                      f"\nThere are {statistika['velka_pismena']} uppercase words."
                      f"\nThere are {statistika['mala_pismena']} lowercase words."
                      f"\nThere are {statistika['pocet_cisel']} numeric strings."
                      f"\nThe sum of all the numbers {statistika['suma']}")
                for i in delka_slov.items():
                    delka_slov_list.append(i)
                delka_slov_list.sort()
                print("-" * 79)
                print("LEN|     OCCURENCES     |NR.")
                print("-" * 79)
                for i in range(len(delka_slov_list)):
                    tisk = fr = "{:>4}".format(f"{delka_slov_list[i][0]}|") \
                                + "{:<20}".format((delka_slov_list[i][1]) * "*") \
                                + "{:<4}".format(f"|{delka_slov_list[i][1]}")
                    print(tisk)
            else:
                print("your chosen number is not between 1-3, terminating the program.. ")
        else:
            print("you didnt write number, terminating the program..")


else:
    print("unregistered user, terminating the program..")
    quit()
