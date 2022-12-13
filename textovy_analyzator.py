'''
projekt_1.py: první projekt do Engeto Python Akademie
author: Martin Čurda
email: curda.mart@gmail.com
discord: Martin Č.#0010
'''
#import pprint
registrovany_user = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
cara = "-" * 40
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
user = input("username: ")
password = input("password: ")
print(cara)
if password == registrovany_user.get(user):
    print("Welcome to the app", user, "\nWe have 3 texts to be analyzed.")
    print(cara)
else:
    print("Unregistered user, terminating the program..")
    print(cara)
    exit()
cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
print(cara)
if cislo_textu.isnumeric():
    if int(cislo_textu) in range(1, 4):
        pass
    else:
        print("Selected number is not in range, terminating the program..")
        exit()
else:
    print("That is not a number!! terminating the program..")
    exit()


jednotliva_slova = TEXTS[int(cislo_textu) - 1].split()
# print(jednotliva_slova)
vycistena_slova = list()

# Slova je potřeba dále vyčistit. U textu č.1 se některá slova nerozdělí.
# for slovo in jednotliva_slova:
#
vyskyt_slov = dict()
for slovo in jednotliva_slova:
    vycistena_slova.append(slovo.strip("\n.,:;?!-_"))

for slovo in vycistena_slova:
    if slovo not in vyskyt_slov:
        vyskyt_slov[slovo] = 1
    else:
        vyskyt_slov[slovo] = vyskyt_slov[slovo] + 1
# print(vycistena_slova)
# print(vyskyt_slov)
#     CELKOVÝ POČET SLOV
#     Čísla nejsou započítána do celkového počtu slov
pocet_slov = list(vyskyt_slov.values())
print("There are ",sum(pocet_slov), "words in the selected text.")
# print(vyskyt_slov)
     # POČET SLOV ZAČÍNAJÍCÍCH VELKÝM PÍSMENEM
titlecase_words = list()
for slovo in vycistena_slova:
    if slovo.istitle():
        titlecase_words.append(slovo)
    else:
        pass
print("There are", len(titlecase_words), "titlecase words")
    # POČET SLOV PSANÝCH VELKÝM PÍSMENEM
uppercase_words = list()
for slovo in vycistena_slova:
    if slovo.isupper() and slovo.isalpha():
        uppercase_words.append(slovo)
    else:
        pass
print("There are", len(uppercase_words), "uppercase words.")
    # POČET SLOV PSANÝCH MALÝM PÍSMENEM
lowercase_words = list()
for slovo in vycistena_slova:
    if slovo.islower() and slovo.isalpha():
        lowercase_words.append(slovo)
    else:
        pass
print("There are", len(lowercase_words), "lowercase words.")
#     # POČET ČÍSEL
pocet_cisel = list()
for slovo in vycistena_slova:
    if slovo.isnumeric():
        pocet_cisel.append(int(slovo))
    else:
        pass
print("There are", len(pocet_cisel), "numeric strings.")
     # SUMA ČÍSEL
suma_cisel = (sum(pocet_cisel))
print("The sum of all the numbers ", suma_cisel)
graf_data = list()
for slovo in jednotliva_slova:
    graf_data.append(len(slovo))
# print(graf_data)
graf_data_delky = dict()
for delka in graf_data:
    if delka not in graf_data_delky:
        graf_data_delky[delka] = 1
    else:
        graf_data_delky[delka] = graf_data_delky[delka] + 1
# print(sorted(graf_data_delky))
# print(graf_data_delky.keys())
# print(graf_data_delky.values())
graf_headder = (f"""{cara}
{"LEN|" : <4}{"OCCURENCES" : ^30}{"|NR." : >4}
{cara}
""")
print(graf_headder)

delka_slova = 0
for delka_slova in sorted(graf_data_delky.keys()):
    if delka_slova in graf_data_delky.keys():
        i = graf_data_delky.get(delka_slova)
        vyskyt_graf = i * "*"
        print(f" {delka_slova :>2}|{vyskyt_graf : <30}|{i :<2}")
        delka_slova = delka_slova + 1
    else:
        pass











