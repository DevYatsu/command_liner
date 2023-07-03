import sys
from commands import create_command, remove_command, write_command, rename_command, generate_sh_command, destruct_sh_command
from initializer import command_client

# put all commands here
commands = list([generate_sh_command, destruct_sh_command,
                create_command, remove_command, write_command, rename_command])

# run the script
command_client.append_commands(
    *commands).run_command(sys.argv)
