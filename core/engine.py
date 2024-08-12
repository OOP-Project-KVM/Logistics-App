from os import read
from core.application_data import ApplicationData
from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory,app_data: ApplicationData):
        self._command_factory = factory
        self.app_data = app_data

    def start(self):
        
        while True:
            if self.app_data.has_registered_users == False:
                read_input = input('Welcome, Please register a user first: ')
                command = self._command_factory.create(read_input)
                result = command.execute() # type: ignore
                print(result)

            if self.app_data.has_logged_in_user == None:
                read_input = input('Please login first: ')
                command = self._command_factory.create(read_input)
                result = command.execute() # type: ignore
                print(result)
               

            read_input = input()
            if read_input.lower() == 'end':
                break
            
            command = self._command_factory.create(read_input)
            result = command.execute() # type: ignore
            
            print(result)
 