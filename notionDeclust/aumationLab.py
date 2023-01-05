import os
from pywinauto import application
from pywinauto import keyboard

app = application.Application()
app.start("Notepad.exe")

