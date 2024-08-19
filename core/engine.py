
from core.application_data import ApplicationData
from core.command_factory import CommandFactory



class Engine:
    def __init__(self, factory: CommandFactory, app_data: ApplicationData):
        self._command_factory = factory
        self.app_data = app_data

    def start(self):
        self.display_welcome_message()
        self.app_data.load_state()
        while True:
            
            self.display_initial_options()

            read_input = input('Select an option (enter the number or "end" to quit): ').strip().lower()
            if read_input == 'end':
                self.app_data.save_state()
                print("Exiting the application. Goodbye!")
                break

            self.handle_initial_selection(read_input)

    def display_welcome_message(self):
        print("Welcome to the Logistics Application!")

    def display_initial_options(self):
        print("\nPlease select an option to proceed:")
        print("\nInitial Options:")
        print("1. Register as a new employee")
        print("2. Log in as an existing employee")
        print("Enter 'end' to exit.\n")

    def handle_initial_selection(self, selection):
        if selection == '1':
            self.execute_command('registeruser')
        elif selection == '2':
            self.execute_command('loginuser')
            if self.app_data.has_logged_in_user:
                self.run_main_menu()
        else:
            print("Invalid selection. Please try again.")

    def run_main_menu(self):
        while True:
            self.display_menu()

            read_input = input('Select an option (enter the number or "end" to quit): ').strip().lower()
            if read_input == 'end':
                print("Exiting the application. Goodbye!")
                break

            self.handle_menu_selection(read_input)
            if not self.app_data.has_logged_in_user:
                break

    def display_menu(self):
        print("\nMain Menu:")
        print("1. Create Package")
        print("2. Create Route")
        print("3. Assign Truck to Route")
        print("4. Assign Package to Route")
        print("5. View Routes")
        print("6. Search Route")
        print("7. Logout")
        print("8. View Unassigned Packages")
        print('9. View Available Trucks')
        print('10. View Package Details')
        print("Enter 'end' to exit.\n")

    def handle_menu_selection(self, selection):
        menu_options = {
            '1': "createpackage",
            '2': "createroute",
            '3': "assigntrucktoroute",
            '4': "assignpackage",
            '5': "viewroutes",
            '6': "searchroute",
            '7': "logoutuser",
            '8': 'viewunassignedpackages',
            '9': 'viewavailabletrucks',
            '10': 'viewpackagedetails'
        }

        if selection in menu_options:
            command_name = menu_options[selection]
            self.execute_command(command_name)
        else:
            print("Invalid selection. Please try again.")

    def execute_command(self, command_name):
        command_input = command_name
        params = []

        if command_name == "registeruser":
            params.append(input("Enter username: "))
            params.append(input("Enter first name: "))
            params.append(input("Enter last name: "))
            params.append(input("Enter password: "))
            params.append(input("Enter role (Manager/Worker): "))
            params.append(input("Enter contact: "))

        elif command_name == "loginuser":
            params.append(input("Enter username: "))
            params.append(input("Enter password: "))

        elif command_name == "createpackage":
            params.append(input("Enter package ID: "))
            params.append(input("Enter start location: "))
            params.append(input("Enter end location: "))
            params.append(input("Enter weight (kg): "))
            params.append(input("Enter customer contact information: "))

        elif command_name == "createroute":
            params.append(input("Enter route ID: "))
            locations = input("Enter location names separated by spaces: ")
            params.extend(locations.split())

        elif command_name == "assigntrucktoroute":
            params.append(input("Enter truck ID: "))
            params.append(input("Enter route ID: "))

        elif command_name == "assignpackage":
            params.append(input("Enter package ID: "))
            params.append(input("Enter route ID: "))

        elif command_name == "searchroute":
            params.append(input("Enter start location: "))
            params.append(input("Enter end location: "))
        
        elif command_name == 'viewpackagedetails':
            params.append(input("Enter package ID: "))
        

        command_input += ' ' + ' '.join(params)

        command = self._command_factory.create(command_input)
        result = command.execute()  #type: ignore
        print(result)
