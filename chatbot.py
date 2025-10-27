from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

# Get a response to a specific input
print(chatbot.get_response('Hello'))
print(chatbot.get_response('What is your name?'))