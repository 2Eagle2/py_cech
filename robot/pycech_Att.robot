*** Settings ***
Documentation     - kontrola vzniku uživateľa pri vzniku dlhu pokiaľ neexistuje
...               - kontrola pripisani dlhu pokiaľ uživatel niečo dlží

*** Test Cases ***
TC_prázdny cech
    when cech je prázdny
    given zoznam dlžníkov
    then zoznam by mal byť prázdny

TC_overenie dlhu dlžnika
    given meno
