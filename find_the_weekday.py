from math import floor
import datetime #imported this to determine the correct tense (is/was/will be {weekday} on {date})

print ("This was written by yours truly to get the \033[38;2;255;100;100mweekday\033[0m of any given date."
      "\nThis was coded according to the widely used Gregorian calender, it may not come to terms with other calenders such as Julian's."
      "\nThis is my second project after learning python, so the code may seem"+' "unprofessional"'+" but who cares? I'm a beginner anyway.\n")

#To prevent the program from crashing in case of unwanted inputs
while True:
   try:
       a= int(input("Enter the year: "))
       if not a <= 0:
          break
       print("\033[38;2;255;0;0mBE SERIOUS COME ON\033[0m")
   except ValueError:
    print("Insert an \033[38;2;255;0;0minteger\033[0m dumbass")

#The following math will determine whether the entered year is a leap year or not
x=a%4
y=a%100
z=a%400

if x == 0:
    if y == 0:
       if z == 0:
            Leap_Year = True
       else:
             Leap_Year = False
    else:
        Leap_Year = True
else:
    Leap_Year = False

#To prevent the program from crashing in case of unwanted inputs
while True:
    try:
        b= int(input("Enter the month's serial number: "))
        if 1 <= b <= 12:
           break
        else:
            print("Type \033[38;2;255;0;0m1 for January, 2 for February,... \033[0mlike that dummy :<\n")
    except ValueError:
        print("Insert only \033[38;2;255;0;0mintegers\033[0m from \033[38;2;255;0;0m1 to 12\033[0m dummy :<\n")

#Naming the months according to their corresponding value
if b==1:
    m="January"
elif b==2:
    m="February"
elif b==3:
    m="March"
elif b==4:
    m="April"
elif b==5:
    m="May"
elif b==6:
    m="June"
elif b == 7:
    m = "July"
elif b == 8:
    m = "August"
elif b == 9:
    m = "September"
elif b==10:
    m="October"
elif b==11:
    m="November"
elif b==12:
    m="December"


#To prevent the user from entering the wrong dates (like entering 30th February)
if b in [1,3,5,7,8,10,12]:
        while True:
            try:
                c = int(input("Enter the date: "))
                if 1 <= c <= 31 :
                    break
                print(f"\033[38;2;255;0;0m{m} can't exceed 31 days\033[0m")
            except ValueError:
                print("Insert only \033[38;2;255;0;0mintegers\033[0m you dummy >:\n")

elif b in [4,6,9,11]:
        while True:
            try:
                c=int(input("Enter the date: "))
                if 1 <= c <= 30:
                    break
                print(f"\033[38;2;255;0;0m{m} can't exceed 30 days\033[0m")
            except ValueError:
                print("Insert only \033[38;2;255;0;0mintegers\033[0m you dummy >:\n")
else:
    if not Leap_Year:
        while True:
            try:
                c = int(input("Enter the date: "))
                if 1 <= c <= 28:
                    break
                print(f"\033[38;2;255;0;0mFebruary can't exceed 28 days in {a}\033[0m")
            except ValueError:
                print("Insert only \033[38;2;255;0;0mintegers\033[0m you dummy >:\n")
    else:
        while True:
            try:
                c=int(input("Enter the date: "))
                if 1 <= c <= 29:
                    break
                print(f"\033[38;2;255;0;0mFebruary can't exceed 29 days in {a}\033[0m")
            except ValueError:
                print("Insert only \033[38;2;255;0;0mintegers\033[0m you dummy >:\n")




#The following math will go over your head, only I can understand it :>
if not Leap_Year:
    if b==1:
        final= c
    elif b==2:
        final= c+31
    elif b==3:
        final = c+59
    elif b==4:
        final = c+90
    elif b==5:
        final= c+120
    elif b== 6:
        final = c+151
    elif b== 7:
        final = c+181
    elif b== 8:
        final= c+ 212
    elif b== 9:
        final= c+243
    elif b==10:
        final= c+273
    elif b== 11:
        final= c+304
    elif b== 12:
        final= c+334
    t=a-1
    q= (365 * t + floor(t/4) + floor(t/400) - floor(t/100) + final) % 7  #(I discovered this formula all by myself back when I was in 10th grade)

    #Naming the weekdays according to their corresponding remainders
    if q==1:
        day="Monday"
    elif q==2:
        day="Tuesday"
    elif q==3:
        day="Wednesday"
    elif q==4:
        day="Thursday"
    elif q==5:
        day="Friday"
    elif q==6:
        day="Saturday"
    elif q==0:
         day="Sunday"


else:
    if b==1:
        final=c
    elif b==2:
        final= c+31
    elif b==3:
        final = c+60
    elif b==4:
        final = c+91
    elif b==5:
        final= c+121
    elif b== 6:
        final = c+152
    elif b== 7:
        final = c+182
    elif b== 8:
        final= c+ 213
    elif b== 9:
        final= c + 244
    elif b==10:
        final= c+ 274
    elif b== 11:
        final= c+ 305
    elif b== 12:
        final= c+336
    t = a - 1
    q = (365 * t + floor(t / 4) + floor(t / 400) - floor(t / 100) + final) % 7
    if q == 1:
        day = "Monday"
    elif q == 2:
        day = "Tuesday"
    elif q == 3:
        day = "Wednesday"
    elif q == 4:
        day = "Thursday"
    elif q == 5:
        day = "Friday"
    elif q == 6:
        day = "Saturday"
    elif q == 0:
        day = "Sunday"


#this part is for determining the correct tense, e.g. it can't be said "it is Wednesday on 1 jan, 1997", a "was" is needed for the past.
today = datetime.date.today()
if a < today.year:
    verb = "was"
elif a > today.year:
    verb = "will be"
else:
    if b < today.month:
        verb = "was"
    elif b > today.month:
        verb = "will be"
    else:
        if c < today.day:
            verb = "was"
        elif c > today.day:
            verb = "will be"
        else:
            verb = "is"



#The final part, the output
if c in [1,21,31]:
   print(f"It {verb} \033[38;2;0;255;255m{day}\033[0m on {c}st {m}, {a}")
elif c in [2,22]:
   print(f"It {verb} \033[38;2;0;255;255m{day}\033[0m on {c}nd {m}, {a}")
elif c in [3,23]:
   print(f"It {verb} \033[38;2;0;255;255m{day}\033[0m on {c}rd {m}, {a}")
else:
   print(f"It {verb} \033[38;2;0;255;255m{day}\033[0m on {c}th {m}, {a}")





         
