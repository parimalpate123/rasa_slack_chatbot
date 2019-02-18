from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
agent = Agent.load('./models/current/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-525465834114-524864270065-550012447110-1827c49d338679fe1e329374f61ee6af', #app verification token
							'xoxb-525465834114-525382855891-9wJ3kN1DTJ9Plp6r1nXt6e9v', # bot verification token
							'N7oZdLwzfCZ3sm1syUsTn0Nl', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
