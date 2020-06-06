"""
Done by Ilya Malakhov. Classes Lesson, Day, Schedule were released.
"""

from schedule import Lesson, Day, Schedule

with open('schedule.txt', encoding='utf-8') as f:
    days = []
    for line in f:
        days.append(Day(line[0], [Lesson(*x.split(',')) for x in line[2:].split(';')]))
    schedule_nsu = Schedule(days)
    print(schedule_nsu)

