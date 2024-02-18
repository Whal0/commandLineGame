import pickle
from games import *
from Engine import *

rooms = {
        1:{
            "ID": 1,
            "name": "Agora",
            "opis": "Wielki oktagonalny plac, widzisz metalową TABLICE blisko miejsca z którego przyszliście, Dagona który siedzi obok POSĄGU.\n Sama skala tego miejsca Cię zaskakuje nic teraz nie mogłoby wyglądać tak pokaźnie.",
            "discovery": "",
            "pickups": ["herb slonca"],
            "interest": ["posag","plyta", "tablica"],
            "desc": ["Wielki marmurowy posąg, wydaje się że to człowiek z skrzydłami anioła, lecz jego twarz i ręce nie są już na nim, składa się to na niepokojącą postać, na jednej ze ścian postawy jest metalowa PŁYTA"," Czytasz: \"Ku wiecznej wyprawie i niezłomnej woli\" widzisz z jak z jeden ze ścian wychodzi mała miedziana linia idąc za nią odkrywasz ukryty PRZYCISK", "Podchodząc widzisz że to mapa miasta:\n Zachód - Ściana Widm\nWschód - Księżycowa Wieża\n Południe - Ratusz\n Północ - Mechaniczny Plac\n Północny zachód - Wielki… \n reszta jest zniszczona" ],
            "actions": ("przycisk", ),
            "exits": {"wschod":2,
                      "zachod":4,
                      "polnoc":5,
                      "poludnie":3},
            "visited": True,
            "quest": False,
            "success": "Udaje Ci się otworzyć mechanizm, w małym pudełeczku widzisz HERB ŚŁOŃCA",
            "fail": "Mechanism pulsuje ciepłem, zostajesz poparzony"
        },
        2:{
            "ID": 2,
            "name": "Ksieżycowa Wieża",
            "opis": "W środku widzisz że wszystkie ściany są w różnych odcieniach niebieskiego a sufit jest pstrokato żółty,\n widzisz SCHODY spiralnie wijące się ku górze, z boku pokoju widzisz małe BIURKO. Na jednej ze ścian wisi RAPIER",
            "discovery": "Zbliżasz się do wieży, mniejszej niż ta na horyzoncie, ta jest cała w gradiencie z niebieskiego do czarnego u góry gdzie jest szklana kopuła, drzwi są wyłamane, wchodzisz do środka",
            "pickups": ["herb natury", "papiery"],
            "interest": ["biurko", "schody"],
            "desc": ["Małe biureczko na którym leża jakieś PAPIERY"],
            "actions": ("schody",),
            "exits": {"zachod":1},
            "visited": False,
            "quest": False,
            "success": "Jesteś szybki I udaje Ci się przekroczyć schody bez wpadania w dziury. Na górze widzisz piękny widok opuszczonego miasta przez rozbitą kopułe W środku okręgu widzisz pięknie ozdobione pudełko w którym leży HERB NATURY",
            "fail": "Mokry kamień nie jest twoim przyjacielem. Spadasz na sam dół wieży."
        },
        3:{
            "ID": 3,
            "name": "Ratusz",
            "opis": "Widzisz 4  różne drzwi i schody do góry. 2 z nich są zawalone razem ze schodami, jedne z nich są zamknięte od drugiej strony.\n Idziesz do jedynej dostępnej i również największej przestrzeni.\n W środku widzisz typowe ustawienie biura jakiegoś burmistrza.\n Z lewej widzisz GLOBUS, z prawej małą BIBLIOTEKE, przy oknach z drugiej strony jest wielkie KRZESŁO przy biurku.\n Za nim pomiędzy oknami jest RAMA bez obrazu",
            "discovery": "Podchodzisz do pokaźnego gmachu który oznaczasz jako Ratusz tego miasta. Przed nim widzisz TABLICZKĘ z ogłoszeniami i ogromne drewniane drzwi. Udaje Ci się je otworzyć i wkraczasz do Ratusza",
            "pickups": ["herb tornada", "lina", "dokument"],
            "interest": ["tabliczka", "biblioteka", "globus", "archiwum", "rama"],
            "desc": ["Czytasz Tablicę:\nUwaga mieszkańcy Arkadii, dzielnica Zadasz blisko Mechanicznego Parku będzie zamknięta przez najbliższe parę dni z powodu renowacji. STANOWCZY ZAKAZ ZBIŻANIA SIĘ DO IGŁY\nDo Igły? Brzmi jak nazwa tamtej wieży, ciekawe co się z nią stało",
                    "Na półkach widzisz jeszcze kilka książek uchronionych przed zagładą ich tytuły brzmią:\nWielki Tom Poezji Niebiańskiej\nPlazmidy - igranie z Bogiem?\n Dziennik Arkadii\n Wielkie wojny starożytnych - za czasów pochodni i włóczni\nNawet ciekawa selekcja szkoda że reszta nie jest kompletna.",
                    "Globus mapy starego świata, jeszcze widać na niej sporo wysp które już nie istnieją, wszystkie 3 kontynenty są dalej razem. To musiało naprawdę ułatwiać podróż",
                    "W archiwum znajdujesz oprócz sterty zniszczonych papierów, jeden DOKUMENT zachowany w jakiejś dziwnej substancji, papier stał się dziwnie śliski i gibki, oprócz tego tylnia ściana zawiera piękne malowidło przedstawiające tą samą skrzydlatą postać co posąg, tym razem w całej jego okazałośći",
                    "Rama jest podpisana - Wielki Arbert Renolds 20XX, zgadujesz że to jeden z ostatnich burmistrzy przed katastrofą"],
            "actions": ("krzeslo","rapier"),
            "exits": {"polnoc":1},
            "visited": False,
            "quest": False,
            "success": "aaaaaaa",
            "fail": "bbbbbbbbb"
        },
        4:{
            "ID": 4,
            "name": "Sciana Widm",
            "opis": "Po bliższej obserwacji zauważasz że każda cegła jest innego koloru i wszystkie ciągle są pod wpływem ten wody bez źródła o dziwo żadna z nich nie uległa rozpadowi.\n Im dłużej się przyglądasz tym większe wrażenie że coś się pojawia i znika",
            "discovery": "Przed sobą widzisz dziwną ścianę, wydaje się że się ruszać. Podchodzisz bliżej i ze spokojem notujesz że jest ruchoma.\n Po chwili zauważasz że ta ściana jest ciągle mokra.\n Nie wiesz skąd woda napływa ale wygląda to jakby ta ściana jedyną rzeczą trzymająca to miejsce przed zalaniem, kątem oka widzisz metalowy ZNAK",
            "pickups": ["herb wodospadu", "cegla"],
            "interest": ["znak",],
            "desc": ["Na znaku jest napisane: Magia! Tęczowe widma,  hipnotyczne sny. Nie przyglądajcie się zbyt długo! Kto wie co zobaczycie na ten przeklętej ścianie"],
            "actions": ("sciana",),
            "exits": {"wschod": 1,},
            "visited": False,
            "quest": False,
            "success": "Na szczęście halucynacja odchodzi bo tym jak impulsywnie opowidasz na pytanie. Co dziwne twoja ręka wybiła jedną z CEGIEŁ i teraz widzisz również HERB WODOSPADU.",
            "fail": "Nie udaje Ci się wykonać zadania. Wizje odchodzą ale zostajesz z ogromnym bólem głowy"
        },
        5:{
            "ID": 5,
            "name":"Mechaniczny Park",
            "opis": "Wygląda jak opuszczony plac konstrukcji, metal i beton wiją się w dziwne formy.\n Widzisz porozrzucane narzędzia, wiele RUR, dużo ziemi i błota.\n Jednak wszystko w tym obszarze jest pokryte w ścieżkach, ŁAWKACH, METALOWYCH DRZEWACH to nie budowa ale jakiegoś rodzaju park atrakcji",
            "discovery": "Docierasz do ogrodzonego żelaznym płotem kwadratu, nad framugą bramy są piękne wzory które są kontynuowane na ogrodzeniu wzdłuż, betonowe ścieżki zaczynają Cię prowadzić.\n Nie wiesz czy to przez czas, czy z designu to miejsce wygląda jak teren budowy parku dla robotów.\n Sam metal i beton.",
            "pickups": ["herb burzy", "rura", "srubokret"],
            "interest": ["lawka","metalowe drzewa"],
            "desc": ["Ławka zrobiona z metalu, ale kiedy na niej siadasz jest dziwnie ciepła oraz miękka. Wstając pod ławką widzisz ŚRUBOKRĘT ", "Klony natury zbudowane z jakiegoś czarnego metalu, w zestawieniu ze stanem miastka tworzą bardzo zimną atmosferę"],
            "actions": ("robot",),
            "exits": {"poludnie": 1,
                      "polnoc": 6},
            "visited": False,
            "quest": False,
            "success": "Automaton zaczyna się niekontrolowanie poruszać po czym upada z głośnym echem, z jego wnętrza wysuwa się HERB BURZY - najpewniejsze źródło jego mocy.",
            "fail": "Widzisz jak twój mechaniczny przeciwnik wystrzeliwuje piorun ze swojej lancy. Tracisz przytomność."
        },
        6:{
            "ID": 6,
            "name":"Dziwne Drzwi",
            "interest": [],
            "opis": "Patrzysz się na wielkie ozłocone drzwi z wielkim kołem zębatym w środku.\n Każdy z 6 zębów ma miejsce na coś 2 są już wypełnione, widzisz góry na przeciwnym widzisz kosmos. Kolejne 4 sloty są puste",
            "discovery": "Pochodzisz do wejścia tego dziwnego drapacza chmur, ale jego wejście nie przypomina niczego co kiedykolwiek widziałeś bądź słyszałeś z legend. Dagon miał rację to miejsce skrywa jakiś większy sekret",
            "pickups": [],
            "desc": [],
            "actions": ("","drzwi"),
            "exits": {"poludnie": 5,},
            "visited": False,
            "quest": False,
            "success": "Wasza teoria się sprawdziła, herby były przewodnikami i wszystkie linie między płytami metalowych drzwi wypełniają się płynami różnych kolorów, po chwili słychać klik i wielka zębatka zaczyna się ruszać razem z drzwiami w lewo chowając się w ścianę",
            "fail": "Wszystkie herby wyskakują ze swoich miejsc z falą uderzeniową swoich elementów"

        },
    }

use = {
    "przycisk": hangman,
    "sciana": roshambo,
    "schody": reflex,
    "krzeslo": timebomb,
    "robot": fight,
    "rapier": "Wkładasz cienki miecz między szparę w drzwiach. O dziwo po chwili machania słyszysz lekkie upadek i drzwi są otwarte. Po drugiej stronie widzisz LINĘ która trzymała drzwi. Ten pokój wygląda na ARCHIWUM.",
    "drzwi": "Nie wiesz jak nawet zacząć je otwierać, czysta siła tu nic nie zdziała przy takiej masie"

}

f = open("level_2.dat", "wb")
pickle.dump(rooms,f)
pickle.dump(use,f)
