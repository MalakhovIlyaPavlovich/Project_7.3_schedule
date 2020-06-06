class Lesson:
    time_pairs = [
        ' 9:00 - 10:35',
        '10:50 - 12:25',
        '12:40 - 14:15',
        '14:30 - 16:05',
        '16:20 - 17:55',
        '18:10 - 19:45',
        '20:00 - 21:35',
    ]

    def __init__(self, number, type=None, title=None, classroom=None, teacher=None):
        if title == None and classroom == None:
            self.title = title
            self.number = number
            self.teacher = teacher
            self.type = type
            self.time = Lesson.time_pairs[int(number) - 1]
            self.classroom = classroom
        else:
            self.title = title
            Lesson.number_checking_exception(number)
            self.number = number
            self.teacher = teacher
            self.type = type
            self.time = Lesson.time_pairs[int(number) - 1]
            self.classroom = classroom

    def __str__(self):
        if self.title == None and self.classroom == None:
            return '{}:'.format(self.time)
        else:
            return '{}: {}, ауд.{}, {} - {}'.format(self.time, self.title, self.classroom, self.teacher, self.type)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def number_checking_exception(number):
        if not number.isdigit():
            raise ValueError('Number of pair must be a digit in th range of 1 to 7.')
        if not 1 <= int(number) <= len(Lesson.time_pairs):
            raise ValueError('Number of pair must be a digit in th range of 1 to 7.')


class Day:
    days = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье',
    ]
    def __init__(self, number, lessons):
        self.number = int(number) - 1
        self.lessons = []
        lessons_dict = {}
        for x in lessons:
            lessons_dict[x.number] = x
        for i in range(len(Lesson.time_pairs)):
            number = str(i + 1)
            if number not in lessons_dict:
                lesson = Lesson(number)
            else:
                lesson = lessons_dict[number]
            self.lessons.append(lesson)

    def __str__(self):
        s = '{:-^40}\n'.format(Day.days[self.number] + ' ')
        for x in self.lessons:
            s += str(x) + '\n'
        return s

    def __repr__(self):
        return self.__str__()


class Schedule:
    def __init__(self, days):
        days_dict = {}
        for x in days:
            days_dict[x.number + 1] = x
        for i in range(1, 8):
            if i not in days_dict:
                days_dict[i] = Day(str(i), [])
        self.monday = days_dict[1]
        self.tuesday = days_dict[2]
        self.wednesday = days_dict[3]
        self.thursday = days_dict[4]
        self.friday = days_dict[5]
        self.saturday = days_dict[6]
        self.sunday = days_dict[7]

    def __str__(self):
        s = str(self.monday) + '\n'
        s += str(self.tuesday) + '\n'
        s += str(self.wednesday) + '\n'
        s += str(self.thursday) + '\n'
        s += str(self.friday) + '\n'
        s += str(self.saturday) + '\n'
        s += str(self.sunday) + '\n'
        return s



