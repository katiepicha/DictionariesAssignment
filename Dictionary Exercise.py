# Dictionaries
def main():

    course_number = input('Enter a course number: ')

    room_no = room_dict()
    instructor_name = instructor_dict()
    class_time = time_dict()

    course_details(course_number, room_no, instructor_name, class_time)

def room_dict():
    Room_Number = {'CS101' : 3004 , 'CS102' : 4501 , 'CS103' : 6755 , 'NT110' : 1244 , 'CM241' : 1411}
    return Room_Number

def instructor_dict():
    Instructor = {'CS101' : 'Haynes' , 'CS102' : 'Alvarado' , 'CS103' : 'Rich' , 'NT110' : 'Burke' , 'CM241' : 'Lee'}
    return Instructor

def time_dict():
    Meeting_Time = {'CS101' : '8:00 am' , 'CS102' : '9:00 am' , 'CS103' : '10:00 am' , 'NT110' : '11:00 am' , 'CM241' : '1:00 pm'}
    return Meeting_Time

def course_details(course_number, room_no, instructor_name, class_time):
    if course_number not in room_no:
        print('Invalid Course Number')
    else:
        print('Room Number: ', room_no[course_number])
        print('Instructor: ', instructor_name[course_number])
        print('Class Time: ', class_time[course_number])


main()



