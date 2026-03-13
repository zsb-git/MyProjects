import calendar

class Calendar:

    def __init__(self,date):

        self.month_constants =  {  
            "1": "January",
            "2": "Februaru", 
            "3": "March", 
            "4": "April",
            "5": "May",
            "6": "June", 
            "7": "July",
            "8": "August", 
            "9": "September",
            "10": "October",
            "11": "November",
            "12": "December",}

        self.days_constants = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
        self.year, self.month, self.day = map(int, date.split("-"))
        

    def is_LeapYear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_days_in_month(self, year, month): 
        if month == 2:
            if self.is_LeapYear(year):
                return 29
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31
        
    def get_no_of_days( self, year, month, day):
        base_year = 1911
        days = 0
        while base_year < year:
            if self.is_LeapYear(base_year):
                days += 366
            else:
                days += 365
            base_year += 1
        base_month = 1
        while base_month < month:
            days += self.get_days_in_month(year, base_month)
            base_month += 1    
        start_date = 1
        while start_date < day:
            start_date += 1
            days += 1
        return days 

    def get_day(self,days):
        days = days % 7
        return days  
    def get_day_name(self,day):
        return self.days_constants[day]
    
    def display(self):
        
        print("The day is: \033[1;32m{}\033[0m".format(self.get_day_name(self.get_day(self.get_no_of_days(self.year, self.month, self.day)))))

        print("\033[1;34m{}\033[0m {}".format(Cal.month_constants[str(self.month)], self.year))

        for i in range(0, len(Cal.days_constants)):
            print("\033[1;33m{}\033[0m".format(Cal.days_constants[i]), end="\t")
        print()

        for i in range(0, Cal.get_day(Cal.get_no_of_days(self.year, self.month, 1))):
            print("\t", end="")

        for i in range(1, Cal.get_days_in_month(self.year, self.month) + 1):
            if i == self.day:
                print("\033[1;37;44m{}\033[0m".format(i), end="\t")
            else:
                print("\033[1;36m{}\033[0m".format(i), end="\t")
            if (i + Cal.get_day(Cal.get_no_of_days(self.year, self.month, 1))) % 7 == 0:
                print()

while True:
    Cal = Calendar(input("Enter date (YYYY-MM-DD): "))
    Cal.display()
    userchoice = input("Do you want to continue? (y/n): ")
    if userchoice.lower() != 'y':
        break
    print("\n")







