import psutil as psutil
import pyautogui
import time
import os
from pywinauto.application import Application

print("1. Closing all background running PowerBI instances")
# Kill running PBI
PROCNAME = "PBIDesktop.exe"
for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()

# Start PBI and open the workbook
print("2. Opening Finance Dashboard")
try:
    os.startfile(r'C:\Users\ssahu\Desktop\Power BI\My Visualisations\Finance_Visualisation.pbix')
except Exception:
    print('File Not Found')

app = Application(backend = 'uia').connect(path = PROCNAME)
win = app.window(title_re = '.*Power BI Desktop')
time.sleep(10)
# win.wait("enabled", timeout = 300)
# win.Save.wait("enabled", timeout = 300)
win.set_focus()

time.sleep(10)
# print(pyautogui.position())
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.hotkey('alt', 'h')
# pyautogui.hotkey('h')
time.sleep(1)
pyautogui.hotkey('q')
time.sleep(1)
pyautogui.keyDown('down')
time.sleep(1)
pyautogui.keyDown('up')
pyautogui.hotkey('enter')
time.sleep(4)
pyautogui.hotkey('alt', 'h')
time.sleep(3)
pyautogui.hotkey('q')
time.sleep(1)
pyautogui.press('tab', presses=2)
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('del')
print("3. Deleted Old connection details in advanced Editor")

# Opening Notepad having new connection
print("4. Opening Notepad having new connection details")
NOTEPROC = "Notepad.exe"
os.startfile(r'C:\Users\ssahu\Desktop\Power BI\My Visualisations\connection.txt')
app = Application(backend = 'uia').connect(path = NOTEPROC)
win1 = app.window(title_re = '.*Notepad')
win1.set_focus()
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
win1.close()

# Setting focus back on PowerBI
# win = app.window(title_re = '.*Power BI Desktop')
# time.sleep(5)


# Changing Connection String in PowerBi

# Saving new connection string
pyautogui.hotkey('alt', 'tab')
# pyautogui.hotkey('tab')
# pyautogui.hotkey('enter')
pyautogui.hotkey('alt', 'tab')
# pyautogui.hotkey('tab')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

# Refreshing Table
pyautogui.hotkey('alt', 'h')
pyautogui.hotkey('r')
time.sleep(1)
pyautogui.hotkey('enter')

# Close and Apply
pyautogui.hotkey('alt', 'h')
pyautogui.hotkey('c')
time.sleep(1)
pyautogui.hotkey('enter')
win.set_focus()
print("5. Added new connection details and Applied Changes")

# Refresh
print("6. Refreshing")
pyautogui.hotkey('alt', 'h')
pyautogui.hotkey('r')
pyautogui.hotkey('ctrl', 's')
