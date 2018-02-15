# pycech
náučný testovací program

## O programe
Cielom programu je vytvoriť zoznam dlžníkov krčmárovi. (Sekera už nežije, borg umrel, kto nemá peniaze, nech nepije). Do zoznamu sa zapíše meno dlžníka a jeho dlh. Po je jeho splacení je dlžník zo zoznamu vymazaný.

## Funkčnost
Pri spustení sa vypíše list všetkých dlžníkov.
```
pycech.py --status
```
Výpis konkrétneho dlznika
```
pycech.py --name <meno_dlznika>
```
Odčítanie dlhu konkrétnemu dlžníkovi.
```
pycech.py --name <meno_dlznika> --returns <amout_of_money>
```
Pridanie dlhu konkrétnemu dlžníkovi.
```
pycech.py --name <meno_dlznika> --takes <amout_of_money>
```
Zmazanie cechu.
```
pycech.py --clear
```
