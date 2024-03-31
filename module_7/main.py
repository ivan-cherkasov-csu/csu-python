from CourseCatalog import CourseCatalog
from os import system

if __name__ == '__main__':  
    system("cls")
    catalog = CourseCatalog()
    print("Active courses")
    for c in catalog.get_list_of_courses():
        print(c)
    while True:
        i = input("Please enter course number: ").upper()
        if i is None or i == 'Q' or i == 'EXIT' or i == 'QUIT':
            exit(0)
        else:
            room = catalog.get_room_number(i)
            if room is None:
                print(f"Course with name '{i}' not found. Please try again")
                continue
            else:
                print(f"The room number is {room} instructor's name {catalog.get_instructor_name(i)} starts at {catalog.get_course_time(i)}")
