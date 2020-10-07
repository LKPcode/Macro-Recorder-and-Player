import os
import json


class Storage:
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    # self.

    def write(self, events, path_to_file):
        if not os.path.exists(os.path.dirname(os.path.abspath(path_to_file))):
            os.makedirs(os.path.dirname(os.path.abspath(path_to_file)))
        the_file = open(path_to_file, "w+")
        for event in events:
            the_file.write(json.dumps(event) + "\n")
        the_file.close()

    def load_file(self, path_to_file):  # returns a list of dicts
        the_file = open(path_to_file, "r")
        event_list = []
        while True:
            # Get next line from file
            line = the_file.readline()
            # if line is empty end of file is reached
            if not line:
                break

            event_list.append(json.loads(line))

        the_file.close()

        return event_list

    def get_macros(self, folder):
        print(os.listdir(folder))
        macro_names = os.listdir(folder)
        macros = []
        count = 0
        for macro in macro_names:
            path = folder + "/" + macro
            dict = {"id": count, "name": macro, "events": self.load_file(path)}
            macros.append(dict)
            count += 1

        return macros

    def read_script(self, path_to_file):
        the_file = open(path_to_file, "r")
        operations = []
        count = 0
        while True:
            # Get next line from file
            line = the_file.readline()
            # if line is empty end of file is reached
            if not line:
                break

            line = line.split()

            operation = {
                "dont forget to write the code that loads the operation from the script"}
            if line[0] == "macro":
                operation = {"id": count, "operation": line[0],
                             "macro": line[1],
                             "rounds": line[2]}
            if line[0] == "wait":
                operation = {"id": count, "operation": line[0],
                             "seconds": line[1]}
            if line[0] == "goto":
                operation = {"id": count, "operation": line[0],
                             "line": line[1]}
            if line[0] == "if":
                operation = {"id": count, "operation": line[0],
                             "image": line[1]}
            if line[0] == "else":
                operation = {"id": count, "operation": line[0]}
            if line[0] == "end":
                operation = {"id": count, "operation": line[0]}
            if line[0] == "left_click":
                operation = {"id": count, "operation": line[0]}

            # print(line)
            operations.append(operation)
            count += 1

        the_file.close()

        return operations

    def get_scripts(self, folder):
        print(os.listdir(folder))
        script_names = os.listdir(folder)
        scripts = []
        for script in script_names:
            path = folder + "/" + script
            dict = {"name": script, "operations": self.read_script(path)}
            scripts.append(dict)

        return scripts

    def get_images(self, folder):
        print(os.listdir(folder))
        image_names = os.listdir(folder)
        images = []
        for image in image_names:
            #path = folder + "/" + image
            dict = {"name": image}
            images.append(dict)

        return images


# store = Storage()

# str = store.get_scripts("../scripts")
# print(str)
# print(store.load_file())

# print(json.loads('{"id": 0, "kind": "key_pressed", "key": "l"}\n))
