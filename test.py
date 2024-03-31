from calendar import Month, month_name
from datetime import datetime, date, time, timedelta
import os 
os.system("cls")

print(datetime.now().date() )

class TimeSource(object):
    def get_date(self) -> date: return datetime.now().date()
    def get_time(self) -> time: return datetime.now().time()

class Task(object):
    description: str
    day: date
    def __init__(self, todo: str, day: date) -> None:
        self.day = day
        self.description = todo

class ToDoList(object):
    __time_source: TimeSource
    __tasks: list[Task]
    
    def __init__(self, time_source: TimeSource):
       self.__time_source = time_source
       self.__tasks = []
       
    def add_task(self, todo: str):
        now = self.__time_source.get_time()
        today = self.__time_source.get_date()
        day = today if now.hour < 18 else today + timedelta(days=1)
        self.__tasks.append(Task(todo, day))