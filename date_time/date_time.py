from datetime import datetime, date, time, timezone, timedelta

if __name__ == "__main__":
    some_time = time(hour=14, minute=30)  # setting time to tooth-hurty :D
    print(some_time)
    print(f"The hour is: {some_time.hour}, the minute is: {some_time.minute}")

    some_other_time = time(hour=1, minute=1, second=1, microsecond=1)
    print(some_other_time)

    today = date.today()
    print(today)
    print(f"The day is: {today.day}, the month is: {today.month}, the day is: {today.year}")
    print(today.ctime())

    some_other_day = date(year=1991, month=12, day=23)
    print(some_other_day)

    time_of_writing = datetime(year=2022,
                               month=10,
                               day=4,
                               hour=8,
                               minute=31,
                               second=21,
                               microsecond=89)
    print(time_of_writing)
    time_of_writing = time_of_writing.replace(year=2038)
    print(time_of_writing)

    now = datetime.now(tz=timezone.utc)
    print(now.isoformat())

    one_week = timedelta(days=7)
    print(f"One week ago the date was {now - one_week}")

    # ref: https://www.programiz.com/python-programming/datetime/strftime

    british_date_format = '%d-%m-%Y'
    time_format = '%H:%M:%S'
    easy_read_british_date_format = '%A, %-d %B %Y'

    # You can use the above to format datetime objects into strings following the below
    now = datetime.now(timezone.utc)
    print(now.strftime(easy_read_british_date_format))
    print(now.strftime(british_date_format))
    print(now.strftime(time_format))
    british_date_string = now.strftime(british_date_format)
    print(british_date_string)
    # You can then use those same format strings to convert a date as a string back to a datetime object like this
    datetime_object = datetime.strptime(british_date_string, british_date_format)
    print(datetime_object)
