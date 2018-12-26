import command_system

def hello():
   message = 'Hello my friend!\nI am a new TutorForces chat-bot.\n Please choose the letter which contains the topic you need.\n A - you are foreigner and want to participate our activities\n B - advertisements\n C - you want to be a part of a team\n D - other \n E - русскоязычное меню'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['Hello', 'Hi', 'Good morning', 'Hey', '5', 'start']
hello_command.description = 'menu'
hello_command.process = hello