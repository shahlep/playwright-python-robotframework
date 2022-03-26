*** Settings ***
Documentation    Suite description
Library         ../Library/PyLib/PlaywrightCore.py

Suite Setup         launch browser   CHROMIUM
Suite Teardown      close browser
