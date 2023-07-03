from command_liner import CommandLiner

# set the prefix to run your commands once the script is usable,
# that is after running generate-sh command
commands_prefix = "commandliner"
command_client = CommandLiner(commands_prefix)


def get_prefix():
    return commands_prefix
