# add list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# creating loop
while True:
    # getting the input date from user
    date = input("Date: ")
    try:
        # split the date by slash(/)
        month, day, year = date.split("/")
        year= year.strip()
        # check if month and day is in between 1 to 12 and 1 to 30 respectively
        if 1<=int(month)<=12 and 1<=int(day)<=31 :
            break
    except:
        try:
            if ',' in date:
                # split the date by space
                month, day, year = date.split(" ")
                # find the number of month

                for i in range(len(months)):
                    if month == months[i]:
                        month = i+1
                # removing comma from day
                day = day.replace(",","")
                # check if month and day is in between 1 to 12 and 1 to 30 respectively
                if 1<=int(month)<=12 and 1<=int(day)<=31 :
                    break
        except:
            # go to next line
            #print()
            pass
# print date & add 0 before month and day if they are less than 10
print(f"{year}-{int(month):02}-{int(day):02}")
