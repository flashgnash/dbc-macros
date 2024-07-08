from pynput import keyboard, mouse
import threading
import time

# Initialize the mouse controller
mouse_controller = mouse.Controller()

# Flag to indicate if 'T' key is held
is_t_held = False

def on_press(key):
    global is_t_held
    try:
        if key.char == 't':  # Check if the 'T' key is pressed
            if not is_t_held:
                is_t_held = True
                # Start the autoclicking task when 'T' key is pressed
                thread = threading.Thread(target=autoclick)
                thread.start()
    except AttributeError:
        pass

def on_release(key):
    global is_t_held
    try:
        if key.char == 't':  # Check if the 'T' key is released
            is_t_held = False
    except AttributeError:
        pass

def autoclick():
    while is_t_held:
        mouse_controller.click(mouse.Button.left)
        # No delay for maximum clicking speed
        time.sleep(0.001)  # Optional: small sleep to prevent CPU overuse

def main():
    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
