from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

def main():
    # Initialize application data
    app_data = ApplicationData()
    app_data.initalize_trucks()  # Assuming this initializes some truck data
    
    # Load employees from the file
    # app_data.load_employees_from_file('models/Employees.txt')
    
    # Create the command factory with the application data
    cmd_factory = CommandFactory(app_data)
    
    # Create the engine with the command factory and application data
    engine = Engine(cmd_factory, app_data)
    
    # Start the engine to run the application
    engine.start()

if __name__ == "__main__":
    main()
