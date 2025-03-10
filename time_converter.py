

print("----------------------------------------------")
print("Task 1: Convert a 24-hour time to AM/P time")
print("----------------------------------------------")


hours = int(input("Enter the hours (0-23): "))
minutes = int(input("Enter the minutes (0-59): "))
print()


time24 = f"{hours:02d}:{minutes:02d}"



if hours == 00:
    newhours = 12
    period = "AM"

elif hours >= 1 and hours <=11:
    newhours = hours
    period = "AM"

elif hours == 12:
    newhours = 12
    period = "PM"

elif hours >= 13 and hours <=23:
    newhours = hours-12
    period = "PM"

    
time12 = f"{newhours:02d}:{minutes:02d} {period}"


print("24-Hour Time:",time24)
print("AM/PM Time:  ",time12)
print()


if hours >= 5 and hours <= 11: 
    print("Good morning!")
    
elif hours >= 12 and hours<=17:
    print("Good afternoon!")

elif hours >= 18 and hours <=21:
    print("Good evening!")

elif hours <=4 or hours >=22:
    print ("Good night!")

print()

print("----------------------------------------------")
print("Task 2: Convert AM/PM time to 24-hour time")
print("----------------------------------------------")


hours2 = int(input("Enter the hours (0-12): "))
minutes2 = int(input("Enter the minutes (0-59): "))
am_pm = input("Enter AM or PM: ")
print()

time_12 = f"{hours2:02d}:{minutes2:02d} {am_pm}"


if am_pm == "AM" and hours2 == 12:
    newhours2 = 00
    
elif am_pm == "AM" and hours2 != 12:
    newhours2 = hours2

elif am_pm == "PM" and hours2 == 12:
    newhours2 = 12

elif am_pm == "PM" and hours != 12:
    newhours2 = hours2 + 12

time_24 = f"{newhours2:02d}:{minutes2:02}"

    
print("AM/PM Time:  ",time_12)   
print("24-Hour Time:",time_24)
print()

if am_pm == "AM":
    print("It's the start of the day!")

else:
    print("The day is almost done")

