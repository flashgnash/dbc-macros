from pynput import mouse, keyboard
import threading
import time


print("Testing")

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
    counter = 1
    while is_left_held:
        if counter % 2 != 0:
            # Press '1' and left mouse button
            kb_controller.press('1')
            kb_controller.release('1')
            mouse_controller.click(mouse.Button.left)
        else:
            # Press '2' and left mouse button
            kb_controller.press('2')
            kb_controller.release('2')
            mouse_controller.click(mouse.Button.left)
        
        # Alternate
        counter += 1
        
        # Add a small delay to control the speed of alternation
        time.sleep(0.1)

def main():
    # Start listening to mouse events
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()
