*** Settings ***
Resource  resources.robot
Suite Setup  Open Browser  http://google.com  ${BROWSER}
Suite Teardown  Close All Browsers
