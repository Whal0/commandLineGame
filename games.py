from random import *
from threading import Timer
import time, string

# minigry/questy użyte w czasie gry

def mastermind():
    print("podaj 4 liczby jedna po drugiej \n1- dobra pozycja \n2-dobra liczba zle miejsce \n0- zle miejsce")
    input("enter aby grac")
    numberList = []
    guessList = []
    result = [0,0,0,0]
    check = 0
    tries = 2

    for p in range(4):
        rng = randint(1, 9)
        numberList.append(rng)

    while check != 4:
        guessList.clear()
        check = 0
        for i in range(4):
            user = int(input("liczba:"))
            guessList.append(user)

        for j in range(4):
            if guessList[j] == numberList[j]:
                result[j] = 1
                check += 1
            else:
                for k in range(4):
                    if guessList[j] == numberList[k]:
                        result[j] = 2
        print(result)
        tries -= 1
        if tries == 0:
            print("Porażka!")
            return 0
        print(f"Zostało {tries} prób")
    print("Sukces!")
    return 1
def fallout():
    print("Napisz dobre słowo z podanych na ekranie")
    input("enter aby grac")
    r = range
    keys = ["ALOZO", "ENACT", "SWORE", "PITYS", "SMELL", "CARTS", "RACES"]
    guesses = 4
    u, c = '_ '
    a = [choice('!"#$%&\'()*+/:;<=>?@[\\]^_{|}') for i in c * 360]
    L = len(keys[0])
    i = {*r(360 - len(keys[0]))}
    p = lambda x: '0x%02X' % x + c + ''.join(a[15 * x:][:15])
    for q in keys:
        s = choice([*i])
        a[s:s + L] = q
        i -= {*r(s - L, s - ~L)}
    interface = '''  %s
 /%s\\
|# %s #|
?%s?
? Witaj w Systemie IT Arkadii  Wersja:2.879   ?
? Hasło wymagane      ######?
?%s?
%%s?%s?
|%s|
\%s/
#   \%s/'''.replace('?', '|#|').replace('#', c * 4) % (
        u * 53, c * 53, u * 45, c * 45, c * 45, u * 45, c * 55, u * 55, u * 39) % (
                        '|    | %s | %s |    |\n' * 12) % (*[p(a) for b in range(12) for a in [b, b + 12]],)
    print(interface)
    correctAns = choice(keys)
    while guesses > 0:
        playerguess = input('Podaj hasło ('+'ilosc prób:' + str(guesses) + ' ) >')
        correct_letters = 0

        if playerguess.upper() == correctAns:
            print('Logowanie pomyślne.')
            return 1

        guesses -= 1
        interface.replace("X", guesses * "X")
        print(interface)
        print('Odrzucono.')
        for i in range(len(playerguess)):
            if playerguess[i].upper() == correctAns[i]:
                correct_letters += 1
        print(correct_letters, "/", len(correctAns), "correct")

    print("yikes")
    return 0

def krzyzyk():
    print("kolko i krzyzyk, grasz jako X\n wpisuj od 1-9\n 1|2|3\n4|5|6\n7|8|9")
    input("enter aby grac")
    PLANSZA = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}

    board_keys = []


    for key in PLANSZA:
        board_keys.append(key)


    def printBoard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])

    check = ["1","2","3","4","5", "6", "7", "8", "9"]
    turn = "X"
    count = 0
    end = False
    for i in range(10):
        if turn == "O":
            turn = 'O'
            ai = choice(check)
            check.remove(ai)
            print(ai)
            PLANSZA[ai] = turn
            count += 1
        else:
            while True:
                printBoard(PLANSZA)
                print("Twoja kolej")
                move = input()
                if PLANSZA[move] == ' ':
                    PLANSZA[move] = turn
                    count += 1
                    check.remove(move)
                    break
                else:
                    print("Juz zajete.\n Zagraj gdzie indziej!\n")

        if count >= 5:
            if PLANSZA['7'] == PLANSZA['8'] == PLANSZA['9'] != ' ':  # across the top
                printBoard(PLANSZA)
                print("\nKoniec.\n")
                print(" **** " + turn + " Wygrał. ****")
                end = True
            elif PLANSZA['4'] == PLANSZA['5'] == PLANSZA['6'] != ' ':  # across the middle
                printBoard(PLANSZA)
                print("\nKoniec.\n")
                print(" **** " + turn + " Wygrał. ****")
                end = True
            elif PLANSZA['1'] == PLANSZA['2'] == PLANSZA['3'] != ' ':  # across the bottom
                printBoard(PLANSZA)
                print("\nKoniec.\n")
                print(" **** " + turn + " Wygrał. ****")
                end = True
            elif PLANSZA['1'] == PLANSZA['4'] == PLANSZA['7'] != ' ':  # down the left side
                printBoard(PLANSZA)
                print("\nKoniec.\n")
                print(" **** " + turn + " Wygrał. ****")
                end = True
            elif PLANSZA['2'] == PLANSZA['5'] == PLANSZA['8'] != ' ':  # down the middle
                printBoard(PLANSZA)
                print("\nKoniec.\n")
                print(" **** " + turn + " Wygrał. ****")
                end = True
            elif PLANSZA['3'] == PLANSZA['6'] == PLANSZA['9'] != ' ':  # down the right side
                printBoard(PLANSZA)
                print("\nKoniec.\n")
                print(" **** " + turn + " Wygrał. ****")
                end = True
            elif PLANSZA['7'] == PLANSZA['5'] == PLANSZA['3'] != ' ':  # diagonal
                printBoard(PLANSZA)
                print("\nKoniec.\n")
                print(" **** " + turn + " Wygrał. ****")
                end = True
            elif PLANSZA['1'] == PLANSZA['5'] == PLANSZA['9'] != ' ':  # diagonal
                printBoard(PLANSZA)
                print("\nKoniec.\n")
                print(" **** " + turn + " Wygrał. ****")
                end = True

        if count == 9:
            print("Remis, jeszcze raz")
            x = krzyzyk()
            return x
        if end and turn == "X":
            return 1
        elif end and turn == "O":
            return 0

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

def hangman():
    print("zgadnij slowo z liter")
    input("enter aby grac")

    rand = ["pog", "champ"]
    target = choice(rand)
    guess = '_' * len(target)
    tries = 5

    while (guess != target) and (tries > 0):
        print('Now:', guess, "zgaduj")
        s = input(">")
        if len(s) > 1:
            print('1 litera!')
            continue

        guess = ''.join(s if target[i] == s else guess[i] for i in range(len(target)))

        if not any(target[i] == s for i in range(len(target))):
            tries -= 1
            print(f"Ilość prób: {tries}")
    if tries == 0:
        return 0
    else:
        return 1

def timebomb():
    print("Wpisz podany ciag znaków w odpowiednim czasie (mala literą)")
    input("enter aby grac")
    def gameover():
        print("\nPorażka...")
        input("Nacisnij aby kontynuowac")
    t = Timer(7.0, gameover)
    t.start()
    letters = string.ascii_lowercase
    word = ''.join(choice(letters) for i in range(10))

    userinput = input("Ciąg: " + word)
    if userinput == word:
        t.cancel()
        return 1
    return 0

def blackjack():
    print("Wygraj w blackjacka")
    input("enter aby grac")
    suits = ('♡', '♢', '♤', '♧')
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'As')
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'As': 11
    }

    class Card():
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return self.rank + self.suit

    class Deck():
        def __init__(self):
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))

        def __str__(self):
            deckComposition = ''
            for card in self.deck:
                deckComposition += '\n' + card.__str__()
            return "The deck has: " + deckComposition

        def shuffle(self):
            shuffle(self.deck)

        def deal(self):
            singleCard = self.deck.pop()
            return singleCard

    class Hand():
        def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0

        def addCard(self, card):
            self.cards.append(card)
            self.value += values[card.rank]

            # track aces
            if card.rank == 'As':
                self.aces += 1

        # test_deck = Deck()
        # test_deck.shuffle()
        # test_player = Hand()
        # pulled_card = test_deck.deal()
        # print(pulled_card)
        # test_player.addCard(pulled_card)
        # print(test_player.value)
        def checkAces(self):

            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1

    def hit(deck, hand):
        # handCard = deck.deal()
        # hand.addCard(singleCard)
        # hand.checkAces()
        hand.addCard(deck.deal())
        hand.checkAces()

    def hitOrStand(deck, hand):

        while True:
            x = input("grasz czy czekasz: g- grasz, c- czekasz ")
            if x[0].lower() == 'g':
                hit(deck, hand)
                return True
            elif x[0].lower() == 'c':
                print("Grasz stoi. Przeciwnik is playing.")
                return False
            else:
                print("Sorry, try again!")
                continue

    def showCards(player, dealer):
        print("\nKarty Przeciwnika: ")
        print("<Ukryta karta>")
        print('', dealer.cards[1])
        print("\nTwoje karty:", *player.cards, sep='\n ')

    def showAll(player, dealer):
        print("\nKarty Przeciwnika:", *dealer.cards, sep='\n ')
        print("Wartość Przeciwnika =", dealer.value)
        print("\nTwoje karty:", *player.cards, sep='\n ')
        print("Twoja wartosc =", player.value)

    def game():

        deck = Deck()
        deck.shuffle()

        playerHand = Hand()
        playerHand.addCard(deck.deal())
        playerHand.addCard(deck.deal())

        dealerHand = Hand()
        dealerHand.addCard(deck.deal())
        dealerHand.addCard(deck.deal())

        print("ROZDANIE 1")
        showCards(playerHand, dealerHand)
        i = 2
        while hitOrStand(deck, playerHand):
            print(f"ROZDANIE {i}")
            showCards(playerHand, dealerHand)
            i += 1
            if playerHand.value > 21:
                print("Przegrana")
                break

        if playerHand.value <= 21:
            while dealerHand.value < playerHand.value:
                hit(deck, dealerHand)

            showAll(playerHand, dealerHand)

            if dealerHand.value > 21:
                print("WYGRANA")
                return 1

            elif dealerHand.value > playerHand.value:
                print("PRZEGRANA")
                return 0
            elif dealerHand.value < playerHand.value:
                print("WYGRANA")
                return 1
            else:
                print("REMIS")
                playerHand.value = 0
                dealerHand.value = 0
                game()

    x = game()
    return x

def roshambo():
    print("Papier/Kamien/nozyce do 3")
    input("enter aby grac")
    choices = ("kamien", "papier", "nozyce")
    wins = [0, 0]
    while True:
        user = input("Co wybierasz?:").lower()
        ai = choice(choices)
        print(user)
        print(ai)
        if ai == user:
            print("Remis")

        elif user == "kamien":

            if ai == "papier":
                print(f"{user} bije {ai}  Przegrana!")
                wins[1] += 1
                print(f"Wynik: {wins[0]}-{wins[1]}")
            else:
                print(f"{user} bije {ai}  Wygrana!")
                wins[0] += 1
                print(f"Wynik: {wins[0]}-{wins[1]}")
        elif user == "papier":

            if ai == "nozyce":
                print(f"{user} bije {ai}  Przegrana!")
                wins[1] += 1
                print(f"Wynik: {wins[0]}-{wins[1]}")
            else:
                print(f"{user} bije {ai}  Wygrana!")
                wins[0] += 1
                print(f"Wynik: {wins[0]}-{wins[1]}")
        elif user == "nozyce":

            if ai == "kamien":
                print(f"{user} bije {ai}  Przegrana!")
                wins[1] += 1
                print(f"Wynik: {wins[0]}-{wins[1]}")
            else:
                print(f"{user} bije {ai}  Wygrana!")
                wins[0] += 1
                print(f"Wynik: {wins[0]}-{wins[1]}")
        else:
            print("wybierz coś normalnego!")

        if 5 in wins:
            if wins[0] == 5:
                print("KONIEC wygrałeś")
                return 1
            else:
                print("KONIEC przgrałeś")
                return 0

def reflex():
    goal = randint(4,25)
    input(f"Nacisnij enter po podanym czasie? Cel: {goal}s")
    t = time.time()
    while True:
        input()
        break
    t_end = time.time()
    player = t_end - t
    print(t_end - t)
    if goal - 0.25 < player < goal + 0.25:
        print("wygrana")
        return 1
    else:
        print("przegrana")
        return 0

# def fight(): w Engine.py
#     WEAPONS = ["miecz", "cegla", "rapier", "rura"]
#     class Fighter:
#         def __init__(self, name, str, dex, con, weapon):
#             self.weapon = weapon
#             self.name = name
#             self.sila = str
#             self.zwinnosc = dex
#             self.kondycja = con
#             self.hit = 100 + self.zwinnosc*10
#             self.hp = randint(self.kondycja * 5, self.kondycja * 10)
#             self.damage = randint(self.sila, self.sila * 3)
#     inv = [""]
#     check =  [item for item in inv if item in WEAPONS]
#     if check == []:
#         check = ["pięściami"]
#     player = Fighter(gracz.name,gracz.sila,gracz.zwinnosc,gracz.kondycja,check)
#     print(player.__dict__)
#     print(gracz.name)
#     #player = Fighter("jan", 3, 3, 3, check[0])
#     if gracz.level == 1:
#         enemy = Fighter("test dummy", 2, 2, 2, "patykiem")
#     elif gracz.level == 2:
#         enemy = Fighter("Automaton", 8, 5, 6, "lancą")
#         enemy.weapon = "Lanca"
#     elif gracz.level == 3:
#         enemy = Fighter("Kostium Nurka", 8, 3, 10, "wiertłem")
#         enemy.weapon = "Wiertło"
#     else:
#         enemy = Fighter("test dummy", 2, 2, 2, "patykiem")
#     print(enemy.name, "atakuje!")
#
#     if enemy.zwinnosc > player.zwinnosc:
#         print("Przeciwnik pierwszy")
#         time.sleep(1)
#     else:
#         print("Ty pierwszy!")
#         time.sleep(1)
#     i = 1
#     while enemy.hp > 0 and player.hp > 0:
#
#         print("\nTura", i)
#         print(f"Pozostałe HP:\n"
#               f"Ty: {player.hp}\n"
#               f"Przeciwnik: {enemy.hp}\n"
#               f"\nCo Robisz?")
#         print("- walka\n"
#               "- unik\n"
#               "- ucieczka")
#         choice = input(">").lower()
#
#         if choice == "walka":
#             print(f"{enemy.name} atakuje {enemy.weapon}!")
#             time.sleep(0.5)
#             if randint(1,100) <= player.hit:
#                 print(f"{enemy.name} trafia za {enemy.damage}")
#                 player.hp -= enemy.damage
#                 time.sleep(0.5)
#             else:
#                 print("Pudło!")
#                 time.sleep(0.5)
#             print(f"{player.name} atakuje {player.weapon}!")
#             time.sleep(0.5)
#             if randint(0,100) <= enemy.hit:
#                 print(f"{player.name} trafia za {player.damage}")
#                 enemy.hp -= player.damage
#                 time.sleep(0.5)
#             else:
#                 print("Pudło!")
#                 time.sleep(0.5)
#             player.hit = 100 - player.zwinnosc*10
#             enemy.hit = 100 - enemy.zwinnosc*10
#         elif choice == "unik":
#             player.hit = 20
#             print("Gotujesz się na atak")
#             print(f"{enemy.name} atakuje {enemy.weapon}!")
#             time.sleep(0.5)
#             if randint(0,100) <= player.hit:
#                 print(f"{enemy.name} trafia za {enemy.damage}")
#                 player.hp -= enemy.damage
#                 player.hit -= 5
#                 time.sleep(0.5)
#             else:
#                 print("Piękny unik! Przeciwnik jest otwarty na atak")
#                 enemy.hit += 20
#                 time.sleep(0.5)
#         i += 1

def minigra10():
    print("wip")
    return 1

def minigra11():
    print("wip")
    return 1

def minigra12():
    print("wip")
    return 1

def minigra13():
    print("wip")
    return 1

def minigra14():
    print("wip")
    return 1

def minigra15():
    print("wip")
    return 1

