import pyautogui
import time
from tkinter import Tk

loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\caftex-icon.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)
loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\caftex-start-session.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)
pyautogui.typewrite("tempadmin",0.1)
pyautogui.typewrite(["enter"])
pyautogui.typewrite("Flanagan5",.01)
pyautogui.typewrite(["enter"])
pyautogui.typewrite("KJFLANAGAN",0.1)
pyautogui.typewrite(["enter"])
time.sleep(0.5)
pyautogui.typewrite("pc",0.1)
pyautogui.typewrite(["enter"])
pyautogui.typewrite("password",.01)
pyautogui.typewrite(["enter"])

time.sleep(2)
loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\stock.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)

loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\runtime.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)


loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\reports.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)

loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\user-reports.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)

pyautogui.typewrite(["up"])

loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\cutters.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)

pyautogui.typewrite("-7",0.1)
pyautogui.typewrite(["enter"])
pyautogui.typewrite("-1",0.1)
pyautogui.typewrite(["enter"])
time.sleep(0.2)
pyautogui.typewrite(["enter"])
time.sleep(0.2)
pyautogui.typewrite(["enter"])

loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\dif.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(5)

loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\save-location.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)

save_loc = "C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\"
#C:\Users\patrick.coffey\OneDrive - Flanagan Flooring\Desktop\gui-automation
pyautogui.typewrite(save_loc,0.05)
pyautogui.typewrite(["enter"])
time.sleep(0.5)
loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\save-filename.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)

pyautogui.hotkey('ctrl', 'c')
root = Tk()
copied_var = root.clipboard_get()
root.destroy()
print(copied_var)
#input("Pausing for user to perform checks")

loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\save-button.PNG')
pyautogui.click(pyautogui.center(loc))
#pyautogui.click(pyautogui.center(loc))
time.sleep(5)

loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\caftex-window-focus.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(0.2)
pyautogui.typewrite(["esc"])
time.sleep(0.2)
pyautogui.typewrite(["esc"])
time.sleep(0.2)
pyautogui.typewrite(["esc"])
time.sleep(0.2)
pyautogui.typewrite(["esc"])
time.sleep(0.2)
pyautogui.typewrite(["esc"])
time.sleep(2.5)
loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\exit-yes.PNG')
pyautogui.click(pyautogui.center(loc))
time.sleep(1)
pyautogui.typewrite(["esc"])
time.sleep(1)
loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\close.PNG')
pyautogui.click(pyautogui.center(loc))
#time.sleep(1)
#loc = pyautogui.locateOnScreen('C:\\Users\\patrick.coffey\\OneDrive - Flanagan Flooring\\Desktop\\gui-automation\\tk-close.PNG')
#pyautogui.click(pyautogui.center(loc))

