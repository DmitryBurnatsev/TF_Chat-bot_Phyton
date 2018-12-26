import command_system

def hello():
   message = 'Привет, друг!\nЯ новый чат-бот TutorForces.\n Пожалуйста, напиши тему своего обращения в ответ на это сообщение.\n 1 - ты иностранец\n 2 - реклама\n 3 - ты хочешь стать частью команды\n 4 - другая причина \n Write 5 for ENG'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'дратути', 'здравствуй', 'здравствуйте', 'e', 'начать']
hello_command.description = 'Меню'
hello_command.process = hello
