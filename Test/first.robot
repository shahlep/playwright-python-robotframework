*** Settings ***
Documentation    Suite description
Library         ../Library/PyLib/PlaywrightCore.py

Suite Setup         launch browser   CHROMIUM
Suite Teardown      close browser

Test Setup          open application
Test Teardown       close application

*** Test Cases ***
My first test case
    log     "This is first test case"
    take screenshot

My second test case
    log     "This is second test case"
    take screenshot