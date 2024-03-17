from webex_bot.webex_bot import WebexBot
from webex_bot.commands.help import HelpCommand
from findMyFolk import findmyfolk
from projects import projects
from components import components

# Create a Bot Object
bot = WebexBot(teams_bot_token="MGNmNDBjMDMtODUzNC00N2YxLThjNzYtYzM0Nzc0NDdlYTE4ZmFmNDYyNjYtMTIx_P0A1_7a263a36-2e32-4816-a1bb-b51387e8b2a7",
               include_demo_commands=False)

bot.add_command(findmyfolk())
bot.add_command(projects())
#bot.add_command(components())

# Call `run` for the bot to wait for incoming messages.
bot.run()