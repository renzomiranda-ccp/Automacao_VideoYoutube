import pyautogui as pa
import time
from abrir_navegador import abrir_navegador

pesquisas = [
    "curso python",
    "python automação",
]
pa.PAUSE = 1
def pesquisar_youtube(pesquisa):

        abrir_navegador()
        pa.hotkey("ctrl","l")
        pa.write('youtube.com')
        pa.press('tab')
        pa.write(pesquisa)
        pa.press('enter')

        pa.sleep(1.5)

        pa.click(x=657, y=754)


for pesquisa in pesquisas:
    pesquisar_youtube(pesquisa)




