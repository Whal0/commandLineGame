import random
import pickle
import os
import sys
import time

rooms = {}
use = {}


def slowp(string):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")


def load_rooms(i):
    global rooms
    global use
    file = open(os.path.join(sys.path[0], "level_" + str(i) + ".dat"), "rb")
    rooms = pickle.load(file)
    use = pickle.load(file)
    file.close()


story_level = 1
load_rooms(story_level)


class Hero:
    def __init__(self):
        self.name = ""
        self.profesja = ""
        self.hp = 0
        self.MAXHP = 0
        self.sila = 0
        self.zwinnosc = 0
        self.charyzma = 0
        self.kondycja = 0
        self.inteligencja = 0
        self.level = 1
        self.inventory = ["kompas","czerwony krysztal", "niebieski krysztal", "bialy krysztal", "czarny krysztal"]
        self.location = rooms[1]
        self.mapID = self.location["ID"]
        self.solvedQuests = 0

    def getstatus(self):
        print("\nNazwa postaci:", self.name, "\n"
                "Profesja:", self.profesja, "\n"
                "Poziom:", self.level, "\n"
                "Punkty życia:", f"{self.hp}/{self.MAXHP}\n"
              "---Statystyki---", "\n"
            "Siła:", self.sila, "\n"
            "Zwinność:", self.zwinnosc, "\n"
            "Charyzma:", self.charyzma, "\n"
            "Kondycja:", self.kondycja, "\n"
            "Inteligencja:", self.inteligencja, "\n"
            "Wykonane zadanie:", self.solvedQuests, "\n")

    def inventory_add(self, item):
        if item in gracz.location["pickups"]:
            self.inventory.append(item)
            print("Dodano", item, "do ekwipunku")
            gracz.location["pickups"].remove(item)
        else:
            print("Nie ma takiego przedmiotu!")

    def inventory_remove(self):
        item = input("Który przedmiot?\n>")
        if item in self.inventory:
           self.inventory.move(item)
        else:
            print("Nie posiadasz takiego przedmiotu!")

    def inventory_print(self):
        print("Przedmioty w ekwipunku:", *self.inventory, sep="\n")

    def inventory_use(self):
        item = input("Który przedmiot?\n>")
        if item in self.inventory:
            print("Użyto", item)
            interaction(item)


gracz = Hero()


def creator():
    gracz.name = input("Poszukiwaczu! Podaj swe imię:")
    print("Witaj", gracz.name + ".", "Powiedz mi swoją profesję:\n"
                                     "1 - Szermierz \n"
                                     "2 - Akolita \n"
                                     "3 - Archeolog \n"
                                     "4 - Bard \n"
                                     "5 - Strażnik \n"
                                     "6 - Zagubiony (losowe statystyki)  \n"
                                     "7 - Świerzak (wybór gracza)")
    prof = int(input())
    dostepne_profesje = ("Szermierz", "Akolita", "Archeolog", "Bard", "Strażnik", "Zagubiony", "Świerzak")
    cechy = ["STR", "DEX", "CHA", "CON", "INT"]
    stats = []
    gracz.profesja = dostepne_profesje[prof - 1]
    choices = {
        1: [3, 6, 3, 5, 4],
        2: [3, 3, 5, 3, 7],
        3: [4, 4, 4, 4, 5],
        4: [3, 5, 6, 4, 3],
        5: [6, 2, 4, 5, 4],
    }

    if prof == 6:
        for i in range(5):
            randomstat = random.randint(1, 6)
            stats.append(randomstat)

    elif prof == 7:
        points = 21
        j = 0
        while j < 5:
            print("Podaj ile punktow rozdac w", cechy[j], "(Min. 1 pkt/Max. 6 pkt) Pozostało", points,
                  "punktów")
            add = int(input())
            if add > points or add < 1 or add > 6:
                print("Zła ilość punktów. \n")
            else:
                stats.append(add)
                points -= add
                j += 1

    else:
        stats = choices.get(prof, [3, 3, 3, 3, 3])

    print("Statystyki postaci\n")
    for q in range(5):
        print(cechy[q] + ":", stats[q])

    gracz.hp = random.randint(stats[3] * 5, stats[3] * 12)
    print("Twoje HP:", gracz.hp)
    gracz.sila = stats[0]
    gracz.zwinnosc = stats[1]
    gracz.charyzma = stats[2]
    gracz.kondycja = stats[3]
    gracz.inteligencja = stats[4]
    gracz.MAXHP = gracz.hp


def powitanie():
    print("""
    ________          __     ______               
   / ____/ /__  ___  / /_   / ____/__  ____ ______
  / /_  / / _ \/ _ \/ __/  / / __/ _ \/ __ `/ ___/
 / __/ / /  __/  __/ /_   / /_/ /  __/ /_/ / /    
/_/   /_/\___/\___/\__/   \____/\___/\__,_/_/                                                       
    """)
    print("Witaj podróżniku co chcesz zrobić?")
    print("- Nowa gra\n"
          "- Wczytaj grę\n"
          "- Wyjdź")


def user():
    akcje = ["popatrz", "zabierz", "menu", "idz", "uzyj", "gdzie", "zbadaj", "debug"]
    try:
        check = input(">").lower().split()
        while check[0] not in akcje:
            print("Nieznana komenda")
            check = input(">").lower().split()

        if check[0] == "menu":
            menu()

        elif check[0] == "zabierz":
            try:
                temp = " ".join(check[1:])
                gracz.inventory_add(temp)
            except IndexError:
                print("Ale co?")
                user()

        elif check[0] == "idz":
            try:
                temp = check[1]
                move(temp)
            except IndexError:
                print("Ale gdzie?")
                user()

        elif check[0] == "zbadaj":
            try:
                temp = " ".join(check[1:])
                look(temp)
            except IndexError:
                print("Ale na co?")
                user()

        elif check[0] == "uzyj":
            try:
                temp = " ".join(check[1:])
                interaction(temp)
            except IndexError:
                print("Ale czego?")
                user()

        elif check[0] == "gdzie":
            print("Jesteś w", gracz.location["name"])
        elif check[0] == "popatrz":
            slowp(gracz.location["opis"])
        elif check[0] == "debug":
            gracz.solvedQuests = 5
    except IndexError:
        print("Napisz coś!")


def menu():
    while True:
        print("""
               #### MENU ####
                  - Mapa -
                 - Status -
                - Ekwipunek -
                 - Pomoc -
                 - Zapisz -
                 - Wczytaj -
               - Wróć do gry -
               - Wyjdź z gry -
               ###############
               """)
        choice = input(">").lower()
        if "mapa" in choice:
            mapa()
        elif "status" in choice:
            gracz.getstatus()
        elif "ekwipunek" in choice:
            eq()
        elif "pomoc" in choice:
            pomoc()
        elif "zapisz" in choice:
            save(rooms, gracz, use)
        elif "wczytaj" in choice:
            load()
        elif "wroc" in choice:
            break
        elif "wyjdz" in choice:
            exit("Do następnego razu!")


def eq():
    while True:
        gracz.inventory_print()
        choice = input("1. Usuń przedmiot\n"
                       "2. Użyj przedmiot\n"
                       "3. Powrót\n"
                       ">").lower()
        if "usun" in choice:
            gracz.inventory_remove()
        elif "uzyj" in choice:
            gracz.inventory_use()
            break
        elif "powrot":
            break


def mapa():
    mapy = ["""              
              +---------------+
              |               |
              |    BRAMA      |
              |               |
              +---+---^--+----+
                  +------+
                  |      |
                  |      |
                  |      |
    +------------++      |
    |            ||      |
    |            ||ULICA |
    |            ||      |
    |    DOM     ||      |
    |            |>      |
    |            ||      |
    |            ||      |
    |            ||      |
    +------------++      |
                  |      |
                  |      |
                  |      |
                  |      |
               xx +------xxx
           xxxxx           xxxxx
        xxxx                    xx
      xxx                        xxx
    xxx                            xx
  xxx                               xx
 xx                                  xx
xx                                    xx
x                                    +-----+
x                                    |     |
x                                    |  S  |
x                RYNEK               |  K  |
x                                    |  L  |
x                                    |  E  |
xx                                   |  P  |
 x                                   |     |
 x                                   +-----+
 xx                                   xx
  xx                                  x
   xx                               xx
    xx                            xxx
      xxx                        xx
        xxxxx                xxxx
            xxxxxxxxxxxxxxxxxx""",
            """
                             +--+DRZWI+---+
                             |+++-----++++|
                     +-------+------------+-------+
                     |                            |
                     |                            |
                     |             PLAC           |
                     |                            |
                     |                            |
                     |             ^              |
                     |             |              |
                     +-------------+--------------+
                                   |
                                   |
                            xxxxxxx|xxxxxxx             +-----------+
                          xxx              xxxxx        |           |
                        xx                     xxx      |           |
+-------------+       xx                         xx     |           |
|             |      xx                           xx    |           |
|             |      x                             xx   |   WIEZA   |
|             |     x                               x   |           |
|             |     x                               xx  |           |
|             |    xx                                x  |           |
|    SCIANA   <+-----           AGORA                 ---+->         |
|             |    x                                 x  |           |
|             |    xx                               xx  |           |
|             |     x                               x   |           |
|             |     xx                             xx   |           |
|             |      x                            xx    |           |
+-------------+       xx                          x     |           |
                       xx                      xxx      +-----------+
                         xxxxxxxxxxx|xxxx xxxxxx
                                    |
                       +------------+-------------+
                       |            v             |
                       |                          |
                       |                          |
                       |          RATUSZ          |
                       |                          |
                       |                          |
                       +--------------------------+
            """,
            """
    +-----------+
    |           |
    | GENERATOR |
    |           |
    |           |
    |      |    |
    +------+----+
           |
+----------+-----------+
|          |           <-------------+
|                      |             |
|                      |      +------+-----+
|                     -+--+   |            |
|      SERCE           |  |   |            |
|                      |  |   |  FABRYKA   |
|                      |  |   |            |
+-----------^----------+  |   +------+-----+
            |             |          |
     +------+-------+     |          |
     |      |       |     |          |
     |  PRZEDSIONEK |     |          |
     +--------------+     |          |
                          |    +-----+-----+
                          |    |           |
                          |    |           |
                          |    |           |
                          +---->  WARSZTAT |
                               |           |
                               |           |
                               |           |
                               +-----------+
            """]
    print(mapy[gracz.level - 1])


def pomoc():
    print("""
        Nie używaj polskich liter w inpucie.
        Przedmioty z interakcją są CAPSEM
        Zbieraj wszystko co zobaczysz
        
        Dostępne komendy:
        zbadaj <obiekt> - Zbadaj obiekt w otoczeniu
        zabierz <przedmiot> - Jeśli możliwe zabiera przedmiot i umieszcza w ekwipunku
        idz <kierunek> - Przejdź do innej lokacji, dostępne kierunki: polnoc, wschod, zachod, poludnie
        uzyj <obiekt> - użyj przedmiotu z ekwipunku lub w otoczeniu, może aktywować quest, odkryć nowe możliwośći
        gdzie - sprawdz swoją obecną pozycję
        popatrz - rozejrzyj się w swojej lokacji (opis lokacji)
        """)


def save(r, g, u):
    name = input("Jak nazwiesz zapis:")
    if not os.path.exists('saves'):
        os.makedirs('saves')
    with open(os.path.join("saves", name + "_" + gracz.name+".dat"), 'wb') as zapis:
        pickle.dump(g, zapis, pickle.HIGHEST_PROTOCOL)
        pickle.dump(r, zapis, pickle.HIGHEST_PROTOCOL)
        pickle.dump(u, zapis, pickle.HIGHEST_PROTOCOL)
        zapis.close()
        print("zapis pomyślny")
        print(g, r, u)


def load():
    global rooms
    global use
    global gracz
    global story_level

    if not os.path.exists('saves'):
        print("Brak zapisów")
        return
    else:
        arr = os.listdir("saves")
        if len(arr) == 0:
            print("Brak zapisów")
            return

        for i in range(len(arr)):
            print(f"{i + 1}. {arr[i]}")
        choice = int(input()) - 1

        with open(os.path.join("saves", arr[choice]), "rb") as wczyt:
            print(os.path.join("saves", arr[choice]))
            gracz = pickle.load(wczyt)
            rooms = pickle.load(wczyt)
            use = pickle.load(wczyt)
            wczyt.close()
    load_rooms(gracz.level)
    return gracz.level


def move(kierunek):
    if kierunek in gracz.location["exits"]:
        print("Idziesz na", kierunek)
        gracz.location = rooms[gracz.location["exits"].get(kierunek, "yikes")]
        gracz.mapID = gracz.location["ID"]
        if not gracz.location["visited"]:
            print(gracz.location["discovery"])
            gracz.location["visited"] = True
        else:
            print("Dotarłeś do", gracz.location["name"])

    else:
        print("Tam nic nie ma!")


def look(obiekt):
    if obiekt in gracz.location["interest"]:
        slowp(gracz.location["desc"][gracz.location["interest"].index(obiekt)])


def interaction(choice):
    if choice == gracz.location["actions"][0] and gracz.location["quest"] is False:
        win = use[choice]()
        if win:
            gracz.location["quest"] = True
            slowp(gracz.location["success"])
            gracz.solvedQuests += 1
        else:
            slowp(gracz.location["fail"])
            gracz.hp -= 5 * gracz.level
    elif choice == gracz.location["actions"][0] and gracz.location["quest"]:
        print("Już do zrobiłeś!")

    elif choice in gracz.location["actions"] and (choice in gracz.inventory):
        gracz.inventory.remove(choice)
        slowp(use[choice])
        del use[choice]

    elif choice in gracz.location["actions"]:
        slowp(use[choice])

    else:
        print("Nie możesz tego tutaj użyć!")


def loadnext():
    global story_level
    story_level += 1
    load_rooms(story_level)
    gracz.mapID = 1
    gracz.solvedQuests = 0
    gracz.location = rooms[1]


def levelup():
    gracz.level += 1
    cechy = ["Siła", "Zręczność", "Charyzma", "Kondycja", "Inteligencja"]
    print("LEVEL UP! \n Jaką ceche wybierasz?")
    print(*cechy, end=".\n")
    choice = input(">").lower()
    if choice.startswith("s"):
        gracz.sila += 2
    elif choice.startswith("z"):
        gracz.zwinnosc += 2
    elif choice.startswith("c"):
        gracz.charyzma += 2
    elif choice.startswith("k"):
        gracz.kondycja += 2
        gracz.MAXHP += random.randint(6, 24)
        gracz.hp = gracz.MAXHP
    elif choice.startswith("i"):
        gracz.inteligencja += 2
    else:
        print("Wybierz jedno!")


def downtown():
    DialogFlag = True
    EndFlag = False
    x = False
    check = ["czerwony krysztal", "niebieski krysztal", "bialy krysztal", "czarny krysztal"]

    print("CEL: Znajdz Dagona")
    while True:

        side = [item for item in gracz.inventory if item in check]
        if len(side) == 4:
            x = True

        user()
        if gracz.solvedQuests == 5 and DialogFlag and x:
            slowp("Po zebraniu kryształów, zaczynają emanować dziwną energią, może uda Ci się nimi otworzyć te drzwi")
            print("CEL: Użyj KRYSZTAŁY na Bramie")
            EndFlag = True
            DialogFlag = False
        if gracz.mapID == 5 and EndFlag:
            slowp(
                "\"Hej! Jednak żyjesz, miałem czekać do zmroku, potem wracać Musiałeś nie dostać aż tak mocno jeśli pamiętałeś żeby spotkać się tu. Sam znalazłem się 2 kilometry stąd nawet przytomny. Miałem trochę czasu dla siebie i znalazłem coś\"\n"
                "Dagon wyciąga dziwny dysk z różnymi obrazami i polami.\n"
                "\"Mam dziwne przeczucie że to pozwoli nam przekroczyć Bramę, bądź gotowy na zostanie historią ;)\"\n"
                "Dagon pochodzi do Bramy. Z bliska widzisz jak ogromna jest, freski zdobią jej ściany przedstawiają scenę wstępu do nieba człowieka z złotą koroną i błękitnym kryształem w ręce przez dziurę w chmurach. Nad obrazem widnieje napis: \"ἀβασίλευτος\"\n"
                "Dagon widzi twoją konfuzję i zaczyna tłumaczyć: \n"
                "\"Nie zniewolony przez Króli\" ~ może przez takie pokazy pychy rzeczy tak się potoczyły. Heh kto wie, nie mi oceniac kiedy jestem w tym samym miejscu”  "
                "Kończąc to zdanie wkłada dysk w slot na środku drzwi i po chwili słyszysz głośny trzask. Po chwili orientujesz się że Brama się otwiera. Na twarzy Dagona maluje się euforia. \"Bingo. Szybko nie wiadomo czy ten mechanizm wytrzyma\". Razem ze swoim przewodnikiem przebiegasz przez otwartą szparę w Bramie. Dotarłeś do Arkadii - miasta które dotknęło nieba…\n"
                "Razem dochodzicie do centrum miasta, ogromny oktagon na środku którego stoi POSĄG, widzisz że 4 z ośmiu odnóg są zawalone, Dagon zaczyna - \"Ja na razie zostanę tutaj według legend nazywali to miejsce Agorą na cześć starożytnej cywilizacji której język był na Bramie, ale teraz jedyne miejsce w które chcę się dostać teraz, to tam:” pokazując na wielką szpiczastą betonową wieże kilka razy większe niż cokolwiek co jeszcze stoi.\n "
                "\"Sam fakt, że to coś przetrwało daje mi dobre przeczucia na temat tego co jest w środku\"\n"
                "Dotarłeś do serca miasta, czas pozwiedzać.\n"
            )
            break
        if gracz.hp <= 0:
            przegrana()

    levelup()
    loadnext()


def city():
    dialogFlag = True
    endFlag = False
    x = False
    check = ["herb slonca", "herb natury", "herb wodospadu", "herb burzy", "herb tornada"]
    print("CEL: Eksploruj")
    while True:
        side = [item for item in gracz.inventory if item in check]
        if len(side) == 5:
            x = True

        user()
        if gracz.solvedQuests == 5 and dialogFlag and x:
            endFlag = True
            slowp("Dagon woła do Ciebie: \"Hej te herby, mogą działać podobnie jak mój\" Przypominasz sobie jak otworzył Bramę\n"
                  "Nie jest to zły pomysł, powinieneś spróbować")
            print("CEL:Idz do BRAMY")
            dialogFlag = False
        if gracz.mapID == 6 and endFlag:
            slowp("Wasza teoria się sprawdziła, herby były przewodnikami i wszystkie linie między płytami metalowych drzwi wypełniają się płynami różnych kolorów.\n "
                  "Po chwili słychać klik i wielka zębatka zaczyna się ruszać razem z drzwiami w lewo chowając się w ścianę Dagon mówi:\n"
                  "\"Leć ja przypilnuje żeby nic nie przeszło\""
                  "Przechodzisz przez próg wieży, bo chwili chodzenia w ciemnym korytarzu, naciskach na płytkę naciskową, z hukiem otwarte wyjście jest zablokowane wielkim kawałkiem metalu z sufitu.\n"
                  "Dagon jednak nie da rady dołączyć. Mimo to idziesz dalej.\n"
                  "Dochodzisz do dwustronnych drzwi do których obok tabliczka piszę „Przedsionek Nieba” – lekko zaniepokojony przechodzisz przez nie.\n"
                  "W środku jest mały pokój, jabky poczekalnia, na ścianach jest sporo elektroniki, parę krzeseł i oszklone biurko\n")
            break
        if gracz.hp <= 0:
            przegrana()
    levelup()
    loadnext()


def inside():
    dialogFlag = True
    endFlag = False
    x = False
    check = ["oko", "klucz"]
    print("CEL: Wydostań się")
    while True:
        side = [item for item in gracz.inventory if item in check]
        if len(side) == 2:
            x = True

        user()
        if gracz.solvedQuests == 5 and dialogFlag and x:
            endFlag = True
            slowp("Wydaje Ci się że masz wszystkie przedmioty żeby aktywować generator")
            print("CEL:Idz do GENERATORA")
            dialogFlag = False
        if gracz.mapID == 5 and endFlag:
            break
        if gracz.hp <= 0:
            przegrana()


def end():
    side = ["dziwna notatka", "list w butelce", "notes", "notatnik", "papiery", "dokument", "dziennik"]
    check = [item for item in gracz.inventory if item in side]
    stat = [gracz.sila, gracz.zwinnosc, gracz.charyzma, gracz.kondycja, gracz.inteligencja]
    badend2 = any(i >= 8 for i in stat)
    final = len(check)
    if final >= 5:
        slowp("Generator zaczyna swój szum, po chwili myślisz że był to słaby pomysł.\n"
              "Wraz z coraz większą siłą czujesz jak całe pomieszczenie zaczyna się trząść ale jesteś pewny z papierów że wszystko wykonałeś dobrze.\n"
              "Po chwili wstrząsy ustają i jedyne co słychać to kojący teraz szum generatora.\n"
              "Wychodzisz na zewnątrz żelazne wrota uchylone ze swojego miejsca.\n"
              "Widzisz Dagona. \"Nie mogę naprawdę to zrobiłeś, zrozumiem eksploracje ale przywrócenie miasta do życia , nie brałem Cię za maniaka ale Ci się udało\" \n"
              "Mija parę dni zanim razem z Dagonem jesteście znani na całym globie, Arkadia zostaje odbudowana tym razem bez planów żeby wzbić się w powietrze.\n"
              "Dzięki studiowaniu generatora i resztek notatek Technokraty, ludzkość nowej ery zyskuje wcześniej niepomyślane.\n"
              f"Na płycie Agorskiej na twoją cześć zostaje wyryte: Nowemu bohaterowi {gracz.name}, który odzyskał wieczną zgubę.\n")
    elif badend2:
        slowp("Generator zaczyna swój szum, po chwili myślisz że był to słaby pomysł.\n"
              "Wraz z coraz większą siłą czujesz jak całe pomieszczenie zaczyna się trząść, uciekasz z generatora.\n"
              "Wychodząc z windy widzisz jak cały budynek teraz zaczyna wibrować, szkło na ścianach pęka i spada wokół Ciebie.\n"
              "Ekran na kolumnie daje potwierdzenie powrotu generatora ale dalej wyświetla błąd, tym razem twój.\n"
              "Uciekasz dalej, drzwi są uchylone. Przebiegasz przez Arkadię, wiesz że nie masz dużo czasu.\n"
              "Przy Agorze spotykasz Dagona, alarmując go uciekacie razem. O wspólnych siłach wydostajecie się poza Bramę teraz w pełni operacyjną i znajdujecie najbliższe tory za pomocą których uciekacie.\n"
              "W trakcie słyszczycie huk i błysk światła z jednej strony tunelu. Udaje się dam wydostać zanim się zawalił. W chmurze pyłu opuszczacie swój szynowiec.\n"
              "Dagon obraca się i mówi: \"Mi chyba starczy poszukiwania na jakiś czas\" \n"
              "Obracasz się razem z nim widąc jak w środku ruin tego miasta teraz jest jeszcze większy krater wyrytu od środka. \n"
              "Wiele rzeczy nie zostanie odkrytych, ale przynajmniej wyszedłeś z Arkadii cały.\n")
    else:
        slowp("Generator zaczyna swój szum, po chwili myślisz że był to słaby pomysł.\n"
              "Wraz z coraz większą siłą czujesz jak całe pomieszczenie zaczyna się trząść, uciekasz z generatora.\n"
              "Wychodząc z windy widzisz jak cały budynek teraz zaczyna wibrować, szkło na ścianach pęka i spada wokół Ciebie.\n"
              "Ekran na kolumnie daje potwierdzenie powrotu generatora ale dalej wyświetla błąd, tym razem przez Ciebie.\n"
              "Uciekasz dalej, drzwi są uchylone. Przebiegasz przez Arkadię, wiesz że nie masz dużo czasu.\n"
              "Przy Agorze spotykasz Dagona, alarmując go uciekacie razem. Jesteś jednak za słaby by kontynuować.\n"
              "Dagon zostawia Cię blisko miejsca w którym się obudziłeś.\n"
              "Upadasz na kamień i ostatnie co widzisz to jak cały środek miasta zapada się w stronę Igły, zanim zostajesz zmiażdżony.\n")


def przegrana():
    print("Czujesz jak życie ucieka z twojego ciała, jednak ty też nie dałeś rady \n"
          "GAME OVER")
    temp = input("Wczytać zapis Y/N").lower()
    while True:
        if temp == "y":
            load()
        elif temp == "n":
            exit("Do następnego razu!")


def fight():  # minigra reszta w pliku games.py
    WEAPONS = ["miecz", "cegla", "rapier", "rura"]

    class Fighter:
        def __init__(self, name, strength, dex, con, weapon):
            self.weapon = weapon
            self.name = name
            self.sila = strength
            self.zwinnosc = dex
            self.kondycja = con
            self.hit = 100 + self.zwinnosc * 10
            self.hp = random.randint(self.kondycja * 5, self.kondycja * 10)
            # self.damage = random.randint(self.sila, self.sila * 4)

    inv = [""]
    check = [item for item in inv if item in WEAPONS]
    if not check:
        weapon = "pięściami"
    else:
        weapon = check[0]
    player = Fighter(gracz.name, gracz.sila, gracz.zwinnosc, gracz.kondycja, weapon)
    if gracz.level == 1:
        enemy = Fighter("test dummy", 2, 2, 2, "patykiem")
    elif gracz.level == 2:
        enemy = Fighter("Automaton", 8, 5, 6, "lancą")
        enemy.weapon = "Lanca"
    elif gracz.level == 3:
        enemy = Fighter("Kostium Nurka", 8, 3, 10, "wiertłem")
        enemy.weapon = "Wiertło"
    else:
        enemy = Fighter("test dummy", 2, 2, 2, "patykiem")
    print(enemy.name, "atakuje!")

    if enemy.zwinnosc > player.zwinnosc:
        print("Przeciwnik pierwszy")
        time.sleep(1)
    else:
        print("Ty pierwszy!")
        time.sleep(1)
    i = 1
    while enemy.hp > 0 and player.hp > 0:

        print("\nTura", i)
        print(f"Pozostałe HP:\n"
              f"Ty: {player.hp}\n"
              f"Przeciwnik: {enemy.hp}\n"
              f"\nCo Robisz?")
        print("- walka\n"
              "- unik\n"
              )
        choice = input(">").lower()

        if choice == "walka":
            print(f"{enemy.name} atakuje {enemy.weapon}!")
            time.sleep(0.5)
            if random.randint(1, 100) <= player.hit:
                damage = random.randint(enemy.sila, enemy.sila * 3)
                print(f"{enemy.name} trafia za {damage}")
                player.hp -= damage
                time.sleep(0.5)
            else:
                print("Pudło!")
                time.sleep(0.5)
            print(f"{player.name} atakuje {player.weapon}!")
            time.sleep(0.5)
            if random.randint(0, 100) <= enemy.hit:
                damage = random.randint(player.sila, player.sila * 3)
                print(f"{player.name} trafia za {damage}")
                enemy.hp -= damage
                time.sleep(0.5)
            else:
                print("Pudło!")
                time.sleep(0.5)
            player.hit = 100 - player.zwinnosc * 10
            enemy.hit = 100 - enemy.zwinnosc * 10
        elif choice == "unik":
            player.hit = 20
            print("Gotujesz się na atak")
            print(f"{enemy.name} atakuje {enemy.weapon}!")
            time.sleep(0.5)
            if random.randint(0, 100) <= player.hit:
                damage = random.randint(enemy.sila, enemy.sila * 3)
                print(f"{enemy.name} trafia za {damage}")
                player.hp -= damage
                player.hit -= 5
                time.sleep(0.5)
            else:
                print("Piękny unik! Przeciwnik jest otwarty na atak")
                enemy.hit += 20
                time.sleep(0.5)
        i += 1

    if player.hp < 0:
        gracz.hp = 0
        return 0
    else:
        return 1
