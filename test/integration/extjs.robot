*** Settings ***
Resource    ../resource.txt
Library     ExtJSLibrary

*** Variables ***
${Cell Editing}=  http://dev.sencha.com/deploy/ext-4.0.1/examples/grid/cell-editing.html
${Pop Up}=     Ext.ComponentQuery=window[hidden=false]
${OK Button}=  ${Pop Up} button[hidden=false]
${First Cell}=  Ext.DomQuery=*[class*=x-grid-table]/tbody/tr:nth(2)/td
${Cell Input}=  Ext.DomQuery=*[class*=x-grid-editor] [class*=x-form-focus]
${ENTER}=  \\13

*** Test Cases ***
Accept Store Dialog
    [Setup]  Go To  ${Cell Editing}
    Wait Until Ext Is Ready
    Wait Until Page Contains Element  ${Pop Up}
    Click Element  ${Ok Button}
    Page Should Not Contain Element  ${Pop Up}
