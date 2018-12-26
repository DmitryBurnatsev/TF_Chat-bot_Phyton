import command_system

def foreigner():
   message = 'If you want to participate in our activities, please subscribe: \n 1)Our Facebook page: https://www.facebook.com/tutorforces/ \n 2)Our international club vk page https://vk.com/int.polyunion \n 3)please write to [id177101639|Dmitrii] if you still have any questions \n '
   return message, ''

foreigner_command = command_system.Command()

foreigner_command.keys = ['a']
foreigner_command.description = 'Ответ для иностранца'
foreigner_command.process = foreigner