import time

from collections import defaultdict

def read_file(path='input'):
    with open(path) as input_file:
        for line in input_file:
            yield line

def sort_by_timestamp(lines):
    return sorted(lines, key=lambda line: get_time(line))

def get_time(line):
    form = '[%Y-%m-%d %H:%M]'
    time_string = ' '.join(line.split()[:2])
    timestamp = time.strptime(time_string, form)
    return timestamp

def get_sleeping_distribution(data):
    snoozie = defaultdict(lambda: defaultdict(int))
    for line in data:
        line = line.split()
        if line[3].startswith('#'):
            current_guard_id = line[3].strip('#')
        current_minute = int(line[1].split(':')[1].strip(']'))
        if line[2] == 'falls':
            fell_asleep_at = current_minute
        if line[2] == 'wakes':
            woke_up_at = current_minute
            asleep_during_minutes = range(fell_asleep_at, woke_up_at)
            for minute in asleep_during_minutes:
                snoozie[current_guard_id][minute] += 1

    snooziest_minutes = []
    for guard in snoozie:
        snooziest_minute_for_guard = max(snoozie[guard], key=lambda minute: snoozie[guard][minute])
        snooziest_minutes.append((guard, snooziest_minute_for_guard, snoozie[guard][snooziest_minute_for_guard]))

    slacker = max(snooziest_minutes, key=lambda i: i[2])
    return int(slacker[0]) * slacker[1]


def main():
    lines = [line for line in read_file()]
    data = sort_by_timestamp(lines)
    return get_sleeping_distribution(data)

print(main())
