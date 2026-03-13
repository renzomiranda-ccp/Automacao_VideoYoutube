import pyautogui as pa

pa.PAUSE = 1

def abrir_navegador():
    pa.press('win')
    pa.write('edge')
    pa.press('enter')
