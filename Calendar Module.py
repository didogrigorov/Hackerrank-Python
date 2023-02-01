from calendar import day_name, weekday

mm, dd, yyyy = map(int, input().split())
print(day_name[weekday(yyyy, mm, dd)].upper())