import sqlite3

conn = sqlite3.connect('kino_miasto.db')
cursor = conn.cursor()

try:
    cursor.execute('''
        CREATE TABLE kino (
            id INTEGER PRIMARY KEY,
            nazwa TEXT,
            adres TEXT
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE sala (
            id INTEGER PRIMARY KEY,
            kino_id INTEGER,
            numer TEXT,
            wielkosc TEXT,
            FOREIGN KEY (kino_id) REFERENCES kino(id)
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE seans (
            id INTEGER PRIMARY KEY,
            sala_id INTEGER,
            film_id INTEGER,
            data TEXT,
            godzina TEXT,
            FOREIGN KEY (sala_id) REFERENCES sala(id),
            FOREIGN KEY (film_id) REFERENCES film(id)
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE film (
            id INTEGER PRIMARY KEY,
            opis_id INTEGER,
            nazwa TEXT,
            kategoria TEXT,
            kategoria2 TEXT,
            premiera TEXT,
            czas TEXT,
            produkcja TEXT,
            rezyser TEXT,
            obsada TEXT,
            nazwa_jpg TEXT,
            FOREIGN KEY (opis_id) REFERENCES opis(id)
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE opis (
            id INTEGER PRIMARY KEY,
            opisf TEXT
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE uzytkownik (
            id INTEGER PRIMARY KEY,
            login TEXT,
            haslo TEXT,
            email TEXT
        )
    ''')
except Exception as e:
    pass

try:
    cursor.execute('''
        CREATE TABLE rezerwacja (
            id INTEGER PRIMARY KEY,
            data TEXT,
            rzad TEXT,
            miejsce TEXT,
            uzytkownik_id INTEGER,
            seans_id INTEGER,
            FOREIGN KEY (uzytkownik_id) REFERENCES uzytkownik(id),
            FOREIGN KEY (seans_id) REFERENCES seans(id)
        )
    ''')
except Exception as e:
    pass


# 2 kina, rozne lokalizacje
kina = [
            (1, "Kino Miasto", "Warszawa ul. Fiołkowa 13"),
            (2, "Kino Miasto", "Warszawa ul. Różana 7")
]

try:
    cursor.executemany("INSERT INTO kino VALUES (?,?,?)", kina)
except Exception as e:
    pass

# kazde kino ma 2 sale
sale = [
            (1, 1, "1", "duza"),
            (2, 1, "2", "mala"),
            (3, 2, "1", "duza"),
            (4, 2, "2", "mala")
]

try:
    cursor.executemany("INSERT INTO sala VALUES (?,?,?,?)", sale)
except Exception as e:
    pass

seanse = [
            (1, 1, 8, "22.01.2024", "14.00"),
            (2, 1, 7, "22.01.2024", "17.00"),
            (3, 1, 3, "22.01.2024", "20.00"),
            (4, 2, 6, "22.01.2024", "14.00"),
            (5, 2, 6, "22.01.2024", "17.00"),
            (6, 2, 7, "22.01.2024", "20.00"),
            (7, 3, 8, "22.01.2024", "14.00"),
            (8, 3, 7, "22.01.2024", "17.00"),
            (9, 3, 3, "22.01.2024", "20.00"),
            (10, 4, 6, "22.01.2024", "14.00"),
            (11, 4, 6, "22.01.2024", "17.00"),
            (12, 4, 7, "22.01.2024", "20.00"),

            (13, 1, 8, "23.01.2024", "14.00"),
            (14, 1, 4, "23.01.2024", "17.00"),
            (15, 1, 3, "23.01.2024", "20.00"),
            (16, 2, 6, "23.01.2024", "14.00"),
            (17, 2, 3, "23.01.2024", "17.00"),
            (18, 2, 7, "23.01.2024", "20.00"),
            (19, 3, 8, "23.01.2024", "14.00"),
            (20, 3, 4, "23.01.2024", "17.00"),
            (21, 3, 3, "23.01.2024", "20.00"),
            (22, 4, 6, "23.01.2024", "14.00"),
            (23, 4, 3, "23.01.2024", "17.00"),
            (24, 4, 7, "23.01.2024", "20.00"),

            (25, 1, 8, "24.01.2024", "14.00"),
            (26, 1, 9, "24.01.2024", "17.00"),
            (27, 1, 4, "24.01.2024", "20.00"),
            (28, 2, 6, "24.01.2024", "14.00"),
            (29, 2, 1, "24.01.2024", "17.00"),
            (30, 2, 3, "24.01.2024", "20.00"),
            (31, 3, 8, "24.01.2024", "14.00"),
            (32, 3, 9, "24.01.2024", "17.00"),
            (33, 3, 4, "24.01.2024", "20.00"),
            (34, 4, 6, "24.01.2024", "14.00"),
            (35, 4, 1, "24.01.2024", "17.00"),
            (36, 4, 3, "24.01.2024", "20.00"),

            (37, 1, 10, "25.01.2024", "14.00"),
            (38, 1, 9, "25.01.2024", "17.00"),
            (39, 1, 4, "25.01.2024", "20.00"),
            (40, 2, 8, "25.01.2024", "14.00"),
            (41, 2, 2, "25.01.2024", "17.00"),
            (42, 2, 1, "25.01.2024", "20.00"),
            (43, 3, 10, "25.01.2024", "14.00"),
            (44, 3, 9, "25.01.2024", "17.00"),
            (45, 3, 4, "25.01.2024", "20.00"),
            (46, 4, 8, "25.01.2024", "14.00"),
            (47, 4, 2, "25.01.2024", "17.00"),
            (48, 4, 1, "25.01.2024", "20.00"),

            (49, 1, 10, "26.01.2024", "14.00"),
            (50, 1, 9, "26.01.2024", "17.00"),
            (51, 1, 2, "26.01.2024", "20.00"),
            (52, 2, 8, "26.01.2024", "14.00"),
            (53, 2, 4, "26.01.2024", "17.00"),
            (54, 2, 4, "26.01.2024", "20.00"),
            (55, 3, 10, "26.01.2024", "14.00"),
            (56, 3, 9, "26.01.2024", "17.00"),
            (57, 3, 2, "26.01.2024", "20.00"),
            (58, 4, 8, "26.01.2024", "14.00"),
            (59, 4, 4, "26.01.2024", "17.00"),
            (60, 4, 4, "26.01.2024", "20.00"),

            (61, 1, 5, "27.01.2024", "14.00"),
            (62, 1, 2, "27.01.2024", "17.00"),
            (63, 1, 1, "27.01.2024", "20.00"),
            (64, 2, 10, "27.01.2024", "14.00"),
            (65, 2, 9, "27.01.2024", "17.00"),
            (66, 2, 2, "27.01.2024", "20.00"),
            (67, 3, 5, "27.01.2024", "14.00"),
            (68, 3, 2, "27.01.2024", "17.00"),
            (69, 3, 1, "27.01.2024", "20.00"),
            (70, 4, 10, "27.01.2024", "14.00"),
            (71, 4, 9, "27.01.2024", "17.00"),
            (72, 4, 2, "27.01.2024", "20.00"),

            (73, 1, 5, "28.01.2024", "14.00"),
            (74, 1, 5, "28.01.2024", "17.00"),
            (75, 1, 1, "28.01.2024", "20.00"),
            (76, 2, 10, "28.01.2024", "14.00"),
            (77, 2, 9, "28.01.2024", "17.00"),
            (78, 2, 2, "28.01.2024", "20.00"),
            (79, 3, 5, "28.01.2024", "14.00"),
            (80, 3, 5, "28.01.2024", "17.00"),
            (81, 3, 1, "28.01.2024", "20.00"),
            (82, 4, 10, "28.01.2024", "14.00"),
            (83, 4, 9, "28.01.2024", "17.00"),
            (84, 4, 2, "28.01.2024", "20.00")
]
try:
    cursor.executemany("INSERT INTO seans VALUES (?,?,?,?,?)", seanse)
except Exception as e:
    pass

filmy = [
            (1,1,   "Aquaman",                                  "Akcja",        "Sci-Fi",       "19 grudnia 2018",      "2 godz. 23 min.",  "USA, Australia",               "James Wan",                        "Jason Momoa, Amber Heard, Willem Dafoe",                           "aqua.jpg"),
            (2,2,   "Igrzyska Śmierci: Ballada ptaków i węży",  "Akcja",        "Sci-Fi",       "17 listopada 2023",    "2 godz. 37 min.",  "USA",                          "Francis Lawrence",                 "Tom Blyth, Rachel Zegler, Viola Davis",                            "ballada.jpg"),
            (3,3,   "Barbie",                                   "Dramat",       "Komedia",      "21 lipca 2023",        "1 godz. 54 min.",  "USA, Kanada",                  "Greta Gerwig",                     "Margot Robbie, Ryan Gosling, America Ferrera",                     "barbie.jpg"),
            (4,4,   "Oppenheimer",                              "Biograficzny", "Dramat",       "21 lipca 2023",        "3 godz.",          "USA, Wielka Brytania",         "Christopher Nolan",                "Cillian Murphy, Emily Blunt, Matt Damon",                          "oppenheimer.jpg"),
            (5,5,   "Spider-Man: Poprzez multiwersum",          "Animacja",     "Akcja",        "2 czerwca 2023",       "2 godz. 20 min.",  "USA",                          "Joaquim Dos Santos, Kemp Powers",  "Shameik Moore, Hailee Steinfeld, Brian Tyree Henry",               "spider-man.jpg"),
            (6,6,   "Świąteczna niespodzianka",                 "Familijny",    "Świąteczny",   "9 grudnia 2022",       "1 godz. 18 min.",  "Norwegia",                     "Andrea Eckerbom",                  "Marte Klerck-Nilssen, John F. Brungot, Lene Kongsvik Johansen",    "swieta.jpg"),
            (7,7,   "Szybcy i wściekli 10",                     "Akcja",        " ",            "19 maja 2023",         "2 godz. 21 min.",  "USA, Chiny, Japonia",          "Louis Leterrier",                  "Vin Diesel, Michelle Rodriguez, Jason Momoa",                      "szybcy.jpg"),
            (8,8,   "Trolle 3",                                 "Animacja",     "Familijny",    "1 grudnia 2023",       "1 godz. 31 min.",  "USA",                          "Walt Dohrn",                       "Anna Kendrick, Justin Timberlake, Camila Cabello",                 "trolle.jpg"),
            (9,9,   "Wonka",                                    "Fantasy",      "Komedia",      "14 grudnia 2023",      "1 godz. 53 min.",  "USA, Kanada, Wielka Brytania", "Paul King",                        "Timothée Chalamet, Calah Lane, Keegan-Michael Key",                "wonka.jpg"),
            (10,10, "Między nami żywiołami",                    "Animacja",     "Przygodowy",   "14 lipca 2023",        "1 godz. 41 min.",  "USA",                          "Peter Sohn",                       "Leah Lewis, Mamoudou Athie, Ronnie Del Carmen",                    "zywioly.jpg")
]

opisy = [
            (1, "Arthur Curry niechętnie stara się przejąć władzę w podwodnym królestwie Atlantydy, żeby zapobiec wojnie z ludźmi żyjącymi na powierzchni."),
            (2, "Młody Coriolanus Snow zostaje mentorem trybutki z Dwunastego Dystryktu podczas 10. Głodowych Igrzysk. Od tego momentu losy jego i Lucy Gray Baird nierozerwalnie się splatają."),
            (3, "Barbie, która żyje w idealnym bajkowym świecie przechodzi kryzys egzystencjalny."),
            (4, "Historia amerykańskiego naukowca J. Roberta Oppenheimera i jego roli w stworzeniu bomby atomowej."),
            (5, "Miles trafia do multiwersum, w którym spotyka innych Spider-Manów. Sam musi odkryć, co dla niego oznacza bycie bohaterem oraz jak uratować tych, na których mu zależy."),
            (6, "Nie wszystkie misie zapadają w zimowy sen. A w tym, jednym naprawdę można się zakochać, szczególnie że, potrafi mówić ludzkim głosem. I to nie tylko w Wigilię. Marianna zauważa misia na loterii fantowej podczas jarmarku świątecznego. Od początku czuje z nim niesamowitą więź. Ale niestety dla niej, nasz miś ma inne plany gdyż pragnie aby wygrał go ktoś bogaty. Taki ktoś kto nauczy go wszystkiego o świecie ludzi. Teraz Marianna ma czas tylko do Świąt aby przekonać misia o tym co tak naprawdę jest w życiu ważne."),
            (7, "W ciągu wielu misji i wbrew przeciwnościom losu Dom Toretto i jego rodzina przechytrzyli i prześcignęli każdego wroga na swojej drodze. Teraz muszą zmierzyć się z najgroźniejszym przeciwnikiem, z jakim kiedykolwiek mieli do czynienia."),
            (8, "Po dwóch filmach prawdziwej przyjaźni i flirtowania, Poppy i Mruk są teraz oficjalnie parą! Poppy odkrywa, że Mruk ma sekretną przeszłość. Był kiedyś częścią fenomenalnego boysbandu, BroZone, wraz ze swoimi czterema braćmi: Floydem, Johnem Dory, Sprucem i Clayem. BroZone rozpadł się, a Mruk od tamtej pory nie widział swoich braci. Mruk i Poppy wyruszają w pełną emocji podróż, aby zjednoczyć braci."),
            (9, "Młody Willy Wonka poznaje Oompa-Loompas w czasie jednej ze swoich przygód."),
            (10, "Para przeciwnych sobie żywiołów Ember i Wade wspólnie ratuje miasto przed zagładą.")
]

try:
    cursor.executemany("INSERT INTO opis VALUES (?,?)", opisy)
except Exception as e:
    pass

try:
    cursor.executemany("INSERT INTO film VALUES (?,?,?,?,?,?,?,?,?,?,?)", filmy)
except Exception as e:
    pass

uzytkownicy = [
            (1, "user", "tajnehaslo1", "user1@gmail.com")
]

try:
    cursor.executemany("INSERT INTO uzytkownik VALUES (?,?,?,?)", uzytkownicy)
except Exception as e:
    pass

# sprawdzenie
cursor.execute("SELECT * FROM kino")
print(cursor.fetchall())
cursor.execute("SELECT * FROM sala")
print(cursor.fetchall())
cursor.execute("SELECT * FROM seans")
print(cursor.fetchall())
cursor.execute("SELECT * FROM film")
print(cursor.fetchall())
cursor.execute("SELECT * FROM opis")
print(cursor.fetchall())
cursor.execute("SELECT * FROM uzytkownik")
print(cursor.fetchall())

conn.commit()
conn.close()
