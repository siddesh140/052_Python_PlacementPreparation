# Q.1) Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

#  first take user fname and lname
#
# fname = input("Enter your  first name : ")
# lname = input("Enter your last name : ")
# print(f"{lname} {fname}")

# o/p ->
# E:\PYTHON\.venv\Scripts\python.exe "E:\PYTHON\Placement preparation.py"
# Enter your  first name : Siddesh
# Enter your last name : Yerawar
# Yerawar Siddesh
#
# Process finished with exit code 0

# ------------------

# .2) Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

# import calendar
# year = int(input("Enter the year: "))  # Taking Year
# month = int(input("Enter the month (1-12): "))   # Taking Month
# print(calendar.month(year, month))
# print(calendar.calendar(year, month))

# o/p:
# E:\PYTHON\.venv\Scripts\python.exe "E:\PYTHON\Placement preparation.py"
# Enter the year: 2003
# Enter the month (1-12): 5
#       May 2003
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
#  5  6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30 31

# Process finished with exit code 0

# ---------------------

# Q.3)  Write a Python program to calculate number of days between two dates.
# [ use datetime module ]
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# from datetime import date
# date1 = date(2014, 7, 2)
# date2 = date(2014, 7, 11)
# print(date1 - date2)

# o/p :

# E:\PYTHON\.venv\Scripts\python.exe "E:\PYTHON\Placement preparation.py"
# -9 days, 0:00:00
#
# Process finished with exit code 0
# -------------------------------

# .4)  Write a Python program to test whether a passed letter is a vowel or not.

ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

# o/p1:
# E:\PYTHON\.venv\Scripts\python.exe "E:\PYTHON\Placement preparation.py"
# Enter a character: a
# a is a Vowel
#
# Process finished with exit code 0

# o/p2:
# E:\PYTHON\.venv\Scripts\python.exe "E:\PYTHON\Placement preparation.py"
# Enter a character: g
# g is a Consonant
#
# Process finished with exit code 0