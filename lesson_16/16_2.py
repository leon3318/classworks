from datetime import datetime, timedelta
import logging
logger = logging.getLogger("Event")
file_log = logging.FileHandler("mycode.log")
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out), level=logging.INFO)






class Event():        

    def __init__(self, title, start_time, end_time, participants, location, description):     
        self.title = title        
        self.start_time = start_time        
        self.end_time = end_time        
        self.participants = participants
        self.location = location        
        self.description = description

    def duration(self):        
        delta = self.end_time - self.start_time        
        res = int(( delta.total_seconds() ) // 60)        
        return f"Название проекта - {self.title}, длительность - {res} минут"     

    def add_participants(self, name):                
        self.participants.append(name)
        new_participants_list = ", ".join(self.participants)                
        return f"Добавлен новый участник: {name}. \nТеперь список участников выглядит так: {new_participants_list}"

    def conflicts_with(self, other_event):
        start_other, end_other = other_event                
        begin = max(start_other, self.start_time)
        end = min(end_other, self.end_time)        
        overlap = end - begin    
        if overlap.total_seconds() > 0:           
             return "Есть конфликт событий"
        return "Нет конфликта событий"    

    def __str__(self):        
        first_participant, second_participant = self.participants
        return f"Событие: {self.title} \nВремя начала: {self.start_time}, \nВремя завершения: {self.end_time}, \nУчастники: {first_participant, second_participant}, \nЛокация: {self.location}"
        
# my_event = Event(title="Восхождение", start_time = datetime(2025, 7, 29, 9, 0, 23), end_time = datetime(2025, 7, 29, 10, 5, 23), participants = ["Игорь", "Яков"], location="С-Пб", description="Описание")# print(my_event)

class Meeting(Event):
        
        def __init__(self, title, start_time, end_time, participants, location, description, agenda):
            super().__init__(title = title, start_time = start_time, end_time = end_time, participants = participants, location = location, description = description)  
            self.agenda = agenda
        
        def add_agenda_item(self, item):
            self.agenda.append(item)
            return ", ".join(self.agenda)

        def send_invites(self):
            invite = [f"{participant} получил приглашение" for participant in self.participants]
            return ",\n".join(invite)

class Call(Event):

        def __init__(self, title, start_time, end_time, participants, location, description, call_link, recording):
            super().__init__(title = title, start_time = start_time, end_time = end_time, participants = participants, location = location, description = description)
            self.call_link = call_link
            self.recording = recording
        
        def start_recording(self):
            self.recording = True
            if self.recording:
                logger.info(f"Запись началась в {self.start_time}")
                return f"Запись звонка началась!"
        
        def end_recording(self):
            self.recording = False
            if self.recording == False:
                logger.info(f"Запись закончилась в {self.end_time}")
                return f"Запись звонка закончилась!"


# meet = Meeting(title="Восхождение", start_time = datetime(2025, 7, 29, 9, 0, 23), end_time = datetime(2025, 7, 29, 10, 5, 23), participants = ["Игорь", "Яков"], 
#             location="С-Пб", description="Описание", agenda = ["Представить проект", "Ответить на вопросы", "Защитить проект" ])
# print(meet.add_agenda_item(item="Решить задачу"))
# print(meet.send_invites())
calling = Call(title="Восхождение", start_time = datetime(2025, 7, 29, 9, 0, 23), end_time = datetime(2025, 7, 29, 10, 5, 23), participants = ["Игорь", "Яков"], 
            location="С-Пб", description="Описание", call_link="http:", recording = False)
print(calling.start_recording())
print(calling.end_recording())