from listener import EventListener
from Storage import Storage
from player import Player
import sys


def main():
    if len(sys.argv) <= 2:
        print("You must provide at least <mode> AND <filepath>")
        return 0

    if sys.argv[1] == "record":
        print("Recording has begun. Save and Quit with <Esc>")
        EventListener(sys.argv[2]).start()

    elif sys.argv[1] == "run":
        Player().play_file(sys.argv[2], 1)

    elif sys.argv[1] == "script":
        Player().play_script(sys.argv[2])


if __name__ == "__main__":
    main()
