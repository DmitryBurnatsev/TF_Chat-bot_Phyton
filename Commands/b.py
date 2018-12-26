import command_system

def advertisments():
   message = 'Please make sure that your advertisment follows the idea of our community and write to [id177101639|Dmitrii]'
   return message, ''

advertisments_command = command_system.Command()

advertisments_command.keys = ['b']
advertisments_command.description = 'ads'
advertisments_command.process = advertisments