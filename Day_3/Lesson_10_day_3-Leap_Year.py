#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.

#This is how you work out whether if a particular year is a leap year.

#on every year that is divisible by 4 with no remainder

#except every year that is evenly divisible by 100 with no remainder

#unless the year is also divisible by 400 with no remainder

#If english is not your first language or if the above logic is confusing, try using this flow chart .

#e.g. The year 2000:

#2000 ÷ 4 = 500 (Leap)

#2000 ÷ 100 = 20 (Not Leap)

#2000 ÷ 400 = 5 (Leap!)

#So the year 2000 is a leap year.

#But the year 2100 is not a leap year because:

#2100 ÷ 4 = 525 (Leap)

#2100 ÷ 100 = 21 (Not Leap)

#2100 ÷ 400 = 5.25 (Not Leap)

#Warning your output should match the Example Output format exactly, including spelling an punctuation.

# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
Primeira = year % 4
Segundo = year % 100
Terceiro = year % 400

if Terceiro == 0:
  print('Leap year')
else:
  if Segundo == 0:
    print('Not leap year')
  elif Primeira ==0:
    print('Leap year')
  else:
    print('Not leap year')
