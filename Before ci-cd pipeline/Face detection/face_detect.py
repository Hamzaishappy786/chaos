import keyboard
import pyautogui
import threading
import time

locked = False
blocked_keys = []
mouse_locked = False
stop_mouse_thread = False

UNLOCK_COMBO = {'ctrl', 'alt', 'u'}


def mouse_lock_loop(x, y):
    """Keep resetting the mouse position while locked."""
    global stop_mouse_thread
    while not stop_mouse_thread:
        pyautogui.moveTo(x, y)
        time.sleep(0.05)  # keeps the mouse 'frozen'


def lock_keyboard_and_mouse():
    global locked, blocked_keys, mouse_locked, stop_mouse_thread

    if locked:
        return

    locked = True
    print("🔒 Keyboard & Mouse locked. Press Ctrl+Alt+U to unlock.")

    # Block all keys except unlock combo
    all_keys = [chr(i) for i in range(32, 127)]
    all_keys += ['space', 'enter', 'tab', 'shift', 'ctrl', 'alt', 'caps lock',
                 'esc', 'backspace', 'delete', 'up', 'down', 'left', 'right']

    for key in all_keys:
        if key.lower() not in UNLOCK_COMBO:
            keyboard.block_key(key)
            blocked_keys.append(key)

    # Freeze mouse
    x, y = pyautogui.position()
    stop_mouse_thread = False
    t = threading.Thread(target=mouse_lock_loop, args=(x, y), daemon=True)
    t.start()
    mouse_locked = True


def unlock_keyboard_and_mouse():
    global locked, blocked_keys, mouse_locked, stop_mouse_thread

    if not locked:
        return

    # Unblock keyboard
    for key in blocked_keys:
        keyboard.unblock_key(key)
    blocked_keys.clear()
    locked = False

    # Unfreeze mouse
    stop_mouse_thread = True
    mouse_locked = False
    print("🔓 Keyboard & Mouse unlocked.")


def register_hotkeys():
    keyboard.add_hotkey('ctrl+alt+l', lock_keyboard_and_mouse)
    keyboard.add_hotkey('ctrl+alt+u', unlock_keyboard_and_mouse)


if __name__ == "__main__":
    print("Keyboard+Mouse Lock started 🚀")
    print("Press Ctrl+Alt+L to lock and Ctrl+Alt+U to unlock.")
    register_hotkeys()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting...")