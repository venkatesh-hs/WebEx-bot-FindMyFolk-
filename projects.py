from webex_bot.models.command import Command
from adaptivecardbuilder import *
from webex_bot.models.response import Response

import json
import requests
import logging

log = logging.getLogger(__name__)

class projects(Command):
    def __init__(self):
        super().__init__(command_keyword="projects",
                        card=None,
                        help_message="Show projects")
        
    def execute(self, help_message, attachment_actions, activity):
        url = f"http://localhost:8089/v1/folks/project"
        response = requests.get(url)
        print(response.json())
        outCard = AdaptiveCard()
        outCard.add(TextBlock(text=f"Here are the list of projects!",size="Medium", weight="Bolder"))
        outCard.add(ColumnSet())
        outCard.add(Column(width="stretch"))
        outCard.add(FactSet())
        outCard.add(Fact(title="Projects",value=""))
        outCard.add(Fact(title="------",value=""))
        for project in response.json():
            print(project)
            outCard.add(Fact(title=f"{project}",value=""))
        outCard.add(Fact(title="------",value=""))
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