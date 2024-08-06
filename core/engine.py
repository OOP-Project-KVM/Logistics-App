
from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
        
        while True:
            read_input = input()
            if read_input.lower() == 'end':
                break
            command = self._command_factory.create(read_input)
            # result = command.execute()
            
            # print(result)
 