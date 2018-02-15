*** Settings ***
Documentation     - kontrola vzniku uživateľa pri vzniku dlhu pokiaľ neexistuje
...               - kontrola pripisani dlhu pokiaľ uživatel niečo dlží

*** Test Cases ***
TC_prázdny cech
    when cech je prázdny
    given zoznam dlžníkov
    then zoznam by mal byť prázdny

TC_overenie dlžnika v zozname
    when meno dlžnika
    given nema ešte cech
    then pridanie do zoznamu

TC_zmazanie dlžnika zo zoznamu
    when meno dlžnika zo zonamu
    given zaplatenie cechu
    then zmazanie dlžnika zo zonamu

TC_odčítanie dlhu
    when meno dlžníka zo zoznamu
    given odčítaj nejakú sumu
    then suma zvyšného dlhu

*** Keywords ***
prázdny zoznam
    status    je prázdny

odčítanie dlhu
    returns

pridanie dlhu
    takes

zmazanie cechu
    clear
