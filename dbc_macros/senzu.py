from pynput import keyboard, mouse


# Initialize the keyboard and mouse controllers
kb_controller = keyboard.Controller()
mouse_controller = mouse.Controller()

print(kb_controller,mouse_controller)

def on_press(key):
    try:
        if key.char == 'q':  # Check if the 'Q' key is pressed
            # Press the '9' key
            print("Test")
            kb_controller.press('9')
            kb_controller.release('9')

            # Perform a right mouse button click
            mouse_controller.click(mouse.Button.right)
                
    except AttributeError:
        # This happens when a special key is pressed (like ctrl or shift), not a character key.
        pass

def main():
    print("Test")
    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
