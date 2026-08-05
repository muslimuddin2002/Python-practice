# Task: Given a start time (hours, minutes) and an event duration
# in minutes, calculate and print the end time.
# Hint: use the % (modulo) operator to wrap hours/minutes correctly.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_minutes = hour * 60 + mins + dura

end_hour = (total_minutes // 60) % 24
end_min = total_minutes % 60

print(str(end_hour) + ":" + str(end_min))
