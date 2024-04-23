from pathlib import Path

import keyboard  # pip install keyboard
import pyautogui  # pip install pyautogui


def re_type_it(file_path):
    """Retype the file"""
    # Sleep 1 second for cursor to move to the text area
    pyautogui.sleep(1)

    # Check if the file exists
    if file_path.exists() and file_path.is_file():
        # Open the file in read mode
        with file_path.open("r", encoding="utf-8") as f:
            # Read the file line by line
            for line in f:
                space_num = len(line) - len(line.lstrip(" "))
                tab_num = space_num // 4
                # Fix the cursor position
                pyautogui.hotkey("alt", "left")
                for i in range(tab_num):
                    keyboard.write("    ")
                # Type the line number
                for char in line.lstrip(" "):
                    # Type the character
                    keyboard.write(char)
                # Quit
                if keyboard.is_pressed("q"):
                    keyboard.unhook_all()
            # Fix unwanted symbols
            pyautogui.hotkey("ctrl", "l")
            pyautogui.hotkey("enter")
    else:
        print(f"File {file_path} not found or not a file.")


def bind_keys(file_path):
    """Bind the Ctrl + Alt + T keys to retype the file"""
    keyboard.add_hotkey("ctrl+alt+t", lambda: re_type_it(file_path))


if __name__ == "__main__":
    # Set the path of the file to be retyped
    file_path = Path(r"./re_type_it.py")

    bind_keys(file_path)
    keyboard.wait()
