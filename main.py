import sys
from command_liner import CommandLiner
from commands import create_command, remove_command, write_command, rename_command, generate_sh_command, destruct_sh_command, example_command

# set the prefix to run your commands once the script is usable,
# that is after running generate-sh command
commands_prefix = "commandliner"
command_client = CommandLiner(commands_prefix)


def get_prefix():
    return commands_prefix


# put all commands here
commands = list([generate_sh_command, destruct_sh_command, example_command,
                create_command, remove_command, write_command, rename_command])

# run the script
command_client.append_commands(
    *commands).run_command(sys.argv)
