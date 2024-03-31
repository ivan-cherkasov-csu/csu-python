from unittest import TestCase, main
from CourseCatalog import CourseCatalog
        
class Test(TestCase):
    
    def test_can_get_list_of_curses(self):
        catalog = CourseCatalog()
        courses = catalog.get_list_of_courses()
        self.assertIsNotNone(courses)
    
    def test_can_get_room_number(self):
        catalog = CourseCatalog()
        courses = catalog.get_list_of_courses()
        for course in courses:
            self.assertIsNotNone(catalog.get_room_number(course))
            
    def test_can_get_instructor_name(self):
        catalog = CourseCatalog()
        courses = catalog.get_list_of_courses()
        for course in courses:
            self.assertIsNotNone(catalog.get_instructor_name(course))
    
    def test_can_get_course_time(self):
        catalog = CourseCatalog()
        courses = catalog.get_list_of_courses()
        for course in courses:
            self.assertIsNotNone(catalog.get_course_time(course))

if __name__ == '__main__':
    main()   