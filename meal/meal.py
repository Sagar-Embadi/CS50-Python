def main():
    # get input time from user
    answer = input("What time is it: ")
    # calling the Converted time
    time = convert(answer)
    # breakfast between 7:00 and 8:00
    if time >= 7 and time <=8:
        print("Breakfast time")
    # lunch between 12:00 and 13:00
    if time >= 12 and time <= 13:
        print("Lunch time")
    # dinner between 18:00 and 19:00
    if time >= 18 and time <= 19:
        print("Dinner time")

def convert(time):
    hours,minutes = time.split(":")
    new_minute = float(minutes)/60
    return float(hours)+ new_minute

if __name__ == "__main__":
    main()
