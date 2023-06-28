# command_liner
A simple template to create a CLI (command line interface) made in python.

## Project purpose
The purpose of this project is rather simple. I wanted to share a simple way for python developers to create customizable command line interfaces. The concept here is not necessarily to create a line interface usable for everyone... it's to create a line interface usable by whoever has python installed on his computer. It could be rather simple to implement it for every computer on earth by generating an exetuble but it was not my intention here. 

## Prerequisites
To use command_liner, it should be a piece of cake if you know some python. 
You need python installed on your device to use the project.

### Copy the project
Run  `git clone https://github.com/DevYatsu/command_liner` 

### Project infrastructure
You should find 7 files in this project:
- .gitignore
- command_liner.py
- command.py
- exceptions.py
- LICENSE
- main.py
- README.md

You at least need the *.py* files to use command_liner. 

### Fundamentals
- **command.py** contains all the code regarding the creation of the command class
- **command_liner.py** contains code on the commands_wrapper class
- **exceptions.py** contains code regarding errors managing
- **main.py** is the key file, containing all the llogic of the CLI

You can look at all the files to understand the logic of the project, and modify them if necessary. However if you need a simple use of command_liner just open **main.py** in your code editor.

Now that you're in **main.py** file, you can edit *commands_prefix* variable to set the prefix you want to call your comands with. 

For example  `commands_prefix = "test"` will allow you to call your script with `test <command name>` once generated.

## LICENCE 
MIT as always...
I hereby allow you to do whatever you want with this project!
