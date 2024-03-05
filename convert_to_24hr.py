s="06:15:45PM"

time = s.split(':')
is_pm = s.endswith('PM')

if is_pm:
    if int(time[0]) != 12:
        hour = int(time[0]) + 12
        print(f"{hour}:{time[1]}:{time[2].removesuffix('PM')}")
    else:
        print(f"{time[0]}:{time[1]}:{time[2].removesuffix('PM')}")
else:
    if int(time[0]) == 12:
        print(f"00:{time[1]}:{time[2].removesuffix('AM')}")
    else:
        print(f"{time[0]}:{time[1]}:{time[2].removesuffix('AM')}")

# is_pm = s[-2:].lower() == 'pm'

# time_list = list(map(int, s[:-2].split(':')))

# if is_pm and time_list[0] < 12:
#     time_list[0] += 12

# if not is_pm and time_list[0] == 12:
#     time_list[0] = 0

# print(':'.join(map(lambda x: str(x).rjust(2, '0'), time_list)))