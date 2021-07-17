
# Macro-Recorder-and-Player
This python CLI application can record mouse clicks and keyboard keypresses and play them back as many times as necessary.  There is also a minimal scripting  language supported to identify images on the screen and act accordingly.

## Installation
Open the terminal in the project root folder.
Install the python3 requirements listed in the requirments.txt file.
```sh
pip install -r requirements.txt
```

## How to use
```sh
cd src
python3 main.py  <mode>  <filename>
```

The application has available 3 modes.
- **record**: Records a macro and saves it when the ESC key is pressed. At this point only the following actions are supported: left/right click, all keyboard keypresses.
Example:  python3 main.py  record  example.macro

- **macro**: Plays back a recorded macro given its name. You can cancel the playback by moving the mouse very fast or pressing "Cntrl + C" while focused on the terminal.
Example: python3 macro example.macro
- **script**: In this mode you can code simple logic with a minimal scripting language.
The language supports conditional (if/else) statements on the condition that a predifined image is found on the screen. A predifined image is a screenshot from a part of the screen. The application takes a screenshot and searches for the image that has been placed in the images/targets folder and has been referenced in the script. If the image has been found, the application stores its coordinates so that we can use the "left_click" scripting command.
Example: python3 main.py script example.script

#### Example Script
In the code bellow we run the "login.macro" macro one time.
If the image "home.png" gets found in on the screen then we wait 2 seconds and click two times on the image (double click).
If the image does not get found on the screen, we playback a macro called "do_smthn.macro" 4 times. 
After the multiple executions of the macro we tell the script to start all over again from the begining (line 1) with the use of the "goto" command.

**Warning**: do not leave any empty line in the script file otherwise the script will not run as intended.

```` 
macro login.macro 1
if home.png
    wait 2
    left_click
    left_click
else 
    macro do_smthn.macro 4
    goto 1
````

## License
MIT
**Free Software, Hell Yeah!**
