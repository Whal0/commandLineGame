from Engine import *


powitanie()
available = ["nowa", "wczytaj", "wyjdź"]
choice = input(">").lower().split()

while choice[0] not in available:
    choice = input(">").lower().split()
if choice[0] == "nowa":
    slowp("Świat przeżył nie jeden kataklizm, ale ludzkość zawsze znajduje drogę.\n"
          "To co zostało ze starego świata jest teraz cenniejsze niż jakikolwiek surowiec.\n"
          "Przez nie i nie tylko ruiny starego świata mają reputacje bycia śmiertelnymi pułapkami z których rzadko kto wracał, jednak obietnica bogactw i wiedzy zawsze znajdywała kolejnych śmiałków.\n"
          "Nazwano ich – Poszukiwaczami. Nawet wśród nich jest jedno miejsce które wzbudza grozę – Arkadia.\n"
          "Przed katastrofą było to latające miasto przyrównywane do Nieba. Teraz to ruina wypełniona obcą technologią i pustką.\n"
          "Jednak są i tacy co rzucą się na okazję…\n"
          "Ale już wszystko słyszałeś, więc już zdecydowałeś a więc:\n")
    creator()
    while True:
        check = input("Akceptujesz to: Y/N").upper()
        if check == "N":
            creator()
        elif check == "Y":
            x = 1
            break
    slowp(
        "Życie Poszukiwacza potrafi być trudne, kiedy w końcu udało ci się złapać twojego przewodnika – Dagona, myślałeś że nic już cię nie powstrzyma w zdobyciu Arkadii.\n"
        "Los to jednak okrutna kochanka.\n"
        "Jedyne co pamiętasz to wejście do ostatniego zabezpieczonego zakątka i podążenie za swoim towarzyszem do jednoszynowca który miał według pogłosek prowadzić za Bramę Niebios.\n"
        "Jak zawsze coś poszło nie tak i obudziłeś się w gruzie, bez swojego przewodnika i ekwipunku.\n"
        "Najwidoczniej nie pierwszy bo widzisz obok siebie MIECZ jak i TARCZE która widziała swojego lata świetności.\n"
        "Najpierw musisz odnaleźć Dagona – jeśli jeszcze żyje…\n")


elif choice[0] == "wczytaj":
    x = load()
elif choice[0] == "wyjdz":
    exit("Do następnego razu!")


if x == 1:
    downtown()
    x += 1
if x == 2:
    city()
    x += 1
if x == 3:
    inside()
    end()

