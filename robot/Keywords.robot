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
    ${výstup}=    Run    python ../scripts/pycech.py    ${arg}
    [Return]    ${výstup}

meno dlžníka
    meno    --name

dlžník ${dlžník} si požičia ${dlh}
    [Arguments]    ${dlžník}    ${suma}
    ${výstup}=    cech    --name ${dlžník} --take ${suma}
    [Return]    ${výstup}

dlžník ${dlžník} vráti ${dlh}
    [Arguments]    ${dlžník}    ${suma}
    ${výstup}=    cech    --name ${dlžník} --return ${suma}
    [Return]    ${výstup}

dlžník ${dlžník} má dlh
    [Arguments]    ${dlžník}
    ${výstup}=    cech    --name ${dlžník}
    [Return]    ${výstup}

dlžník ${džník} by mal mať dlh ${suma}
    ${dlh}=    dlžník ${dlžník} má dlh    ${džník}
    Should Be Equal    ${dlh}    ${suma}

dlžník ${džník} nie je v zozname
    ${dlh}=    dlžník ${dlžník} má dlh    ${džník}
    Should Be Empty    ${dlh}

dlžník ${džník} je v zozname
    ${dlh}=    dlžník ${dlžník} má dlh    ${džník}
    Should Not Be Empty    ${dlh}
