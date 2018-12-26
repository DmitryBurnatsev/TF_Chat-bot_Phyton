import command_system

def bye():
   message = 'Thanks for asking! Bye!'
   return message, ''

bye_command = command_system.Command()

bye_command.keys = ['bye', 'good bye']
bye_command.description = 'bye'
bye_command.process = bye