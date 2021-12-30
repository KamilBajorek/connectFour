6.	Cztery w rzędzie (https://en.wikipedia.org/wiki/Connect_Four)
Link do repozytorium Github: https://github.com/KamilBajorek/connectFour

Opis zadania
o	Okno wyswietlające siatkę 7 kolumn x 6 wierszy, przycisk nad każdą kolumną, informację "Tura gracza 1" lub ''Tura gracza 2", przycisk do resetowania gry oraz rozwijalną listę wyboru reguł gry.
o	Początkowo pola siatki są puste.
o	Gracze na zmianę wrzucają monety do wybranych przez siebie kolumn.
o	Pola w których jest moneta gracza 1 są czerwone, pola z monetami gracza 2 są żółte (tkinter, Canvas, http://stackoverflow.com/a/12254442).
o	Gracze wybierają kolumną klikając przycisk nad nią.
o	Wygrywa gracz który pierwszy ustawi cztery monety w linii (poziomo, pionowo lub po skosie).
o	Gdy gra się kończy, wyświetlane jest okienko z napisem "Wygrał gracz 1" lub "Wygrał gracz 2", zależnie kto wygrał grę. Możliwe jest zresetowanie planszy bez zamykania głównego okna.
o	Reprezentacja reguł gry ma być realizowana poprzez hierarchię klas. Klasa bazowa definiuje między innymi funkcję wirtualną ktoWygral() nadpisywaną w klasach pochodnych. Realizowane powinny być przynajmniej dwa zestawy reguł, jako dwie klasy pochodne.

Testy
1.	Wykonanie po dwa ruchy przez każdego z graczy - monety spadają na dół pola gry lub zatrzymują się na już wrzuconym żetonie.
2.	Utworzenie pionowej linii monet przez jednego gracza - oczekiwana informacja o jego wygranej.
3.	Utworzenie poziomej linii monet przez drugiego gracza - oczekiwana informacja o jego wygranej.
4.	Utworzenie skośnej linii przez dowolnego gracza - oczekiwana informacja o jego wygranej.
5.	Zapełnienie pola gry tak, że żaden gracz nie ułożył linii - oczekiwana informacja o remisie.
6.	Ułożenie linii dłuższej niż 4 przez jednego z graczy - oczekiwana informacja o jego wygranej.
[c][c][c][ ][c][c][c]
[ż][ż][ż][ ][ż][ż][ż] <- w następnym ruchu gracz żółty wrzuci monetę w środkową kolumnę.
7.	Próba wrzucenia monety do zapełnionej kolumny - oczekiwana informacja o błędzie.