# PyAutoGUI
import pyautogui

pyautogui.FAILSAFE = False #se colacar True ele Não fechara /Uma sefezone

#Captura a largura e altura da sua tela
telaLarguraX, telaAlturaY = pyautogui.size()

#Move o mouse para a posição indicada no parametro x e y
pyautogui.moveTo(telaLarguraX,0)

#Aciona o clique do mouse
pyautogui.click()

