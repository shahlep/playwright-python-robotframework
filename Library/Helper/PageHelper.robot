*** Settings ***
Documentation    This is page helper file
Library          ../Page/Menu.py
Resource         ../Helper/CommonHelper.robot
Library         ../Page/FileUpload.py

*** Keywords ***
Menu.Navigate Menu For Input Forms
    [Arguments]    ${secondary_menu_item_name}
    ${page}     get page handle
    navigate menu item      ${page}    'Input Forms'     ${secondary_menu_item_name}

Menu.Navigate Menu For Tables
    [Arguments]    ${secondary_menu_item_name}
    ${page}     get page handle
    navigate menu item    ${page}  'Table'     ${secondary_menu_item_name}

Menu.Navigate Menu For Alerts
    [Arguments]    ${secondary_menu_item_name}
    ${page}     get page handle
    navigate menu item      ${page}    'Alerts & Modals'     ${secondary_menu_item_name}

# File upload try
FileUpload.Upload File In Silent Mode
    [Arguments]     ${filepath}
    ${page}     get page handle
    silent upload file     ${page}     ${filepath}
    ${name}   get uploaded file name    ${page}
    Log    ${name}



