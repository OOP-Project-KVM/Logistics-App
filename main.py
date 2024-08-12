from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
app_data.initalize_trucks()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory, app_data)

engine.start()
