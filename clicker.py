import pyautogui 
import time  

def auto_mouse():
    time.sleep(2.50)
    mouse_coordinates = pyautogui.position()  # just for myself
    print(mouse_coordinates)
    time.sleep(0.50)
    pyautogui.click( clicks = 10, interval = 0.25, button = 'left' )


if __name__ == '__main__':
    print(auto_mouse())
