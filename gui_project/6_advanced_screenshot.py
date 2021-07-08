import time
import keyboard
from PIL import ImageGrab

def screenshot():
    cur_time = time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save('image{}.png'.format(cur_time))

keyboard.add_hotkey('F9', screenshot)

keyboard.wait('esc') # 사용자가 esc를 누를 때까지 프로그램 수행