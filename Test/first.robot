*** Settings ***
Documentation    Suite description
Resource        ../Library/Helper/CommonHelper.robot
Resource        ../Library/Helper/PageHelper.robot

Suite Setup         launch firefox browser
Suite Teardown      quit opened browser

Test Setup          open the application
Test Teardown       close the application

*** Test Cases ***
My first test case
    log     "This is first test case"
    menu.navigate menu for input forms    'Simple Form Demo'

My second test case
    log     "This is second test case"
    menu.navigate menu for tables    'Table Pagination'

My second third case
    log     "This is third test case"
    menu.navigate menu for alerts    'Bootstrap Alerts'