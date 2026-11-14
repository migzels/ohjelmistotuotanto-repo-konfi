*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle222
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  username=vi  password=koiruli22
    Output Should Contain  Username has to consist only of letters(a-z) and be atleast 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  username=isoville!  password=koiruli22
    Output Should Contain  Username has to consist only of letters(a-z) and be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  username=ville  password=kissa22
    Output Should Contain  Password has to be atleast 8 characters long and contain atleast 1 non-letter character

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  username=ville  password=koirulionihana
    Output Should Contain  Password has to be atleast 8 characters long and contain atleast 1 non-letter character
