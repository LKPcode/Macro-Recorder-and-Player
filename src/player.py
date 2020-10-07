from Storage import Storage
from pynput.keyboard import Key, Controller
from pynput import keyboard
from pynput.mouse import Controller as mouse_Controller

import pyautogui as do

import time
from image_match import ImageMatch


class Player:

    def __init__(self):
        self.controler = Controller()
        self.keyboard = keyboard
        self.mouse = mouse_Controller()

        self.image_found = []
        self.image_coordinates = []

    # Special keys need to be converted from a string to their correspondent Key.object
    def convert_special_key(self, key):
        if(key == "Key.space"):
            return self.keyboard.Key.space
        if(key == "Key.ctrl"):
            return self.keyboard.Key.ctrl
        if(key == "Key.shift_r"):
            return self.keyboard.Key.shift
        if(key == "Key.backspace"):
            return self.keyboard.Key.backspace
        if(key == "Key.enter"):
            return self.keyboard.Key.enter
        return None

    def play_event(self, event):
        # print(event)
        # Pressed Event
        if(event["kind"] == "key_pressed"):
            self.controler.press(event["key"])
            self.controler.release(event["key"])
            time.sleep(round(float(event["delay"]), 6))
        elif(event["kind"] == "special_key_pressed"):
            self.controler.press(
                self.convert_special_key(event["key"]))
            self.controler.release(
                self.convert_special_key(event["key"]))
            time.sleep(round(float(event["delay"]), 6))
        # mouse Move
        elif(event["kind"] == "mouse_click_left"):
            do.moveTo(int(event["x"]), int(
                event["y"]), duration=float(event["delay"]))
            do.click(button="left")
        # click image
        elif event["kind"] == "left_click_image":
            coordinates = ImageMatch().find_image(event["image"])
            print("searched image")
            if len(coordinates) != 0:
                print("image found")
                do.moveTo(coordinates[0][0],
                          coordinates[0][1], event["delay"])
                do.click(button="left")

    def play_file(self, macro_name, rounds=1):
        events = Storage().load_file("../macros/" + macro_name)

        for x in range(0, rounds):
            for event in events:
                self.play_event(event)

    def play_script(self, script_name, line=1):
        script = Storage().read_script("../scripts/" + script_name)
        print(script)

        line = line
        while line <= len(script):
            operation = script[line - 1]
            if len(self.image_found) == 0 or self.image_found[len(self.image_found) - 1] == True:

                print("op")
                print(operation)
                if operation["operation"] == "macro":
                    self.play_file(
                        operation["macro"], int(operation["rounds"]))

                elif operation["operation"] == "wait":
                    time.sleep(float(operation["seconds"]))

                elif operation["operation"] == "goto":
                    line = int(operation["line"])
                    continue

                elif operation["operation"] == "if":
                    coordinates = ImageMatch().find_image(operation["image"])
                    print("searched image")
                    if len(coordinates) != 0:  # if image was found
                        self.image_found.append(True)
                        self.image_coordinates.append(coordinates[0])
                    else:
                        self.image_found.append(False)

                elif operation["operation"] == "else":
                    self.image_found[len(
                        self.image_found) - 1] = not self.image_found[len(self.image_found) - 1]

                elif operation["operation"] == "end":
                    self.image_found.pop()
                    self.image_coordinates.pop()

                elif operation["operation"] == "left_click":
                    xy = self.image_coordinates[len(self.image_coordinates)-1]
                    event = {"kind": "mouse_click_left",
                             "x": xy[0], "y": xy[1], "delay": 0}
                    self.play_event(event)

            else:
                print(operation)
                if operation["operation"] == "else":
                    self.image_found[len(
                        self.image_found) - 1] = not self.image_found[len(self.image_found) - 1]

                elif operation["operation"] == "end":
                    self.image_found.pop()
                    self.image_coordinates.pop()

            line += 1


# store = Storage("folder", "dope")loukasloukasloukas
# play = Player()loukas

# play.play_script("../scripts/test.script")

# myScreenshot = do.screenshot()
# myScreenshot.save(r'../images/tttest.png')
