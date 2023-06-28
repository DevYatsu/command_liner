#!/usr/bin/env python3

from exceptions import ParameterNameError, ParametersNumberError, ScriptError


class Command:
    def __init__(self, name: str, description: str = None):
        self.name: str = name
        self.description: str = description
        self.help_msg: str = None
        self.script: list[str] = []
        self.params: list = {}
        self.params_order: list[str] = []
        self.optional_params_order: list[str] = []

    def set_description(self, new_description: str):
        self.description = new_description
        return self

    def set_help(self, new_msg: str):
        self.help_msg = new_msg
        return self

    def get_description(self):
        if self.description is None:
            return "No description was set for this command."

        return self.description

    def get_help(self):
        if self.help_msg is None:
            return "No help message was set for this command."

        return self.help_msg

    def set_script(self, script: str, *args, **kwargs):
        # self.script contains the script as the list[0] value
        # in the other cells of the list he contains the string names
        # of the dynamic parameters that will be set at exec time
        # they are represented by +++ in the script string
        self.script: list[str] = [script, *args, *kwargs]

        if len(args) + len(kwargs) > len(self.params):
            raise ParametersNumberError(
                f"Too many parameters, requires at most {len(self.params)} parameters")
        elif len(args) + len(kwargs) < len(self.params_order):
            raise ParametersNumberError(
                f"Not enough parameters, requires at least {len(self.params_order)} parameters")
        return self

    def dynamise_script(self):
        # replacing the +++ by the varibles in parameters
        script, *args = self.script
        dynamised_script = script
        for arg in args:
            print(self.params[arg][0])
            if self.params[arg][0] and not self.params[arg][1]:
                dynamised_script = dynamised_script.replace(
                    "+++", self.params[arg][0], 1)
            else:
                dynamised_script = dynamised_script.replace(
                    "+++", self.params[arg][0] if self.params[arg][0] != None else "", 1)
        return dynamised_script

    def add_parameter(self, name: str):
        if name in self.params:
            raise ParameterNameError(
                f"This parameter name is already taken: {name}")
        else:
            self.params[name] = [None, False]
            self.params_order.append(name)
        return self

    def add_optional_parameter(self, name: str):
        if name in self.params:
            raise ParameterNameError(
                f"This parameter name is already taken: {name}")
        else:
            self.params[name] = [None, True]
            self.optional_params_order.append(name)
        return self

    def add_params(self, *args):
        for param in args:
            self.add_parameter(param)
        return self

    def add_optional_params(self, *args):
        for param in args:
            self.add_optional_parameter(param)
        return self

    def parse(self, command_line_list: str):
        if len(self.script) > 0 and self.script[0] is None:
            raise ScriptError(
                f"No script was set to be run on this command call: '{self.name}'")

        parameters = command_line_list[1:]

        if len(parameters) > 0:
            if parameters[0] == "--description":
                return print(f'DESCRIPTION:\n{self.get_description()}\n')
            elif parameters[0] == "--help":
                return print(f'HELP MESSAGE:\n{self.get_help()}\n')

        order = [*self.params_order, *self.optional_params_order]

        if len(parameters) < len(self.params_order):
            if len(parameters) == 0:
                raise ParametersNumberError(
                    f"Number of parameters is lacking for {self.name} command, none was given while {len(self.params_order)} are required.")
            elif len(parameters) == 1:
                raise ParametersNumberError(
                    f"Number of parameters is lacking for {self.name} command, only 1 was given while {len(self.params_order)} are required.")
            else:
                raise ParametersNumberError(
                    f"Number of parameters is lacking for {self.name} command, only {len(parameters)} were given while {len(self.params_order)} are required.")

        for i in range(len(parameters)):
            self.params[order[i]][0] = parameters[i]

        return self.run()

    def run(self):
        executable_script = self.dynamise_script()
        exec(executable_script)
        return None
