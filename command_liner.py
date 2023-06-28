from command import Command
from exceptions import CommandLinerNameError, CommandNameError


class CommandLiner:
    def __init__(self, name: str):
        self.name = name
        self.commands = {}

    def list_commands(self):
        print("Commands list:")
        for key, value in self.commands.items():
            print(f"* {key}")
        return self

    def append_command(self, command: Command):
        if command.name in self.commands:
            raise CommandNameError(
                f"This command name is already taken: {command.name}")
        else:
            self.commands[command.name] = command
        return self

    def append_commands(self, *args, **kwargs):
        for arg in [*args, *kwargs]:
            self.append_command(arg)

        return self

    def run_command(self) -> Command:
        command_line = input("Enter a command: ")

        command_components = command_line.split(" ")

        if command_components[0] not in self.commands:
            raise CommandNameError(
                f"This command does not exist: {command_components[1]}")
        return self.commands[command_components[0]].parse(command_line)
