import pyautogui
import time

pyautogui.press('space') 

#pressionar e soltar um tecla do teclado
pyautogui.keyDown('enter')
pyautogui.keyDown('enter')

#escreve um texto
pyautogui.write('hello world')

#combinação de tecla
pyautogui.hotkey('alt', 'f4')
