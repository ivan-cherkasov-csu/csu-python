class CourseCatalog(object):
    __courses: list[str]
    __rooms: dict[str,str]
    __instructors: dict[str, str]
    __schedule: dict[str, str]
    
    def __init__(self) -> None:
        course = ["CSC101", "CSC102", "CSC103", "NET110", "COM241"]
        rooms = ["3004", "4501", "6755", "1244", "1411"]
        instructors = ["Haynes", "Alvarado", "Rich", "Burke", "Lee"]
        time = ["8:00 a.m.", "9:00 a.m.", "10:00 a.m.", "11:00 a.m.", "1:00 p.m."]
        self.__rooms = {}
        self.__instructors = {}
        self.__schedule = {}
        for i in range(len(course)):
            self.__rooms[course[i]] = rooms[i]
            self.__instructors[course[i]] = instructors[i]
            self.__schedule[course[i]] = time[i]
        self.__courses = course
    
    def get_list_of_courses(self) -> list[str]: return self.__courses
    
    def get_room_number(self, course: str) -> str|None: 
        return self.__rooms[course] if course in self.__rooms else None
    
    def get_instructor_name(self, course: str) -> str|None: 
        return self.__instructors[course] if course in self.__instructors else None
    
    def get_course_time(self, course: str) -> str|None: 
        return self.__schedule[course] if course in self.__schedule else None