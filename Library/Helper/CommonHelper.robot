*** Settings ***
Documentation    Common stuffs
Library          ../PyLib/PlaywrightCore.py


*** Keywords ***
Launch Chromium Browser
    launch browser    browser_name=chromium

Launch Firefox Browser
    launch browser    browser_name=firefox

Launch Webkit Browser
    launch browser    browser_name=webkit

Quit Opened Browser
    close browser

Open the application
    open application

Close the application
    close application

Get Page Handle
    ${page_handle}      get page object
    [Return]            ${page_handle}

