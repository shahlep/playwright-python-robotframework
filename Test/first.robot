*** Settings ***
Documentation    Suite description
Resource        ../Library/Helper/CommonHelper.robot

Suite Setup         launch chromium browser
Suite Teardown      quit opened browser

Test Setup          open the application
Test Teardown       close the application

*** Test Cases ***
My first test case
    log     "This is first test case"
    take screenshot

My second test case
    log     "This is second test case"
    take screenshot