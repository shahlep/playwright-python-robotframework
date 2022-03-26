*** Settings ***
Documentation    Suite description
Library         ../Library/PyLib/PlaywrightCore.py

Suite Setup         launch browser   CHROMIUM
Suite Teardown      close browser

Test Setup          open application
Test Teardown       close application
