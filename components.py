from webex_bot.models.command import Command
from adaptivecardbuilder import *
from webex_bot.models.response import Response

import json
import requests
import logging

log = logging.getLogger(__name__)

class components(Command):
    def __init__(self):
        super().__init__(command_keyword="components",
                        card=None,
                        help_message="Show Components")
        
    def execute(self, help_message, attachment_actions, activity):
        url = f"http://localhost:8089/v1/folks/component"
        response = requests.get(url)
        print(response.json())
        outCard = AdaptiveCard()
        outCard.add(TextBlock(text=f"Here are the list of components!",size="Medium", weight="Bolder"))
        outCard.add(ColumnSet())
        outCard.add(Column(width="stretch"))
        outCard.add(FactSet())
        outCard.add(Fact(title="Components",value=""))
        outCard.add(Fact(title="------",value=""))
        for component in response.json():
            print(component)
            outCard.add(Fact(title=f"{component}",value=""))
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