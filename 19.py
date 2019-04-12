#sunday = 0, monday = 1 .. saturday = 6
#january = 0, feb = 2, december = 11

class Date:
    day_table = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    month_table = {
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December"
    }
    def __init__(self, _day, _date, _month, _year):
        self.day = _day
        self.date = _date
        self.month = _month
        self.year = _year
    
    def inc(self):
        self.day = (self.day + 1) % 7

        if self.month == 3 or self.month == 5 or self.month == 8 or self.month == 10: #april, june, september, november
            self.date = ((self.date) % 30) + 1
        elif self.month == 1 :
            if self.year % 100 == 0 and self.year % 400 != 0:
                self.date = ((self.date) % 28) + 1
            elif self.year % 4 == 0:
                self.date = ((self.date) % 29) + 1
            else:
                self.date = ((self.date) % 28) + 1
        else:
            self.date = ((self.date) % 31) + 1
        
        if self.date == 1: #this means it was just a new month
            self.month = (self.month + 1) % 12
            if self.month == 0:
                self.year += 1

    def to_string(self):
        return self.day_table[self.day] + " " + self.month_table[self.month] + " " + str(self.date) + ", " + str(self.year)

date = Date(0,1,0,1901)

count = 0
while date.year < 2001:
    if date.day == 0 and date.date == 1:
        print(date.to_string())
        count += 1
    date.inc()
print(str(count))