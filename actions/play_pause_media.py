from pynput.keyboard import Key, Controller

def universal_play_pause():
    keyboard = Controller()

    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)


if __name__ == "__main__":
    universal_play_pause()
