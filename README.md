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

Now that you're in **main.py** file, you can notice the file is sort of separated in 3 parts:
1. The imports and the client iniatializer
2. All the commands declarations
3. Ready the client to run

First, you can edit *commands_prefix* variable to set the prefix you want to call your comands with. 

Then, you can take a look at the commands and understand how to create them, actually, it is rather simple, it's done in a few steps only:
1. Init a command instance with two arguments, its name and its description
2. You can also set description separately with `.set_description()`, description will be displayed when running `command_name --description`
3. Set a helper message with `.set_help()`, will be displayed when running `command_name --help`
4. Add parameters with `.add_parameter()` or `.add_params()` methods, these params are needed when running the command
5. Add **optional** parameters with `.add_optional_parameter()` or `.add_optional_params()` methods, can be add after the required ones when running the command
6. Use `.set_script()` to write the script run on command use, takes as first parameter the script to run and as others the parameters to use in the script, set them here in the position you want them to be called when using the command

### Example

Let's see a simple example of a command definition, we will suppose that all theimports are doeand that the client is generated

``` python
# first we create the command
example_command = Command("example", "An example command.")

# set help message
example_command = example_command.set_help(
    f"To run the command:\n\t* example <param1> <param2>")

# add parameters in command
example_command = example_command.add_params("param1", "param2")

# add optional params
example_command = example_command.add_optional_parameter("param3")

example_command = example_command.set_script('''
param1 = "+++"
param2 = "+++"
param3 = "+++"

print(param1)  
if param3 != "": # param3 is optional and set to "" if not add in command
    print(param3)                                            
print(param2)     
print(param1)     
print(param2) 
if param3 != "":
    print(param3)    
print(param1)     

''', "param1", "param2", "param3")

# and do not forget to put everything in commands array:

commands = list([generate_sh_command, destruct_sh_command, example_command])
# at least need the two first commands to run the script and destroy it 
```

It's as simple as that!

To make it even simpler, put everything together:
```python  
example_command = Command("example", "An example command.").set_help(
    f"To run the command:\n\t* example <param1> <param2>").add_params("param1", "param2").add_optional_parameter("param3").set_script('''
param1 = "+++"
param2 = "+++"
param3 = "+++"

print(param1)  
if param3 != "": # param3 is optional and set to "" if not add in command
    print(param3)                                            
print(param2)     
print(param1)     
print(param2) 
if param3 != "":
    print(param3)    
print(param1)     

''', "param1", "param2", "param3")
```

Ta daaa! That's it!

## LICENCE 
MIT as always...
I hereby allow you to do whatever you want with this project!
