import time 
import mss
from pynput.keyboard import Key, Controller, Listener

controller = Controller()

arr = []

def on_press(key):
    if hasattr(key, 'char'):
        arr.insert(0, key.char)

l = Listener(on_press=on_press)
l.start()

PIXEL_START   = (151, 662)
PIXEL_CAR     = (382, 1015)
COR_START     = (4, 4, 5)
COR_CAR_FOUND = (255, 255, 255)
TOLERANCIA    = 20

time.sleep(2)

def get_color(sct, x, y):
    monitor = {"top": y, "left": x, "width": 1, "height": 1}
    img = sct.grab(monitor)
    b, g, r = img.pixel(0, 0)[:3]
    return (r, g, b)

def match(sct, x, y, esperado):
    atual = get_color(sct, x, y)
    return all(abs(a - e) <= TOLERANCIA for a, e in zip(atual, esperado))

def press(key, wait=0.3):
    controller.press(key)
    controller.release(key)
    time.sleep(wait)

with mss.MSS() as sct:
    while True:

        # Aguarda tela de busca antes de fazer qualquer coisa
        while True:
            if match(sct, *PIXEL_START, COR_START):
                break
            time.sleep(0.5)

        press(Key.enter, 1)  # abre busca e espera carregar
        press(Key.enter, 1)  # confirma e espera resultado

        if match(sct, *PIXEL_CAR, COR_CAR_FOUND):
            print("Carro encontrado! Comprando...")
            press('y',       0.2)
            press(Key.down,  0.4)
            press(Key.enter, 0.4)
            press(Key.enter, 0)
            time.sleep(6)
            press(Key.enter, 1)
            press(Key.esc,   1)
            press(Key.esc,   1)  # espera 1s para garantir que voltou à busca
        else:
            print("Sem carro. Voltando...")
            press(Key.esc, 1.0)  # espera 2s para garantir que voltou à busca
