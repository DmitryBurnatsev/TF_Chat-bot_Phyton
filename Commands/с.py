import command_system

def team():
   message = 'You can join our team after graduating TutorForces School. Our trainings starts in October. Follow the TutorForces group for further information'
   return message, ''

team_command = command_system.Command()

team_command.keys = ['c']
team_command.description = 'Ответ для иностранца'
team_command.process = team