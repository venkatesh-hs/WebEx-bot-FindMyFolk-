from webex_bot.models.command import Command
import json
import requests

with open("./input-card.json", "r") as card:
    INPUT_CARD = json.load(card)

class findmyfolk(Command):
    def __init__(self):
        super().__init__(command_keyword="findmyfolk",
                        card=INPUT_CARD,
                        help_message="Find my folk")
        
    def execute(self, help_message, attachment_actions, activity):
        project = attachment_actions.inputs['project']
        component = attachment_actions.inputs['component']
        role = attachment_actions.inputs['role']
        url = f"http://localhost:8089/v1/folks/test?project={project}&component={component}&role={role}"
        response = requests.get(url)
        print(response.content)

        response_message = f"{response.content}"

        return response_message