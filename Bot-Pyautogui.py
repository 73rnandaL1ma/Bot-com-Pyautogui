import pyautogui
import time
pyautogui.PAUSE = 2
pyautogui.press ("win")
pyautogui.write ("Netflix")
pyautogui.press ("enter") 
time.sleep (12)

pyautogui.click ( x=1306, y=63 )
pyautogui.click (x=553, y=287)
pyautogui.write ("fernanda.lima.silva")
pyautogui.click (x=734, y=332)
pyautogui.write ("123456")
time.sleep (2)
pyautogui.click (x=659, y=373)


