import os
import pyautogui
import time

    
settingsAndMemberCoord = (134,262)
settingsCoord = (459,684)
deleteCoord = (1000,980)
deleteTextCoord = (1159, 738)
permaDeleteCoord = (1268, 864)
workspaceSettingsCoord = (1414, 651)

# while True:
#     print(pyautogui.position())
def deleteWorkspace():
    #1-aller sur le bon workspace (avec ctrl+3)
    print('1')
    pyautogui.hotkey('ctrl', '4')
    
    time.sleep(4)

    #2-click on 'Settings & Members'
    print('2')
    pyautogui.click(settingsAndMemberCoord[0], settingsAndMemberCoord[1], button='left')
    time.sleep(2)

    #3-Workspace-settings-scroll all the way down
    print('3')
    pyautogui.click(settingsCoord[0], settingsCoord[1], button='left')
    time.sleep(4)
    for i in range(18):
        pyautogui.typewrite(['tab'])

    pyautogui.typewrite(['enter'])
    # pyautogui.scroll(200)           
    time.sleep(2)

    #4- Select 'Delete entire workspace
    print('4')
    pyautogui.click(deleteCoord[0], deleteCoord[1], button='left')
    time.sleep(1)

    #5-Enter text 'Vivi is the most lil bitch'
    print('5')
    pyautogui.click(deleteTextCoord[0], deleteTextCoord[1], button='left')
    pyautogui.typewrite('Vivi is the most lil bitch')

    #6- click 'Permanently delete workspace'
    print('6')
    pyautogui.click(permaDeleteCoord[0], permaDeleteCoord[1], button='left')
    time.sleep(7)

for i in range(30):
    print('step', i)
    deleteWorkspace()