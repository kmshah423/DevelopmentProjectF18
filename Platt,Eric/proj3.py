import json


class Group_16:
    def __init__(self, members):
        self.members = members

    def meet_up(self, day, time):
        pass

    def print_members(self):
        pass


class GroupMember:
    def __init__(self, name, major, classSchedule):
        self.name = name
        self.major = major
        self.classSchedule = classSchedule

    def print_schedule(self):
        pass


class Class:
    def __init__(self, department, classNumber, weekdays,  startTime, endTime):
        self.department = department
        self.classNumber = classNumber
        self.weekdays = weekdays
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self):
        return (f'department: {self.department}, \
                classNumber: {self.classNumber}, \
                weekdays: {self.weekdays}, \
                time: {self.startTime} - {self.endTime}')


# This is an experimental function to load class data.
# It is not yet finished
# It loads the json file containing the class information and passes it to a
# new instance of Class

def loadClasses():
    with open('classes.json', 'r') as read_file:
        data = json.load(read_file)
        print(data)
        print('\n')
        dummy = Class(data['department'],
                      data['classNumber'],
                      data['weekdays'],
                      data['start'],
                      data['end'])
        print(dummy)


if __name__ == '__main__':
    loadClasses()
