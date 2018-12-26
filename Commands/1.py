import command_system

def foreigner():
   message = 'Если хочешь участвовать в наших мероприятиях, советуем подписаться: \n 1)на нашу страницу в Facebook: https://www.facebook.com/tutorforces/ \n 2)на сообщество https://vk.com/int.polyunion \n 3)напиши [id177101639|Диме] если у тебя ещё есть вопросы\n'
   return message, ''

foreigner_command = command_system.Command()

foreigner_command.keys = ['1']
foreigner_command.description = 'Ответ для иностранца'
foreigner_command.process = foreigner
