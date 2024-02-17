import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # time_pattern = r"((0?\d[0-9]?)(:\d{2})? (AM|PM)) to ((0?\d)(:\d{2})? (AM|PM))"
    # ('9:00 AM', '9', ':00', 'AM', '5:00 PM', '5', ':00', 'PM')

    time_pattern = r"((0?\d|1[0-2])(:[0-5]\d)? (AM|PM)) to ((0?\d)(:[0-5]\d)? (AM|PM))"
    matches = re.search(time_pattern, s)
    # print(matches.groups())
    if matches:
        military_time = military_format(list(matches.groups()))
        return military_time
    else:
        raise ValueError

def military_format(time):
    military_time = ''

    if time[3] == 'PM':
        military_time += f"{str(int(time[1])+12)}{time[2] if time[2] else ':00'} to "
        if time[7] == 'PM':
            military_time += f"{str(int(time[5])+12)}{time[6] if time[6] else ':00'}"
        else:
            if len(time[5]) != 2:
                military_time += f"0{time[5]}{time[6] if time[6] else ':00'}"
            else:
                military_time += f"{time[5]}{time[6] if time[6] else ':00'}"
        return military_time
    else:
        if len(time[1]) != 2:
            military_time += f"0{time[1]}{time[2] if time[2] else ':00'} to "
            if time[7] == 'PM':
                military_time += f"{str(int(time[5])+12)}{time[6] if time[6] else ':00'}"
            else:
                if len(time[5]) != 2:
                    military_time += f"0{time[5]}{time[6] if time[6] else ':00'}"
                else:
                    military_time += f"{time[5]}{time[6] if time[6] else ':00'}"
        else:
            military_time += f"{time[1]}:00 to " if time[1] != '12' else '00:00 to'
            if time[7] == 'PM':
                military_time += f"{str(int(time[5])+12)}{time[6] if time[6] else ':00'}"
            else:
                if len(time[5]) != 2:
                    military_time += f"0{time[5]}{time[6] if time[6] else ':00'}"
                else:
                    military_time += f"{time[5]}{time[6] if time[6] else ':00'}"
        return military_time



if __name__ == "__main__":
    main()
