from command import Command
from main import get_prefix

# a few commands to understand how the mecanism works

create_command = Command("create", "A command for creating a file").set_help(f"To run the command:\n\t* {get_prefix()} create <file name>").add_parameter("file_name").set_script('''
file = open("+++", "x")
file.close()
''', "file_name")

remove_command = Command("remove", "A command for removing a file").set_help(f"To run the command:\n\t* {get_prefix()} remove <file name>").add_parameter("file_name").set_script('''
import os
os.remove("+++")
''', "file_name")

rename_command = Command("rename", "A command for renaming a file").set_help(f"To run the command:\n\t* {get_prefix()} rename <file name> <new name>").add_params("file_name", "new_name").set_script('''
import os
os.rename("+++", "+++")
''', "file_name", "new_name")

get_command = Command("get", "A command for perfoming a get request easily.").set_help(f"To run the command:\n\t* {get_prefix()} get <url to get> <file to write data in>").add_params("url", "file_name").set_script('''
import requests
r = requests.get("+++")
data = r.json()

file = open("+++", "a")
file.write("{}".format(data))
file.close()
''', "url", "file_name")

write_command = Command("write", "A command for writing content to a file").set_help(f"To run the command:\n\t* {get_prefix()} write <file to write> <content> (<mode for writing>)").add_params("file_name", "content").add_optional_parameter("mode").set_script('''
file_name = "+++"
content = "+++"
mode = "+++"

if mode is None or mode == "":
    mode = "w"

file = open(file_name, mode)
file.write(content)
file.close()
''', "file_name", "content", "mode")
