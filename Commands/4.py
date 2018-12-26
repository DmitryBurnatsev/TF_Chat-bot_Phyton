import command_system

def other():
   message = 'По прочим вопросам обращайтесь к [id172149289|Кате]'
   return message, ''

other_command = command_system.Command()

other_command.keys = ['4']
other_command.description = 'Ответ студенту'
other_command.process = other