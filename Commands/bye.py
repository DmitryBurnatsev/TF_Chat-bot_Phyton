import command_system

def bye():
   message = 'Спасибо, что обратились к нам. До свидания!'
   return message, ''

bye_command = command_system.Command()

bye_command.keys = ['пока', 'до свидания', 'спасибо']
bye_command.description = 'Прощание'
bye_command.process = bye