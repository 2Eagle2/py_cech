*** Settings ***
Library           OperatingSystem

*** Keywords ***
vyprázdníme cech
    cech    --clear

zoznam by mal byť prázdny
    ${výstup} =    cech    --status
    Should Be Equal    ${výstup}    ${EMPTY}

cech
    [Arguments]    ${arg}
    ${výstup} =    Run    python ../scripts/cech.py ${arg}
    [Return]    ${výstup}
