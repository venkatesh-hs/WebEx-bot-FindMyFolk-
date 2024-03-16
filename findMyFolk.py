from webex_bot.models.command import Command
from adaptivecardbuilder import *
from webex_bot.models.response import Response

import json
import requests
import logging

log = logging.getLogger(__name__)

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
        log.info(f"{project}")
        log.info(f"{component}")
        log.info(f"{role}")

        url = f"http://localhost:8089/v1/folks?project={project}&component={component}&role={role}"
        response = requests.get(url)
        print(response.json())
        outCard = AdaptiveCard()
        outCard.add(TextBlock(text=f"Here you go!",size="Medium", weight="Bolder"))
        outCard.add(ColumnSet())
        outCard.add(Column(width="stretch"))
        outCard.add(FactSet())
        for folk in response.json():
            print(folk)
            outCard.add(Fact(title="Name : ",value=f"{folk['name']}"))
            outCard.add(Fact(title="Component : ",value=f"{folk['domain']}"))
            outCard.add(Fact(title="Role : ",value=f"{folk['position']}"))
            outCard.add(Fact(title="------",value="---------"))
        card_data=json.loads(asyncio.run(outCard.to_json()))
        card_payload = {
            "contentType":"application/vnd.microsoft.card.adaptive",
            "content":card_data
        }

        response = Response()
        response.text="Test Card"
        response.attachments=card_payload

        response_message = f"{response.json()}"

        return response