"""
    Given a year, report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

```plain
    on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
```

"""

def is_leap_year(year):
    if(year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        return "Leap year"
    if(year % 4 == 0 and year % 100 == 0):
        return "Not a leap year"
    else:
        return "Leap year"

    return "Not a leap year"

print is_leap_year(2000)
