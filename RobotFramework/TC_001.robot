*** Settings ***
Library     Selenium2Library
Library     SeleniumLibrary

*** Variables ***
${URL}  http:google.com
${Browser}  Chrome

*** Test Cases ***
TC_001
    SeleniumLibrary.Open Browser  ${URL}  ${Browser}
    SeleniumLibrary.maximize browser window
    SeleniumLibrary.close browser

TC_002
    SeleniumLibrary.Open Browser  ${URL}  ${Browser}
    SeleniumLibrary.close browser
    
