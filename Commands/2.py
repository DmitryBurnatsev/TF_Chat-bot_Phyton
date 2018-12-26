import command_system

def advertisments():
   message = 'Просим обратить внимание, что мы рекламируем только то, что относится к тематике нашего сообщества. Если вы уверены, что ваше предложение соответствует нашим требованиям, напишите [id177101639|Диме]'
   return message, ''

advertisments_command = command_system.Command()

advertisments_command.keys = ['2']
advertisments_command.description = 'Ответ на рекламу'
advertisments_command.process = advertisments