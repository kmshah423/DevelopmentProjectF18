


class Group_17:
    def __init__(self, group_members):
        self.group_members = group_members

    # if they don't have any classes on that day, they can meet up regardless of time
    # first check if the given day occurs in their schedule, if it does then check time
    # otherwise don't check time and add them in
    def meet_up(self, day, time):
        able_to_meet = []
        days_in_class = []
        for member in self.group_members:
            for schedule in member.class_schedules:
                day_time = schedule.start_time.split(" ")
                days_in_class.append(day_time[0])

                if day_time[0] == day and not in_time_range(day_time[1], schedule.end_time, time):
                    able_to_meet.append(member.name)

            if day not in days_in_class:
                able_to_meet.append(member.name)
            days_in_class.clear()

        if len(able_to_meet) > 0:
            for name in able_to_meet:
                print(name + ", ", end="")
            print("are able to meet at " + str(time) + " on " + day)
        else:
            print("No one can meet at the given time.")

    def print_members(self):
        for member in self.group_members:
            member.print_schedule()
            print()


class GroupMember:
    def __init__(self, name, major, class_schedules):
        self.name = name
        self.major = major
        self.class_schedules = class_schedules

    def print_schedule(self):
        print(self.name + "'s class schedule: ")
        print("========================")
        i = 1
        for class_time in self.class_schedules:
            print("Class #" + str(i) + ": ", end="")
            class_time.print_class_info()
            i += 1


class Class:
    def __init__(self, department, class_number, start_time, end_time):
        self.department = department
        self.class_number = class_number
        self.start_time = start_time
        self.end_time = end_time

    def print_class_info(self):
        print("In the " + self.department + " department, with a class number of " + str(self.class_number)
               + " starting at " + self.start_time + " and ending at " + self.end_time)


# Function for checking if a value is within a time range
def in_time_range(start_time, end_time, given_time):
    if float(end_time) >= float(given_time) >= float(start_time):
        return True
    else:
        return False


#_______TEST_AREA_________
test_class1 = Class("Computer Science", 4200, "Monday 16.00", "17.15")
test_class2 = Class("English", 3000, "Tuesday 13.00", "14.15")
test_class3 = Class("Communications", 1000, "Wednesday 4.00", "5.15")

test_classes1 = [test_class1, test_class2]
test_classes2 = [test_class2, test_class3]

test_GroupMember1 = GroupMember("Walt", "CS", test_classes1)
test_GroupMember2 = GroupMember("Jack", "English", test_classes2)

test_group_members = [test_GroupMember1, test_GroupMember2]
test_group = Group_17(test_group_members)
test_group.print_members()
test_group.meet_up("Monday", 16.20)
test_group.meet_up("Tuesday", 16.20)
test_group.meet_up("Tuesday", 13.20)
test_group.meet_up("Wednesday", 16.0)
test_group.meet_up("Friday", 17.0)

