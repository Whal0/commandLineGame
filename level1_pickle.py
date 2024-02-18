import pickle
from games import *

rooms = {
        1:{
            "ID": 1,
            "name": "Zrujnowany Dom",
            "opis": "Kiedyś to mogła być ładny domek, ale teraz to tylko parę kamieni i tynku z wielką dziurą ze wschodu.\n Przynajmniej zaoszczędzi Ci szukanie wyjścia. \nNa jednej z dalej stojących ścian widzisz DZIWNĄ NOTATKE,  leży też sporo CEGIEŁ.\n Widzisz wyjście do innego pomieszczenia.",
            "discovery": "",
            "pickups": ["miecz", "dziwna notatka", "cegla", "lupa", "czerwony krysztal", "tarcza"],
            "interest": ["portret","pokoj", "stol", "drewniana zabawka"],
            "desc": ["Ogromny portret rodziny, na kolanach ojca widzisz dwójkę dzieci, na spodzie framugi widnieje napis 20XX, troszkę ponad 200 lat temu, jednak dalej umieli fotografować bez użycia plazmidów. Wygląda jakby coś było za obrazem",
                    " Co ciekawe zauważasz w innym pokoju PORTRET, jak i dalej cały STÓŁ, kiedyś mieszkała tu rodziną. Nie widzisz żadnych ciał, tak jak w legendach miasto duchów opuszczone przez ludzi i bogów.",
                    "Na stole widzisz sporo kurzu, DREWNIANĄ ZABAWKĘ i LUPĘ",
                    "Mały drewniany koń, brakuje mu nogi."],
            "actions": ("drzwi", "miecz", "obraz"),
            "exits": {"wschod":2},
            "visited": True,
            "quest": False,
            "success": "Kamienie z sufitu są szybkie ale ty jesteś szybszy, udało Ci się złamać szyfr i zatrzymać rozpad. Na stole leży CZERWONY KRYSZTAŁ",
            "fail": "Nie udało się I oberwałeś kamieniem, dalej czujesz, że ta piwnica coś ukrywa."
        },
        2:{
            "ID": 2,
            "name": "Główna Ulica",
            "opis": "Po dokładniejszym rozglądnięciu dochodzisz do wniosku że to główna ulica tego sektora miasta kończącego się przy murze, zauważasz ALEJKĘ pomiędzy dwoma domami.",
            "discovery": "Wychodzisz na kamienną ulicę na północ widzisz jakąś sporą ścianę, naprzeciw ulica otwiera się, chyba trafiłeś do przedmieść miasta. \nZ kąta oka widzisz TABLICZKĘ, dalej zero śladu Degona, cała atmosfera napawa cię niepokojem, ale to nie czas na rozmyślanie,",
            "pickups": ["klucz", "niebieski krysztal"],
            "interest": ["tabliczka", "alejka"],
            "desc": ["Na drewnianej tablicy widnieje napis, Ogłoszenie dzielnicy Aor. Resztą papierów jest zniszczona. ",
                     "Idziesz zbadać alejkę, na końcu zauważasz DZWIGNIĘ, niepokojące jest fakt że cała aleja nie ma na sobie żadnych śladów zniszczeń"],
            "actions": ("dzwignia",),
            "exits": {"zachod":1,
                      "polnoc":5,
                      "poludnie":4},
            "visited": False,
            "quest": False,
            "success": "Szybki refleks jeszcze nigdy Cię nie zawiódł i udało Ci się wydostać z tej pułapki. Jednak samo istnienie takiej pułapki w środku miasta, uświadamia Cię o poziomie zagrożenia. Razem z tobą mechanizm uwolnił też NIEBIESKI KRYSZTAŁ, który zwisa za ruszoną DZWIGNIĄ",
            "fail": "Nie udało Ci się wyczuć momentu. Czujesz jak metalowy pręt przyszywa twoje ciało, DZWIGNIA wraca do swojej poprzedniej pozycji"
        },
        3:{
            "ID": 3,
            "name": "Opuszczony Sklep",
            "opis": "Okna są zbyt brudne abyś zobaczył co jest w środku, sam budynek trzyma się dobrze porównując go z otaczającymi go częściami stuktur.\n Kamienne elementy w na krawędziach pozwoliły temu budynkowi przeżyć dłużej niż reszcie.",
            "discovery": "Lekko zgniła pozostałość czegoś co przypomina ganek zdobi ten budynek, nad nim widzisz SZYLD, WEJŚCIE zamknięte, nie widzisz na ten moment innych.\n Wygląda jakby był to sklep w okolicy, teraz już dawno opuszczony",
            "pickups": ["plazmid", "bialy krysztal", "notatnik"],
            "interest": ["lada", "szyld", "wejscie", "kasa", "wnetrze"],
            "desc": ["na ladzie widzisz dziwną KASE, jak i kolejny NOTATNIK",
                     " Pół szyldu jest wyłamane, ale na reszcie w czerwonej farbie wydnieje … wędrowiec",
                     "Kasa wydaje się zepsuta i mechaniczna niestety nic w niej nie ma",
                     " Wnętrze jest pokrytę w kurzu i pajęczynach, wśród pustych pojemników widzisz całkiem pełny PLAZMID, widzisz LADE reszta wnetrza składa się tylko z zniszczonych desek i prochu"],
            "actions": ("sejf","cegla", "klucz"),
            "exits": {"zachod":4},
            "visited": False,
            "quest": False,
            "success": "Sejf otwiera się z cichym klikiem w środku widzisz BIAŁY KRYSZTAŁU ",
            "fail": "Z piskiem sejf szokuje twoje ciało elektrycznością"
        },
        4:{
            "ID": 4,
            "name": "Rynek",
            "opis": "Sama płyta wydaje się zrobiona z czerwonego grafitu. Gdyby to miasto dalej latało jak legendy mówią byłby to piękny kontrast z niebieskim niebem.\n Po rozglądnięciu widzisz zbudowaną SCENE z boku rynku razem ze zniszczonym oświetleniem ale też małe PODIUM.",
            "discovery": "Ulica otwiera się w pokaźny okrąg, zostały jeszcze szczątki czegoś co można było nazwać marketem. \nNa ziemi leżą poszarpane PLAKATY. Większość budynków jest w ruinie, jednak jeden na wschodzie wydaje się w dobrym stanie.\n Wiele BUDEK ustawionych w rzędach, wygląda jak poranny tak, albo jego żałosne resztki",
            "pickups": ["notes", "czarny krysztal"],
            "interest": ["plakaty", "budki", "scena"],
            "desc": ["Wiele strzępów kolorowych papierów, z tego co udało Ci się wyczytać przez to miejsce miała przechodzić grupa muzyków, z gitarą błyszczącą plazmidami, nie do myślenia używać tych cennych artefaktów do instrumentów.",
                     "Wiele z nich nie zostało, ale wygląda to jak typowy pchli market, z tego co widzisz rzędy były w tych samych kolorów, na jednym z nich widzisz NOTES"],
            "actions": ("podium",),
            "exits": {"polnoc":2,
                      "wschod":3},
            "visited": False,
            "quest": False,
            "success": "słyszysz skrzyp i z jednej z desek podium wystaje mała metalowa klatka, widzisz w niej CZARNY KRYSZTAŁU",
            "fail": "klapa w podłodze otwiera się pod tobą, I upadasz na kamień parę metrów w dół"
        },
        5:{
            "ID": 5,
            "name":"Brama Dystryktu",
            "opis": "Brama wygląda na dosyć pokaźną, a sam mur wokół ma z 4 metry gładkiego utwardzonego kamienia, na scianie zwisa NÓŻ i wygląda na to że jeden z PRĘTÓW jest zniekształcony",
            "discovery": "Dochodzisz do wielkiego muru na południowym końcu dzielnicy, znajdujesz dużą żelazną brame, za nią w oddali widzisz sławną Bramę Niebios, wejście do centrum Arkadii.\n Musisz się wydostać, Dagon mówił że w razie kłopotów ta brama to wasz punkt orientacyjny",
            "pickups": ["list w butelce"],
            "interest": ["pret","noz", "mur", "brama"],
            "desc": ["po chwili widzisz że to zardzewiały pret w kształcie kolniczyny",
                     "zwisający z muru pokaźny noż nie wiesz jak znalazł się tak wysoko ani dlaczego tam jest",
                     "nie widzisz żadnego miejsca w którym mur wydaje się naruszony, ten kamień jest zbyt twardy, za to nie daleko przy ścianie widzisz LIST W BUTELCE", "Na bramie nie widzisz żadnego miejsca na klucz, za to cały jest wygrawerowany ze wzorem którego nie rozumiesz spotykającej się w DZIURZE mniejszej niż pięść zaraz obok jest jest PANEL z którego wydobywa się lekki czerwony błysk "],
            "actions": ("panel",),
            "exits": {"poludnie":2},
            "visited": False,
            "quest": False,
            "success": "Udało Ci się wygrzebać kolejny mały KRZYSTAŁ, który spada na ziemie z dennym dziwiękiem",
            "fail": "Próbująć naprawić panel twoja ręka uderza o coś w środku, czujesz szok ognistej energii, szybko oskakujesz od PANELU."
        },
        6:{
            "ID": 6,
            "name":"Brama Niebios",
            "interest": ["uga","buga"],
            "pickups": [],
            "desc": [],
            "actions": (""),
            "exits": {}
        },
}



use = {
    "drzwi": krzyzyk,
    "dzwignia": timebomb,
    "podium": mastermind,
    "sejf": fallout,
    "panel": blackjack,
    "miecz": "Rozcinasz stare płótno, za nimi znajdują się DRZWI, ciekawe gdzie prowadzą, niestety miecz kruszy się w pół uderzając we framugę. Jesteś we WNETRZU",
    "cegla": " jeśli drzwi się nie ruszą czas na improwizacje, rzucasz cegłą w okno sklepu. Działa jak marzenie, wchodzisz do środka, uważając aby nie nadepnąć na resztki swojego nagłego wejścia. JESTEŚ",
    "klucz": "próbujesz otworzyć drzwi kluczem z alejki, o dziwo drzwi otwierają się z głośnym krzypieniem",
    "lada": "Za ladą jest SEJF, teraz tylko go otworzyć",
    "obraz": "Obraz jest zbyt duży abyś mógł go ruszyć",
    "wejscie": "Zamknięte na dobre",
    "dziura":"",
}


f = open("level_1.dat", "wb")
pickle.dump(rooms,f)
pickle.dump(use,f)
