class CommandNameError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ParameterNameError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ParametersNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CommandLinerNameError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ScriptError(Exception):
    def __init__(self, message):
        super().__init__(message)
