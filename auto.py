import pyautogui as pa
import time

pa.PAUSE = 1
def abrir_navegador():
    pa.press('win')
    pa.write('edge')
    pa.press('enter')
    pa.hotkey("ctrl","l")
    pa.write('youtube')
    pa.press('tab')

abrir_navegador()
pa.write('curso python')
pa.press('enter')
pa.sleep(2)
pa.click(x=657, y=754)