import datetime
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
now = datetime.date.today()
dayOfWeek = now.weekday()
today = weekDays[dayOfWeek]
daysToWeekend = 6 - dayOfWeek
print(f"There are {daysToWeekend - 1} days until the weekend.")
quotePrinted = "false"

for left in weekDays[dayOfWeek:daysToWeekend]:
    if today=="Sunday" and quotePrinted=="false":
        print("Get ready to get back into the week!")
        quotePrinted = "true"
    elif (today=="Monday" or today=="Tuesday" or today=="Wednesday") and quotePrinted=="false":
        print("Time to work!")
        quotePrinted = "true"
    elif today=="Thursday" and quotePrinted=="false":
        print("Just one more day!")
        quotePrinted = "true"
    elif quotePrinted=="false":
        print("Time off!")
        quotePrinted = "true"
    else: 
        print(left)