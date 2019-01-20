#import json

from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.channels import HttpInputChannel
#from rasa_core.utils import EndpointConfig

# load your trained agent

#agent = Agent.load(models\current\dialogue, interpreter=RegexInterpreter())
agent = Agent.load('models/current/dialogue', interpreter='models/current/nlu')
#action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

input_channel = \
    SlackInput(slack_token='xoxb-525465834114-525382855891-SYt6HyWl7IfVyhtX19z6jJec'
               , slack_channel='@devops')  # this is the `bot_user_o_auth_access_token`

# the name of your channel to which the bot posts (optional)

# set serve_forever=True if you want to keep the server running
#agent.handle_channel(HttpInputChannel(5004, "/chat", input_channel))
agent.handle_channel(HttpInputChannel(5004, "", input_channel))

#s = agent.handle_channels([input_channel], 5004, serve_forever=False)
#agent.handle_channels([input_channel], 5004, serve_forever=True)
