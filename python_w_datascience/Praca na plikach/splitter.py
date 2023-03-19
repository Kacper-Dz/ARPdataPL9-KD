# start - godzina rozpoczęcia seansu
# playtime - ile sekund oglądaliśmy
# Program ma podzielić playtime na poszczególne grupy
# Moj pomysl:
# playtime = 3.5
# start = 5.6
# time_table = []
# it = 0
# start_time = int(start)
# start_red = start - start_time
# first_time = playtime - int(playtime)
# print(first_time)
# while playtime > 0:
#     if not time_table:
#         time_table.append((playtime, start_time, 1 - first_time))
#         playtime -= 1 - first_time
#         it += 1
#     elif playtime >= 1:
#         time_table.append((playtime, start_time + it, 1))
#         playtime -= 1
#         it += 1
#     elif playtime < 1:
#         time_table.append((start_time + it, playtime))
#
# print(time_table)
# Wlasciwe rozwiazanie:

def time_split(start: float, playtime: float):
   end = start + playtime
   value_list = [0] * 10

   while start <= end:
       if int(start) + 1 > end:
           value_list[int(start)] = f"{end - start:.1f}"
           print(f"{int(start)} - {end - start:.1f}")
       else:
           value_list[int(start)] = f"{(int(start) + 1) - start:.1f}"
           print(f"{int(start)} - {(int(start) + 1) - start:.1f}")
       start = int(start) + 1

       return value_list

print(time_split(5.6, 3.5))
