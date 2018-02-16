*** Settings ***
Documentation     - kontrola vzniku uživateľa pri vzniku dlhu pokiaľ neexistuje
...               - kontrola pripisani dlhu pokiaľ uživatel niečo dlží
Library           OperatingSystem
Resource          Keywords.robot

*** Test Cases ***
TC_prázdny cech
    vyprázdníme cech
    zoznam by mal byť prázdny

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
