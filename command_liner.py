from command import Command
from exceptions import CommandNameError
import shlex


class CommandLiner:
    def __init__(self, name: str):
        self.name = name
        self.commands = {
            "help": Command("help", "A command to get help.")
        }

    def list_commands(self):
        if len(self.commands) == 1 and self.commands["help"] is not None:
            return self

        print("Commands list:")
        for key in self.commands.keys():
            print(f"* {key}")
        return self

    def append_command(self, command: Command):
        if command.name != command.name.lower():
            raise ValueError(
                f"Command names must be lowercase: '{command.name}'")

        if command.name.lower() in self.commands:
            raise CommandNameError(
                f"This command name is already taken: {command.name}")
        else:
            self.commands[command.name.lower()] = command
        return self

    def append_commands(self, *args, **kwargs):
        for arg in [*args, *kwargs]:
            self.append_command(arg)

        return self

    def run_command(self, args_list: list[str] = []) -> Command:
        if len(self.commands) == 0:
            return print("No commands created.")
        if len(self.commands) == 1 and self.commands["help"] is not None:
            return print("No commands created.")

        command_components: list[str] = []

        if len(args_list) > 1:
            if args_list[0] == "main.py":
                command_components = args_list[1:]
            else:
                command_components = args_list[1:]
        else:
            command_components = shlex.split(input("Enter a command: "))

        if command_components[0].lower() not in self.commands:
            raise CommandNameError(
                f"This command does not exist: '{command_components[0]}'")

        if command_components[0].lower() == "help":
            print(
                "Command Line Interface realised with command_liner by DevYatsu on github")
            self.list_commands()
            return print("To get informations on a specific command:\n\t* <command name> --help\nTo see a command description:\n\t* <command name> --description\n")

        return self.commands[command_components[0].lower()].parse(command_components)
