import pyautogui
import time

telaLarguraX, telaAlturaY = pyautogui.size()

pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write('cmd')
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)

pyautogui.write('start https://www.google.com/intl/pt-BR/chrome/')
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)

pyautogui.moveTo(x=1800, y=15)
time.sleep(1)

pyautogui.click()
time.sleep(1)

pyautogui.write('start https://store.steampowered.com/about/')
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)

pyautogui.moveTo(x=1800, y=15)
time.sleep(1)

pyautogui.click()
time.sleep(1)

pyautogui.write('start https://store.epicgames.com/pt-BR/')
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)

pyautogui.moveTo(x=1800, y=15)
time.sleep(1)

pyautogui.click()
time.sleep(1)

pyautogui.write('start https://code.visualstudio.com/')
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)

pyautogui.moveTo(x=1800, y=15)
time.sleep(1)

pyautogui.click()
time.sleep(1)