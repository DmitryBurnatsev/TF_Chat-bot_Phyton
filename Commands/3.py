import command_system

def team():
   message = 'Стать частью команды можно только после прохождения Школы TutorForces. Она проходит осенью, в начале каждого учебного года. Подпишись на наше сообщество и не пропусти информацию о новом наборе!'
   return message, ''

team_command = command_system.Command()

team_command.keys = ['3']
team_command.description = 'Ответ студенту'
team_command.process = team