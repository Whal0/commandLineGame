from games import *
from Engine import *
rooms = {
    1: {
        "ID": 1,
        "name": "Przedsionek Nieba",
        "opis": "Przy małej przerwie w szkle widzisz mały IDENTYFIKATOR – Dr. Samuel Hejden. Po przeciwnej stronie widzisz drzwi ze szklanym PANELem emanującym lekkie niebiskie światło",
        "discovery": "W środku jest mały pokój, jabky poczekalnia, na ścianach jest sporo elektroniki, parę krzeseł jak i oszklone biurko.",
        "pickups": ["identyfikator"],
        "interest": ["rozpiska", "ekran"],
        "desc": ["Widzisz rozpiskę dat, ale obok niej jakby dziecience rysunki",
                 "Pęknięty ekran przedstawiał kiedyś piękną grafikę złotych chmur tytułem \"Witaj w Igle\",, teraz z brakującymi kawałkami wygląda o wiele mrocznej. "],
        "actions": ("rozpiska", "identyfikator", "cegla", "srubokret"),
        "exits": {"polnoc": 2, },
        "visited": True,
        "quest": False,
        "success": "Zadowolony rozgrywką z samym sobą odchylasz się od teraz maniacznie pobazgranej tablicy",
        "fail": "Przegrałeś we własnej wyobraźni, ten fakt trochę Cię boli"
    },
    2: {
        "ID": 2,
        "name": "Serce Arkadii",
        "opis": "Szkło pokrywające wszystkie pokoje odbija je dając całemu wnętrzu lekko niebieski odcień. Widzisz ich dziesiątki w góre wieży, większość nienaruszonych. Na swoim obecnym piętrze niedaleko widzisz EKRAN, za tym widzisz WINDĘ. Niedaleko widzisz TERMINAL",
        "discovery": " W środku widzisz coś nie bywałego, cała wieża jest bez własnego oświetlenia, jedyne światło pochodzi od różnych aparatur i urządzeń. Mimo to musisz zmrużyć oczy przyzwyczajając się do światła. Na kolumnie przechodzącej przez środek wieży widzisz wyrytę: Serce Arkadii",
        "pickups": [],
        "interest": ["ekran", "winda"],
        "desc": ["W windzie widzisz 3 przyciski:\nPółnoc-Generator\nWschód- Warsztat\n",
                 "Ekran błyska na czerwony:\n BŁĄD, stabilność generatora krytyczna, nadpisanie protokołu 0x20 \nStan hibarnacji: aktywny\n Trzeba będzie znaleźć ten generator jeżeli chcę się stąd wydostać"],
        "actions": ("terminal",),
        "exits": {"wschod": 3,
                  "polnoc": 5,
                  "poludnie": 1},
        "visited": False,
        "quest": False,
        "success": "Udało Ci się złamać hasło na ekranie widzisz instrukcje do jakiegos generatora",
        "fail": "bbbbbbbbb"
    },
    3: {
        "ID": 3,
        "name": "Warsztat Technokraty",
        "opis": "Oglądając się uważnie wnętrzu widzisz jakiś DZIENNIK, obok jakieś APARATURY. stertą papierów, szkła i mebli nic ta nie zwraca uwagi jak ciągle obecna MGŁA tworząca atmosferę zaświatów, nie jesteś pewny czy to przez tą windę czy już tak masz dość tego miasta",
        "discovery": "Naciskając warsztat czujesz jak twój żołądek upada i czujesz ze przesuwasz się w dobrym kierunku, jakimś cudem bokiem. Po otwarciu drzwi widzisz jakieś laboratorium, cała podłoga jest pokryta w kawałkach szkła różnych wartości, z za SZYBY naprzeciw widzisz główną kolumnę wieży. Z jeden części pomieszczenia za szafkami wydobywa się MGŁA ",
        "pickups": ["dziennik", "klucz"],
        "interest": ["szyba", "mgła", "aparatura"],
        "desc": [
            "Teraz z lotu ptaka widzisz główną komorę Igły. Bez oślepiających odbić wydaję się dziwnie ciemna. Patrząc do góry cała wieża wewnątrz była pokryta szkłem. Ciekawe w jakim celu.",
            "Temperatura spada im bliżej jesteś źródła tej mgły. Gdy wychodzisz za szafki widzisz 3 miejsca na jakieś szklane cylindry, 2 z nich są rozbitę, na 3 jest kartka: KAPSUŁA bb-1946 z niej emanuje ciągle mroźny wiatr",
            "Na biurku obok konstrukcji leży parę wiolek. Sama maszyna ma długą lupę wycelowaną w mały kawałek szkła, nie wiesz do czego może służyć"],
        "actions": ("kapsula",),
        "exits": {"zachod": 2,
                  "polnoc": 4},
        "visited": False,
        "quest": False,
        "success": "Wielki tytan opada na kolana, wokół jego szyi jest zawieszony KLUCZ ",
        "fail": "Ostatnią rzecz jaką słyszysz jest pisk wiertła, przeszywające twoje serce. Tracisz przytomność"
    },
    4: {
        "ID": 4,
        "name": "Fabryka Plazmidów",
        "opis": "Widzisz droge powrotną do głównej komory na północ.\nIdać dalej, zauważasz źródło dziwieku. Metalowe pudło na jedyym kółku o jednym oku próbuje wstać.\n Chyba Cię zauważa bo mówi: Hejjjj nazywam się: K L U B podejdz tuuu",
        "discovery": "Przechodzisz przez tafle I stajesz w ciemnym pokoju, widzisz setki pustych pojemników na plazmidy na taśmach produkcyjnych. W ciemnośći słyszysz gruchotanie metalu",
        "pickups": ["oko",],
        "interest": ["klub"],
        "desc": ["Klub zaczyna:  hej dawno tu-u-u-u nikogo nie było może runda w KARTY?", ],
        "actions": ("karty", "cegla"),
        "exits": {"polnoc": 2,},
        "visited": False,
        "quest": False,
        "success": "Z-z-z-ostałem pokonany, no coż musisz umrzeć, Klub podnosi się, po czym…. upada jego OKO wyskakuje z miejsca na ziemie, musiał się usmażyć",
        "fail": "HAHAHAH p-p-przegrać na maszyne. Czego Klub nie wiedział to że stół jest miedziany a on wydziela elektryczność z kabli gdy się śmieje. Zostajesz upokorzony i porażony"
    },
    5: {
        "ID": 5,
        "name": "Generator",
        "opis": "Wchodząc dalej oprócz GENERATORA widzisz ich wersje starego PROJEKTORA filmowego. Zauważasz też że wokół głównej kolumny jest ogromna PRZEPAŚĆ z wąskim metalowym przejściem do KONSOLI",
        "discovery": "Naciskając północ o po zamknięciu drzwi czujesz że spadasz, szybko. Czujesz ciarki na plecach, przygotowujesz się na gorsze. Winda nagle staje, powoli otwierasz swoje oczy. Przez otwarte drzwi widzisz wielką żelazną kolumnę na szczycie widzisz masywne miedziane pierścienie, zakurzony napis na ścianie upewnia Cię o twoim położeniu, trafiłeś do GENERATOR ",
        "pickups": [],
        "interest": ["generator", "przepasc", "projektor"],
        "desc": [
            "Wielka konstrukcja odpowiada na parę pytań jak to miejsce trzymało się w powietrzu, obok nich są też kontenery z rurami podpiętymi do głównej, pewnie źródło mocy czyste plazmidy",
            "Patrząc w dół nie widzisz dnia, rzucając kamień w dół nie słyszysz jak się odbija. Spadek nie brzmi dobrze",
            "Tasmą jest zniszczona, na oświetlonym ekranie został jeden obraz nagrania z miasta, w oddali widać całość posągu z Agory. Miasto wygląda żywo"],
        "actions": ("konsola",),
        "exits": {"poludnie": 2},
        "visited": False,
        "quest": False,
        "success": "jakimś cudem udaje Ci się zatrzymać cokolwiek rozpocząłeś, widzisz zieloną diodę",
        "fail": "Piski stają się bolesne, zanim się orientujesz kończą się, z twoich uszu wypływa krew, nie wiesz co się staje"
    },
}

use = {
    "rozpiska": reflex,
    "karty": blackjack,
    "konsola": roshambo,
    "terminal": fallout,
    "kapsula": fight,
    "identyfikator": "Przykładasz identyfikator do panelu i błyska on na zielono, drzwi zaczynają skrzypieć, twój kompas mówi Ci że dalej prowadzą na północ mimo że nie wydaje się to możliwe, cóż jedyne co zostało to iść dalej",
    "cegla": "drzwi są na słabych zawiasach i możesz kontynuować na północ",
    "srubokret": "rozkrecać zamek i mozesz kontynuowac na północ"
}


f = open("level_3.dat", "wb")
pickle.dump(rooms, f)
pickle.dump(use, f)
