import pyautogui
import time

#Captura de dados da tela
#Captura a largura e altura de sua tela
telaLarguraX, telaAlturaY = pyautogui.size()
print(telaLarguraX, telaAlturaY)

#Captura a posição do mouse
time.sleep(3)
posicao_mouse = pyautogui.position()
print(posicao_mouse)

#verifica se o mouse esta na tela e retornar
#True e False
#parametros: (x,y)
print(pyautogui.onScreen(0,0))

#Sefezone
pyautogui.FAILSAFE = True

#move o mouse
pyautogui.moveTo(x=500, y=1000)

#Move o mouse para uma posição relativa ao mouse // tipo se tiver uma sequencia de click, ele ira apartir da posição do ponteiro 
#parametro (x,y, tempo de espera)
pyautogui.moveRel(0, telaAlturaY, 0.5)

#click padrão
pyautogui.click()

#click personalizado (x,y,tempo, qual Botão left ou r)
pyautogui.click(telaLarguraX, telaAlturaY, 0, button='left')

pyautogui.leftClick()

pyautogui.rightClick()

pyautogui.middleClick() # botão do scroll

pyautogui.doubleClick()

pyautogui.tripleClick()

#click e arasta segurando
pyautogui.mouseDown(x=1435, y=18, button='left')

#levanta o dedo do mouse para soltar o arasta
pyautogui.mouseUp()

#Parametro: (quantidade de scroll)
pyautogui.scroll(100)