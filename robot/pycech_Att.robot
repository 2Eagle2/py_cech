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
    vyprázdníme cech
    dlžník Fero nie je v zozname
    dlžník Miso nie je v zozname

TC_zmazanie dlžnika zo zoznamu
    vyprázdníme cech
    dlžník Fero si požičia 1000
    dlžník Mišo si požičia 1000
    dlžník Fero je v zozname
    dlžník Mišo je v zozname
    dlžník Fero vráti 1000
    dlžník Fero nie je v zozname
    dlžník Mišo je v zozname

TC_odčítanie dlhu
    vyprázdníme cech
    dlžník Fero si požičia 1000
    odcitanie dlhu
    dlžník Fero má dlh

TC_pridanie dlžnika
    vyprázdníme cech
    dlžník ${dlžník} si požičia ${dlh}    Fero    100
    dlh Fero by mal byť ${suma}
