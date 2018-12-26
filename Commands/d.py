import command_system

def other():
   message = 'Forward your question to [id172149289|Kate]'
   return message, ''

other_command = command_system.Command()

other_command.keys = ['d']
other_command.description = 'else'
other_command.process = other