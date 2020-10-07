from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput import keyboard
from Storage import Storage
import sys
import time


class EventListener:

    def __init__(self, filename):
        # Setup the listener threads
        self.keyboard_listener = KeyboardListener(
            on_press=self.on_press, on_release=self.on_release)
        self.mouse_listener = MouseListener(
            on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.count = 0
        self.delay = time.time()
        self.events = []
        self.filename = filename

    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.keyboard_listener.join()
        self.mouse_listener.join()

    def get_delay(self):
        previousTime = self.delay
        self.delay = time.time()
        return round(time.time() - previousTime, 3)

    def clean_keycode(self, code):
        if(code[0] == "'"):
            return code[1:-1]
        return code

    def on_press(self, key):
        try:
            # Write normal keys
            event = {"id": self.count, "kind": "key_pressed",
                     "key": key.char, "delay": self.get_delay()}
            print("Key pressed: {0}".format(key))
            self.events.append(event)
            self.count += 1
        except AttributeError:
            if(key == keyboard.Key.esc):  # save recording and and stop listening
                Storage().write(self.events, "../macros/" + self.filename)
                self.keyboard_listener.stop()
                self.mouse_listener.stop()

            # Write Special Keys
            print(key)
            event = {"id": self.count, "kind": "special_key_pressed",
                     "key": str(key), "delay": self.get_delay()}
            self.events.append(event)
            print('special key {0} pressed'.format(key))
            self.count += 1

    def on_click(self, x, y, button, pressed):
        if pressed:
            event = {"id": self.count, "kind": "mouse_click_left",
                     "x": x, "y": y, "delay": self.get_delay()}
            self.events.append(event)
            self.count += 1
        else:
            print('Mouse released at ({0}, {1}) with {2}'.format(x, y, button))

    def on_scroll(self, x, y, dx, dy):
        print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

    def on_release(self, key):
        pass

    def on_move(self, x, y):
        pass


# store = Storage("folder", "dope")
# EventListener(store).start()

# listener.keyboard_listener.join()
# listener.mouse_listener.join()
