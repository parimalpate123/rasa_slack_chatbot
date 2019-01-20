from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/current/nlu')
agent = Agent.load('./models/current/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-525465834114-524864270065-525687865621-959ed2b6ed9f82502442ed44d0cffe89', #app verification token
							'xoxb-525465834114-525382855891-SYt6HyWl7IfVyhtX19z6jJec', # bot verification token
							'N7oZdLwzfCZ3sm1syUsTn0Nl', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
