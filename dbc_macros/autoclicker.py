from pynput import mouse, keyboard
import threading
import time

# Initialize the keyboard controller
kb_controller = keyboard.Controller()
mouse_controller = mouse.Controller()

# Flag to indicate if left mouse button is held
is_left_held = False

def on_click(x, y, button, pressed):
    global is_left_held
    if button == mouse.Button.middle:
        is_left_held = pressed
        if pressed:
            # Start the alternating task when the left mouse button is pressed
            thread = threading.Thread(target=alternate_clicks)
            thread.start()
            
            mouse_controller.release(mouse.Button.left)
def alternate_clicks():
    while is_left_held:
        # Press '1' and left mouse button
        mouse_controller.click(mouse.Button.left)
        time.sleep(0.1)

def main():
    # Start listening to mouse events
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()
